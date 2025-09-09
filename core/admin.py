from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Participant, Set, Track


class TrackInline(admin.TabularInline):
    """Inline para gestionar tracks dentro del admin de Sets"""
    model = Track
    extra = 1
    fields = ['order', 'artist', 'title', 'label', 'duration']
    ordering = ['order']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_photo_preview', 'get_social_links', 'sets_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'bio']
    readonly_fields = ['created_at', 'get_photo_preview']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'photo', 'get_photo_preview', 'bio')
        }),
        ('Redes Sociales', {
            'fields': ('instagram', 'soundcloud', 'spotify', 'youtube', 'website'),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def get_photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 8px;" />',
                obj.photo.url
            )
        return "Sin foto"
    get_photo_preview.short_description = "Vista previa"

    def get_social_links(self, obj):
        links = []
        if obj.instagram:
            links.append('<span style="color: #E9A53B;">IG</span>')
        if obj.soundcloud:
            links.append('<span style="color: #E9A53B;">SC</span>')
        if obj.spotify:
            links.append('<span style="color: #E9A53B;">SP</span>')
        if obj.youtube:
            links.append('<span style="color: #E9A53B;">YT</span>')
        if obj.website:
            links.append('<span style="color: #E9A53B;">WEB</span>')
        return format_html(' | '.join(links)) if links else "Sin redes"
    get_social_links.short_description = "Redes Sociales"

    def sets_count(self, obj):
        count = obj.sets.count()
        return format_html(
            '<span style="color: #153051; font-weight: bold;">{}</span>',
            count
        )
    sets_count.short_description = "Sets"


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'get_thumbnail_preview', 
        'set_type', 
        'get_participants', 
        'is_collaboration',
        'is_featured',
        'published_date'
    ]
    list_filter = ['set_type', 'is_featured', 'published_date', 'participants']
    search_fields = ['title', 'description', 'participants__name']
    filter_horizontal = ['participants']
    readonly_fields = ['created_at', 'updated_at', 'get_thumbnail_preview']
    inlines = [TrackInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'set_type', 'is_featured')
        }),
        ('Archivos de Media', {
            'fields': ('audio_file', 'video_file', 'youtube_url', 'vimeo_url', 'thumbnail', 'get_thumbnail_preview'),
            'description': 'Sube un archivo local O proporciona una URL de YouTube/Vimeo'
        }),
        ('Participantes', {
            'fields': ('participants',)
        }),
        ('Publicación', {
            'fields': ('published_date',)
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 8px;" />',
                obj.thumbnail.url
            )
        return "Sin thumbnail"
    get_thumbnail_preview.short_description = "Preview"

    def get_participants(self, obj):
        participants = obj.participants.all()
        if participants:
            names = [p.name for p in participants]
            return format_html(
                '<span style="color: #E9A53B;">{}</span>',
                ', '.join(names)
            )
        return "Sin participantes"
    get_participants.short_description = "Participantes"

    def save_model(self, request, obj, form, change):
        """Validación antes de guardar"""
        obj.clean()
        super().save_model(request, obj, form, change)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'set', 'artist', 'title', 'label', 'duration']
    list_filter = ['set', 'label']
    search_fields = ['artist', 'title', 'set__title']
    ordering = ['set', 'order']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editando
            return ['set']
        return []