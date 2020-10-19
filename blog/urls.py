

from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('post/<int:pk>/',DetailsView.as_view(),name='post_details'),
    path('post/new',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',BlogUpadateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),
    path('signup',SignUpView.as_view(),name='signup')

]
