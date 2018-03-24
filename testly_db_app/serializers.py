from rest_framework import serializers
from .models import WoodTable


class WoodTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WoodTable
        fields = ['id', 'text', 'parent', 'tree_id', 'level']