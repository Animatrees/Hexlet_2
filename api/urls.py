from django.urls import path

from api.spectacular.urls import urlpatterns as doc_urls
from genetic_test import views

app_name = 'api'

urlpatterns = [
    path('tests/', views.TestListAPIView.as_view()),
    # path('tests/<int:pk>', views.TestDetailAPIView.as_view()),
    path('statistics/', views.StatisticsView.as_view()),
]

urlpatterns += doc_urls
