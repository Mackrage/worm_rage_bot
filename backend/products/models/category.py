from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from app.mixins import UpdateFieldsMixin


class Category(MPTTModel, UpdateFieldsMixin):
    title = models.CharField(max_length=120, verbose_name='Название категории')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            verbose_name='Родитель', on_delete=models.CASCADE)

    objects = models.Manager()
    bulk_update_or_create = BulkUpdateOrCreateQuerySet.as_manager()

    class Meta:
        verbose_name = '(Под)Категория'
        verbose_name_plural = 'Категорий (дерево)'
        default_related_name = 'categories'
        ordering = ('title',)

    def __str__(self):
        return f'Категория {self.title}' if not self.parent else f'Категория {self.title} {self.parent}'
