from rest_framework import viewsets
from .models import Page
from .serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self):
        url = self.request.query_params.get('url', None)
        if url:
            queryset = Page.objects.filter(url=url)
        else:
            queryset = Page.objects.all()
        return queryset
