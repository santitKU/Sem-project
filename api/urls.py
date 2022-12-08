from django.urls import path
from . import views
from api.views import DiseaseList, DiseaseDetail

urlpatterns = [
    path("", DiseaseList.as_view(), name="disease-list"),
    path("<int:pk>/", DiseaseDetail.as_view(), name="disease-detail"),
]