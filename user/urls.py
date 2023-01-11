from django.urls import path

from .views import (
    CustomerListView,
    CustomerDetailsView,
)


urlpatterns = [
    path("users/", CustomerListView.as_view()),
    path("users/<int:pk>/", CustomerDetailsView.as_view()),

]
