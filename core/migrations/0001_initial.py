# Generated migration for Frecuuency models

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre Artístico')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='participants/', verbose_name='Foto')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
                ('soundcloud', models.URLField(blank=True, verbose_name='SoundCloud')),
                ('spotify', models.URLField(blank=True, verbose_name='Spotify')),
                ('youtube', models.URLField(blank=True, verbose_name='YouTube')),
                ('website', models.URLField(blank=True, verbose_name='Sitio Web')),
                ('bio', models.TextField(blank=True, verbose_name='Biografía')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('set_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video')], max_length=10, verbose_name='Tipo de Set')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='sets/audio/', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav'])], verbose_name='Archivo de Audio')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='sets/video/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mov', 'avi'])], verbose_name='Archivo de Video')),
                ('youtube_url', models.URLField(blank=True, verbose_name='URL de YouTube')),
                ('vimeo_url', models.URLField(blank=True, verbose_name='URL de Vimeo')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='sets/thumbnails/', verbose_name='Imagen Thumbnail')),
                ('published_date', models.DateTimeField(verbose_name='Fecha de Publicación')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Set Destacado')),
                ('participants', models.ManyToManyField(related_name='sets', to='core.participant', verbose_name='Participantes')),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(verbose_name='Orden')),
                ('artist', models.CharField(max_length=200, verbose_name='Artista')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('label', models.CharField(blank=True, max_length=100, verbose_name='Sello')),
                ('duration', models.CharField(blank=True, max_length=10, verbose_name='Duración')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='core.set', verbose_name='Set')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
                'ordering': ['set', 'order'],
                'unique_together': {('set', 'order')},
            },
        ),
    ]