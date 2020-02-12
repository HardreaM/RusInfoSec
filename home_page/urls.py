from django.urls import path
from .views import index
from .views import ArticleAddView
from .views import ArticleDetailView
from .views import ArticleByRubricView
from .views import ArticleEditView
from .views import ArticleDeleteView
from .views import ArchiveIndexView

urlpatterns = [
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>', ArticleEditView.as_view(), name='edit'),
    path('add/', ArticleAddView.as_view(), name='add'),
    path('<int:rubric_id>/', ArticleByRubricView.as_view(), name='by_rubric'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('', index, name='index'),
]