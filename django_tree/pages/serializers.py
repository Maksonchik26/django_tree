from rest_framework import serializers
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['name', 'url', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        serializer = self.__class__(children, many=True)
        return serializer.data
