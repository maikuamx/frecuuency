from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
import os


class Participant(models.Model):
    """Modelo para los DJs participantes"""
    name = models.CharField(max_length=100, verbose_name="Nombre Artístico")
    photo = models.ImageField(
        upload_to='participants/', 
        blank=True, 
        null=True,
        verbose_name="Foto"
    )
    instagram = models.URLField(blank=True, verbose_name="Instagram")
    soundcloud = models.URLField(blank=True, verbose_name="SoundCloud")
    spotify = models.URLField(blank=True, verbose_name="Spotify")
    youtube = models.URLField(blank=True, verbose_name="YouTube")
    website = models.URLField(blank=True, verbose_name="Sitio Web")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('participant_detail', kwargs={'pk': self.pk})

    @property
    def social_links(self):
        """Retorna lista de redes sociales activas"""
        links = []
        if self.instagram:
            links.append(('Instagram', self.instagram, 'instagram'))
        if self.soundcloud:
            links.append(('SoundCloud', self.soundcloud, 'soundcloud'))
        if self.spotify:
            links.append(('Spotify', self.spotify, 'spotify'))
        if self.youtube:
            links.append(('YouTube', self.youtube, 'youtube'))
        if self.website:
            links.append(('Website', self.website, 'globe'))
        return links


class Set(models.Model):
    """Modelo para los sets de DJ"""
    SET_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    set_type = models.CharField(
        max_length=10, 
        choices=SET_TYPES, 
        verbose_name="Tipo de Set"
    )
    
    # Archivos locales
    audio_file = models.FileField(
        upload_to='sets/audio/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['mp3', 'wav'])],
        verbose_name="Archivo de Audio"
    )
    video_file = models.FileField(
        upload_to='sets/video/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['mp4', 'mov', 'avi'])],
        verbose_name="Archivo de Video"
    )
    
    # Links embebidos
    youtube_url = models.URLField(blank=True, verbose_name="URL de YouTube")
    vimeo_url = models.URLField(blank=True, verbose_name="URL de Vimeo")
    
    # Thumbnail para el set
    thumbnail = models.ImageField(
        upload_to='sets/thumbnails/',
        blank=True,
        null=True,
        verbose_name="Imagen Thumbnail"
    )
    
    participants = models.ManyToManyField(
        Participant, 
        verbose_name="Participantes",
        related_name="sets"
    )
    
    published_date = models.DateTimeField(verbose_name="Fecha de Publicación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    is_featured = models.BooleanField(default=False, verbose_name="Set Destacado")

    class Meta:
        verbose_name = "Set"
        verbose_name_plural = "Sets"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('set_detail', kwargs={'pk': self.pk})

    @property
    def participants_list(self):
        """Retorna lista de nombres de participantes"""
        return ", ".join([p.name for p in self.participants.all()])

    @property
    def is_collaboration(self):
        """Determina si es una colaboración (más de un participante)"""
        return self.participants.count() > 1

    @property
    def media_url(self):
        """Retorna la URL del archivo de media según el tipo"""
        if self.set_type == 'audio' and self.audio_file:
            return self.audio_file.url
        elif self.set_type == 'video' and self.video_file:
            return self.video_file.url
        elif self.youtube_url:
            return self.youtube_url
        elif self.vimeo_url:
            return self.vimeo_url
        return None

    @property
    def embed_url(self):
        """Retorna URL embebida para YouTube/Vimeo"""
        if self.youtube_url:
            video_id = self.youtube_url.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif self.vimeo_url:
            video_id = self.vimeo_url.split('/')[-1]
            return f"https://player.vimeo.com/video/{video_id}"
        return None

    def clean(self):
        """Validación personalizada"""
        from django.core.exceptions import ValidationError
        
        if self.set_type == 'audio':
            if not self.audio_file:
                raise ValidationError('Se requiere un archivo de audio para sets de tipo Audio.')
        elif self.set_type == 'video':
            if not (self.video_file or self.youtube_url or self.vimeo_url):
                raise ValidationError('Se requiere un archivo de video o URL para sets de tipo Video.')


class Track(models.Model):
    """Modelo para las canciones del tracklist"""
    set = models.ForeignKey(
        Set, 
        on_delete=models.CASCADE, 
        related_name='tracks',
        verbose_name="Set"
    )
    order = models.PositiveIntegerField(verbose_name="Orden")
    artist = models.CharField(max_length=200, verbose_name="Artista")
    title = models.CharField(max_length=200, verbose_name="Título")
    label = models.CharField(max_length=100, blank=True, verbose_name="Sello")
    duration = models.CharField(max_length=10, blank=True, verbose_name="Duración")

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
        ordering = ['set', 'order']
        unique_together = ['set', 'order']

    def __str__(self):
        return f"{self.order}. {self.artist} - {self.title}"