from django.urls import path

from .views import (
    TransactionListView,
    TransactionDetailsView,
    TransactionCreateView,
    TransactionUpdateView,
)


urlpatterns = [
    path("transactions/", TransactionListView.as_view()),
    path("transactions/<int:pk>/", TransactionDetailsView.as_view()),
    path("transactions/create/", TransactionCreateView.as_view()),
    path("transactions/update/<int:pk>/", TransactionUpdateView.as_view()),

]
