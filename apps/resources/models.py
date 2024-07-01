from django.db import models
from apps.common.models import BaseModel
# Create your models here.

RESOURCES_PERMISSIONS = (
    ('all', 'Barcha uchun'),
    ('grether', 'Kattalar uchun'),
    ('students', 'O\'quvchilar uchun'),
    ('teachers', 'O\'qituvchilar uchun')
)

RESOURCE_STATUS = (
    ('free', 'Bepul'),
    ('partial', 'Qisman ochiq'),
    ('premium', 'Premium')
    
)

class ResourceType(BaseModel):
    name = models.CharField(max_length=30, verbose_name='Resurs turi')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Resurs turi'
        verbose_name_plural = 'Resurslar turi'


class Language(BaseModel):
    name = models.CharField(max_length=30, verbose_name='Til')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Til'
        verbose_name_plural = 'Tillar'


class Resource(BaseModel):
    photo = models.ImageField(upload_to='resources/', verbose_name='Rasm', null=True, blank=True)
    file = models.FileField(upload_to='resources/', verbose_name='Fayl')
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsif')
    author = models.CharField(max_length=100, verbose_name='Muallif', null=True, blank=True)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True, verbose_name='Resurs turi')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name='Til')
    country = models.CharField(max_length=30, verbose_name='Mamlakat', null=True, blank=True)
    year = models.PositiveIntegerField(verbose_name='Yil', null=True, blank=True)
    direction = models.CharField(max_length=100, verbose_name='Yo\'nalish', null=True, blank=True)
    pages = models.PositiveIntegerField(verbose_name='Sahifalar soni', null=True, blank=True)
    keywords = models.CharField(max_length=255, verbose_name='Kalit so\'zlar', null=True, blank=True)
    permission = models.CharField(max_length=30, choices=RESOURCES_PERMISSIONS, default='all', verbose_name='Ruxsat')
    status = models.CharField(max_length=30, choices=RESOURCE_STATUS, default='free', verbose_name='Holat')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Resurs'
        verbose_name_plural = 'Resurslar'
