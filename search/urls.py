from django.conf.urls import url

from .views import (
        SearchProductView
        )

app_name = 'search'
urlpatterns = [
    url('', SearchProductView.as_view(), name='query'),
]
