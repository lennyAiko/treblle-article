from django.urls import path
from .views import ArticleListView, ArticleUpdateDestroyView

urlpatterns = [
	path('', ArticleListView.as_view(), name='article_list_view'),
	path('<int:pk>', ArticleUpdateDestroyView.as_view(), name='article_update_destroy_view'),
]

