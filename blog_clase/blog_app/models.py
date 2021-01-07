from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
            .filter(estado='publico')


class Post(models.Model):
    opciones_estado = (
        ('privado', 'Privado'),
        ('publico', 'Publico')
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publicado')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Blog_app_posts')
    body = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=11, choices=opciones_estado, default='publico')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publicado',);

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('Blog_app:detalles_post',
                       args=[self.publicado.year, self.publicado.month, self.publicado.day, self.slug])

