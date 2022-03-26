from django.db import models
from django.conf import settings

# app
from applications.artists import Artist


# 3
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# 
class Category(TimeStampedModel):
    """  Categorias de una entrada  """
    # 
    name = models.CharField(
        'Nombre', 
        max_length=30
    )
    # 
    short_name = models.CharField(
        'Nombre corto', 
        max_length=15,
        unique=True
    )
# 
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
# 
    def __str__(self):
        return self.name
    
# 
class Tag(TimeStampedModel):
    """ Etiquetas de un Post """

    name = models.CharField(
        'Nombre', 
        max_length=30
    )
# 
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
# 
    def __str__(self):
        return self.name
    
# 
class Commentary(TimeStampedModel):
    """ Comentarios """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # 
    commentary = models.TextField(max_length=500)

    
# 
class Post(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # 
    post_title = models.CharField(
        'Titulo', 
        max_length=100
    )
    # 
    tag = models.ManyToManyField(Tag)
    # 
    post_category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    # 
    featured_image = models.ImageField(
        'Imagen', 
        upload_to='media/post/'
    )
    post_description = RichTextUploadingField(
        'Descripcion',
    )
    # 
    post_content = RichTextUploadingField(
        'Contenido',
    )
    # 
    public = models.BooleanField(
        'Publico',
        default=False
    )
    # 
    slug = models.SlugField(
        editable=False, 
        max_length=300
    )
    # 
    artist = models.ForeignKey(
        'Artista',
        Artist, 
        on_delete=models.CASCADE
    )
    # 
    commentary = models.ForeignKey(
        'Comentario',
        Commentary, 
        on_delete=models.CASCADE
    )
    