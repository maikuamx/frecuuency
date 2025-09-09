#!/bin/bash

# Exit on any error
set -e

echo "🎵 Iniciando Frecuuency Platform..."

# Wait for database to be ready
echo "⏳ Esperando base de datos..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "✅ Base de datos lista!"

# Run migrations
echo "🔄 Ejecutando migraciones..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "👤 Verificando superusuario..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print("🎛️ Creando superusuario por defecto...")
    User.objects.create_superuser('admin', 'admin@frecuuency.com', 'frecuuency2025')
    print("✅ Superusuario creado: admin / frecuuency2025")
else:
    print("✅ Superusuario ya existe")
EOF

echo "🚀 Frecuuency está listo para rockear!"

# Start the application
exec "$@"