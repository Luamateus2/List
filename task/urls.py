from django.urls import path
from .views import to_do_list_views,list_views,edit_event_views,delete_event_views,calendar_views,user_views
urlpatterns=[
   path('create/list',to_do_list_views.create_list,name='create_list'),
   path('login',view=user_views.autenticar_usuario,name='autenticar_usuario'),
    path('cadastrar/usuario',view=user_views.adicionar_usuario,name='adicionar_usuario'),
   path('list/',list_views.list,name='list'),
   path('edit/task/<int:id>/', edit_event_views.edit_event, name='edit_event'),
   path('delete/task/<int:id>/', delete_event_views.delete_event, name='delete_event'),  
   path('calendar/',calendar_views.calendar,name='calendar'),# Nova rota

]
