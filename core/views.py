from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Set, Participant


def home(request):
    """Página principal con grid de sets"""
    # Filtros
    set_type = request.GET.get('type')
    category = request.GET.get('category')
    
    sets = Set.objects.prefetch_related('participants', 'tracks').all()
    
    # Filtrar por tipo
    if set_type in ['audio', 'video']:
        sets = sets.filter(set_type=set_type)
    
    # Filtrar por categoría
    if category == 'featured':
        sets = sets.filter(is_featured=True)
    elif category == 'collaborations':
        sets = sets.annotate(participant_count=Count('participants')).filter(participant_count__gt=1)
    elif category == 'solo':
        sets = sets.annotate(participant_count=Count('participants')).filter(participant_count=1)
    
    # Paginación
    paginator = Paginator(sets, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Sets destacados para banner
    featured_sets = Set.objects.filter(is_featured=True)[:3]
    
    context = {
        'page_obj': page_obj,
        'featured_sets': featured_sets,
        'current_type': set_type,
        'current_category': category,
        'total_sets': Set.objects.count(),
        'total_participants': Participant.objects.count(),
    }
    
    return render(request, 'core/home.html', context)


def set_detail(request, pk):
    """Página de detalle y reproducción de set"""
    set_obj = get_object_or_404(
        Set.objects.prefetch_related('participants', 'tracks'), 
        pk=pk
    )
    
    # Sets relacionados (mismos participantes)
    related_sets = Set.objects.filter(
        participants__in=set_obj.participants.all()
    ).exclude(pk=set_obj.pk).distinct()[:4]
    
    context = {
        'set': set_obj,
        'tracks': set_obj.tracks.all(),
        'related_sets': related_sets,
    }
    
    return render(request, 'core/set_detail.html', context)


def participants_list(request):
    """Página de listado de participantes"""
    search = request.GET.get('search')
    
    participants = Participant.objects.annotate(
        sets_count=Count('sets')
    ).prefetch_related('sets')
    
    if search:
        participants = participants.filter(
            Q(name__icontains=search) | Q(bio__icontains=search)
        )
    
    # Paginación
    paginator = Paginator(participants, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search': search,
    }
    
    return render(request, 'core/participants.html', context)


def participant_detail(request, pk):
    """Página de detalle de participante"""
    participant = get_object_or_404(Participant, pk=pk)
    participant_sets = participant.sets.all()
    
    # Estadísticas
    total_sets = participant_sets.count()
    audio_sets = participant_sets.filter(set_type='audio').count()
    video_sets = participant_sets.filter(set_type='video').count()
    collaborations = participant_sets.annotate(
        participant_count=Count('participants')
    ).filter(participant_count__gt=1).count()
    
    context = {
        'participant': participant,
        'sets': participant_sets,
        'stats': {
            'total_sets': total_sets,
            'audio_sets': audio_sets,
            'video_sets': video_sets,
            'collaborations': collaborations,
        }
    }
    
    return render(request, 'core/participant_detail.html', context)


def search(request):
    """Vista de búsqueda global"""
    query = request.GET.get('q', '')
    
    sets = Set.objects.none()
    participants = Participant.objects.none()
    
    if query:
        sets = Set.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(participants__name__icontains=query)
        ).distinct()
        
        participants = Participant.objects.filter(
            Q(name__icontains=query) |
            Q(bio__icontains=query)
        ).distinct()
    
    context = {
        'query': query,
        'sets': sets,
        'participants': participants,
        'total_results': sets.count() + participants.count(),
    }
    
    return render(request, 'core/search.html', context)