from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class WoodTable(MPTTModel):
    text = models.CharField(max_length=120, unique=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True,
                            on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['text']

    def __str__(self):
        return '{}'.format(self.text)