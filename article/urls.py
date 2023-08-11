from django.urls import path
from .views import ArticleListView, ArticleUpdateDestroyView

urlpatterns = [
	path('article/', ArticleListView.as_view(), name='article_list_view'),
	path('article/<int:pk>', ArticleUpdateDestroyView.as_view(), name='article_update_destroy_view'),
]

