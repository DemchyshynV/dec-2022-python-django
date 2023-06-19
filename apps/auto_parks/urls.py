from django.urls import path

from .views import AutoParkListCreateView, AutoParkCarListCreateView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view()),

]
