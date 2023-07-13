from django.urls import path

from .views import AutoParkCarListCreateView, AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_parks_retrieve_update_destroy'),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view()),

]
