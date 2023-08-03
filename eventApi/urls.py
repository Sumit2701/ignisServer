from django.urls import path
from .views import event_create, event_list,register,login

urlpatterns = [
    path('api/event/create', event_create, name='event-create'),
    path('api/event/list', event_list, name='event-list'),
    path("api/register", register, name="register"),
    path("api/login", login, name="login")
 
]
