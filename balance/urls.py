from django.urls import path

from .views import TransactionListView, TransactionDetailsView


urlpatterns = [
    path("transactions/", TransactionListView.as_view()),
    path("transactions/<int:pk>/", TransactionDetailsView.as_view()),

]
