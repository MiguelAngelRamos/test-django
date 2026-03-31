from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

class Producto(models.Model):
    CATEGORIAS = [
        ('Notebooks', 'Notebooks'),
        ('Smartphones', 'Smartphones'),
        ('Tablets', 'Tablets'),
        ('Accesorios', 'Accesorios'),
    ]

    nombre = models.CharField(
        max_length=150, 
        validators=[MinLengthValidator(3, "El nombre debe tener al menos 3 caracteres.")]
    )
    descripcion = models.TextField(
        validators=[MinLengthValidator(10, "La descripción debe ser más detallada (mínimo 10 caracteres).")]
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01, "El precio debe ser mayor a 0.")]
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0, "El stock no puede ser negativo.")]
    )
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    imagen_url = models.URLField(
        max_length=500, 
        blank=True, 
        null=True, 
        help_text="URL de la imagen del producto"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"
