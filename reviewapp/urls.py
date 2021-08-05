from django.urls import path
from . import views


urlpatterns = [
    path('review_list/', views.review_list, name='review_list'),
    path('review_detail/', views.review_detail, name='review_detail'),
]