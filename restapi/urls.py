from django.urls import path
from .views import WorkList, RegisterUser

urlpatterns = [
    path('api/works', WorkList.as_view(), name='work-list'),
    path('api/register', RegisterUser.as_view(), name='register'),
]
