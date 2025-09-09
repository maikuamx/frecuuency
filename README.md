# 🎧 Frecuuency
### *La plataforma definitiva para sets DJ y colaboraciones musicales*

<div align="center">

![Frecuuency Banner](https://images.pexels.com/photos/1190298/pexels-photo-1190298.jpeg?auto=compress&cs=tinysrgb&w=1200&h=400&fit=crop)

**🎵 Donde la música cobra vida • 🤝 Colaboraciones épicas • 🎛️ Sets exclusivos**

[![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)](https://docker.com/)

</div>

---

## 🌟 ¿Qué es Frecuuency?

**Frecuuency** es una plataforma exclusiva diseñada para DJs que buscan compartir su arte de manera profesional. No es solo otro reproductor de música - es un espacio curado donde cada set cuenta una historia, cada colaboración crea magia, y cada beat resuena con la pasión por la música electrónica.

### ✨ La Experiencia Frecuuency

- **🎛️ Sets Exclusivos**: Audio y video de alta calidad con reproductores integrados
- **🤝 Colaboraciones Épicas**: Conecta artistas y crea experiencias musicales únicas  
- **📱 Diseño Inmersivo**: Interfaz moderna con efectos dorados y animaciones sutiles
- **🎵 Tracklists Detalladas**: Cada track identificado con artista, sello y duración
- **🌐 Perfiles Completos**: Redes sociales, biografías y estadísticas de cada DJ

---

## 🚀 Instalación Rápida

### 🐳 Con Docker (Recomendado)

```bash
# Clona el repositorio
git clone <tu-repositorio>
cd frecuuency

# Levanta la plataforma completa
docker-compose up -d

# Crea tu cuenta de administrador
docker-compose exec web python manage.py createsuperuser

# ¡Listo! Visita http://localhost
```

### 🐍 Instalación Local

```bash
# Clona y prepara el entorno
git clone <tu-repositorio>
cd frecuuency
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Configura la base de datos
cp .env.example .env
python manage.py migrate

# Crea tu cuenta DJ
python manage.py createsuperuser

# ¡A mezclar!
python manage.py runserver
```

---

## 🎨 Paleta de Colores

<div align="center">

| Color | Hex | Uso |
|-------|-----|-----|
| 🔵 **Azul Oscuro** | `#153051` | Navegación, textos principales |
| ✨ **Dorado** | `#E9A53B` | Acentos, hover effects, CTAs |
| ⚪ **Blanco** | `#FFFFFF` | Fondos, cards, contenido |
| 🔘 **Gris Claro** | `#E5E5E5` | Bordes, elementos secundarios |

</div>

---

## 🏗️ Arquitectura del Proyecto

```
frecuuency/
├── 🎛️ core/                    # Corazón de la plataforma
│   ├── models.py               # Set, Participant, Track
│   ├── admin.py                # Panel DJ personalizado
│   ├── views.py                # Vistas públicas
│   └── urls.py                 # Rutas de navegación
├── 🎨 templates/               # Interfaces visuales
│   ├── base.html               # Template maestro
│   └── core/                   # Páginas específicas
├── 💫 static/                  # Assets estáticos
│   ├── css/style.css           # Estilos con efectos dorados
│   └── js/main.js              # Interacciones y animaciones
├── 📁 media/                   # Sets y fotos subidas
└── 🐳 Docker files             # Despliegue containerizado
```

---

## 🎵 Modelos de Datos

### 🎤 **Participant** (DJ/Artista)
```python
✨ Nombre artístico
📸 Foto de perfil (opcional)
🔗 Redes sociales (Instagram, SoundCloud, Spotify, YouTube, Website)
📝 Biografía personalizada
📅 Fecha de registro
```

### 🎛️ **Set** (Sesión Musical)
```python
🏷️ Título y descripción
🎵 Tipo: Audio o Video
📁 Archivos locales (MP3, WAV, MP4)
🔗 URLs embebidas (YouTube, Vimeo)
🖼️ Thumbnail personalizado
👥 Participantes (colaboraciones)
📅 Fecha de publicación
⭐ Flag de destacado
```

### 🎶 **Track** (Canción del Tracklist)
```python
🔢 Orden en la lista
🎤 Artista y título
🏷️ Sello discográfico
⏱️ Duración
🔗 Vinculado al Set
```

---

## 🎛️ Panel de Administración

### 🚀 Funcionalidades Exclusivas

- **📊 Dashboard Visual**: Vista previa de imágenes y estadísticas
- **🎵 Gestión de Sets**: Subida de archivos con validación automática
- **👥 Perfiles de DJs**: Gestión completa de participantes y redes sociales
- **🎶 Tracklists**: Editor inline para listas de reproducción
- **⭐ Sets Destacados**: Sistema de promoción de contenido
- **🔍 Búsqueda Avanzada**: Filtros por tipo, participantes y fechas

### 🎨 Interfaz Personalizada

El admin de Django ha sido completamente personalizado con:
- Colores de la marca Frecuuency
- Vista previa de imágenes y thumbnails
- Iconos de redes sociales con indicadores visuales
- Validación inteligente de archivos de media
- Organización por pestañas para mejor UX

---

## 🌐 Páginas Públicas

### 🏠 **Home** - Portal Principal
- Banner con degradado azul oscuro a negro
- Grid responsivo de sets con efectos hover dorados
- Filtros por tipo (Audio/Video) y categoría
- Sets destacados en carousel superior
- Estadísticas en tiempo real

### 🎵 **Set Detail** - Experiencia de Reproducción
- Reproductor integrado (HTML5 + embeds)
- Tracklist completa con metadata
- Perfiles de participantes con redes sociales
- Sets relacionados por artista
- Diseño inmersivo centrado en la música

### 👥 **Artists** - Directorio de DJs
- Grid de participantes con fotos profesionales
- Búsqueda por nombre y biografía
- Estadísticas por artista (sets, colaboraciones)
- Enlaces directos a redes sociales
- Paginación elegante

### 🔍 **Search** - Búsqueda Global
- Resultados separados por categoría
- Búsqueda en sets y participantes
- Interfaz limpia y rápida
- Sugerencias visuales

---

## 🎨 Características de Diseño

### ✨ **Efectos Visuales**
- **Resplandor Dorado**: Hover states con glow effect #E9A53B
- **Animaciones Sutiles**: Transiciones cubic-bezier suaves
- **Degradados**: Azul oscuro a negro en elementos principales
- **Microinteracciones**: Feedback visual en cada acción

### 📱 **Responsive Design**
- **Desktop**: Grid completo con sidebar y navegación expandida
- **Tablet**: Layout adaptativo con menú colapsable
- **Mobile**: Stack vertical optimizado para touch

### 🎯 **UX Principles**
- **Navegación Intuitiva**: Breadcrumbs y estados activos claros
- **Carga Progresiva**: Lazy loading para imágenes y media
- **Accesibilidad**: Contraste óptimo y navegación por teclado
- **Performance**: Optimización de assets y caché inteligente

---

## 🚀 Despliegue en Producción

### 🐳 **Docker Compose** (Recomendado)

```bash
# Configuración completa con PostgreSQL y Nginx
docker-compose up -d

# Migraciones automáticas
docker-compose exec web python manage.py migrate

# Crear superusuario
docker-compose exec web python manage.py createsuperuser
```

### ☁️ **Variables de Entorno**

```bash
SECRET_KEY=tu-clave-super-secreta-para-produccion
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
DATABASE_URL=postgres://user:pass@host:5432/frecuuency
```

### 📦 **Servicios Incluidos**
- **Django App**: Aplicación principal en puerto 8000
- **PostgreSQL**: Base de datos robusta para producción
- **Nginx**: Proxy reverso y servicio de archivos estáticos
- **Volúmenes**: Persistencia de media files y datos

---

## 🎵 Casos de Uso

### 🎛️ **Para el DJ/Administrador**
1. **Subir Sets**: Arrastra archivos o pega URLs de YouTube/Vimeo
2. **Gestionar Artistas**: Crea perfiles completos con redes sociales
3. **Crear Tracklists**: Añade metadata detallada de cada track
4. **Promocionar**: Marca sets como destacados para el banner
5. **Analizar**: Revisa estadísticas de reproducciones y engagement

### 🎧 **Para los Visitantes**
1. **Descubrir**: Explora sets por tipo, artista o colaboraciones
2. **Reproducir**: Disfruta audio/video con controles avanzados
3. **Conectar**: Sigue a los DJs en sus redes sociales
4. **Buscar**: Encuentra sets específicos o artistas favoritos
5. **Compartir**: URLs amigables para compartir sets favoritos

---

## 🛠️ Personalización Avanzada

### 🎨 **Temas Personalizados**
```css
/* Modifica static/css/style.css */
:root {
    --primary-blue: #153051;    /* Tu color principal */
    --accent-gold: #E9A53B;     /* Color de acentos */
    --custom-gradient: linear-gradient(135deg, var(--primary-blue), #000);
}
```

### 🔧 **Nuevos Tipos de Sets**
```python
# En core/models.py
SET_TYPES = [
    ('audio', 'Audio'),
    ('video', 'Video'),
    ('live', 'Live Stream'),     # Nuevo tipo
    ('podcast', 'Podcast'),      # Otro tipo
]
```

### 🌐 **Redes Sociales Adicionales**
```python
# Añade campos al modelo Participant
tiktok = models.URLField(blank=True, verbose_name="TikTok")
twitch = models.URLField(blank=True, verbose_name="Twitch")
```

---

## 📊 Métricas y Analytics

### 🎯 **KPIs Incluidos**
- Total de sets publicados
- Número de artistas registrados
- Sets más reproducidos
- Colaboraciones por mes
- Engagement por red social

### 📈 **Futuras Integraciones**
- Google Analytics para tráfico web
- Spotify API para metadata automática
- SoundCloud API para importación de sets
- Instagram API para contenido social

---

## 🔒 Seguridad y Backup

### 🛡️ **Medidas de Seguridad**
- Validación de archivos subidos
- Sanitización de URLs embebidas
- Rate limiting en búsquedas
- CSRF protection habilitado
- Headers de seguridad configurados

### 💾 **Estrategia de Backup**
```bash
# Backup de base de datos
docker-compose exec db pg_dump -U frecuuency frecuuency > backup.sql

# Backup de archivos media
tar -czf media_backup.tar.gz media/
```

---

## 🎵 Roadmap Musical

### 🚀 **Próximas Features**
- [ ] 🎧 **Playlists Públicas**: Crea listas de reproducción de sets
- [ ] 📊 **Analytics Avanzados**: Dashboard con métricas detalladas
- [ ] 🔔 **Notificaciones**: Alertas de nuevos sets por email
- [ ] 🎨 **Temas Personalizables**: Múltiples esquemas de color
- [ ] 📱 **PWA**: Aplicación web progresiva para móviles
- [ ] 🎤 **Live Streaming**: Integración con plataformas de streaming
- [ ] 🤖 **AI Recommendations**: Sugerencias basadas en gustos musicales

### 🎛️ **Integraciones Futuras**
- **Spotify Connect**: Reproducción directa en dispositivos
- **SoundCloud Pro**: Importación automática de sets
- **Beatport API**: Metadata automática de tracks
- **Social Media APIs**: Publicación automática en redes

---

## 🎧 Contribuir al Beat

### 🤝 **¿Quieres colaborar?**

Frecuuency está abierto a contribuciones de la comunidad DJ. Si tienes ideas para mejorar la plataforma:

1. **🍴 Fork** el repositorio
2. **🌿 Crea** una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **💫 Commit** tus cambios (`git commit -m 'Añade nueva funcionalidad épica'`)
4. **🚀 Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **🎉 Abre** un Pull Request

### 🎵 **Tipos de Contribuciones**
- 🐛 **Bug fixes**: Mejoras en funcionalidad existente
- ✨ **Features**: Nuevas características para DJs
- 🎨 **UI/UX**: Mejoras en diseño y experiencia
- 📚 **Documentación**: Guías y tutoriales
- 🔧 **Performance**: Optimizaciones de velocidad

---

## 🎛️ Tech Stack

<div align="center">

| Categoría | Tecnología | Propósito |
|-----------|------------|-----------|
| **🔧 Backend** | Django 4.2.7 | Framework web robusto |
| **🎨 Frontend** | HTML5 + CSS3 + JS | Interfaz moderna y responsiva |
| **🗄️ Database** | PostgreSQL / SQLite | Almacenamiento de datos |
| **📁 Media** | Django Media Files | Gestión de archivos audio/video |
| **🐳 Deploy** | Docker + Nginx | Containerización y proxy |
| **🎵 Player** | HTML5 Audio/Video | Reproductores nativos |
| **🔗 Embeds** | YouTube/Vimeo APIs | Integración de plataformas |

</div>

---

## 📞 Soporte y Comunidad

### 🎧 **¿Necesitas ayuda?**

- **📧 Email**: soporte@frecuuency.com
- **💬 Discord**: [Únete a la comunidad DJ](https://discord.gg/frecuuency)
- **📱 Instagram**: [@frecuuency_official](https://instagram.com/frecuuency_official)
- **🐛 Issues**: [Reporta bugs aquí](https://github.com/tu-usuario/frecuuency/issues)

### 🌟 **Showcase**

¿Usas Frecuuency para tu música? ¡Queremos conocer tu historia! Comparte tu plataforma con nosotros y podrías aparecer en nuestro showcase oficial.

---

## 📜 Licencia

```
🎵 Frecuuency Platform © 2025
Proyecto privado - Todos los derechos reservados

Creado con ❤️ para la comunidad DJ
Powered by Django 🐍 y mucha cafeína ☕
```

---

<div align="center">

**🎧 "Where every beat tells a story" 🎧**

*Frecuuency - Elevando la experiencia musical desde 2025*

[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)](https://github.com/tu-usuario/frecuuency)
[![Django](https://img.shields.io/badge/Powered%20by-Django-092E20?style=for-the-badge&logo=django)](https://djangoproject.com/)

</div>