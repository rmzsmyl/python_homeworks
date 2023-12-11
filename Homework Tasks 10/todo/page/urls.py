from django.urls import path
from . import views
from . views import TodoList

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    # path('list/', views.list, name='list'),
    path('list/', TodoList.as_view(), name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete<int:id>', views.delete, name='delete'),
    path('search', views.search, name='search'),
]
