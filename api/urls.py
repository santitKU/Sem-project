from django.urls import path
# from . import views
from api.views import DiseaseList, DiseaseDetail, InputViewSet

urlpatterns = [
    path("", DiseaseList.as_view(), name="disease-list"),
    path("<int:pk>/", DiseaseDetail.as_view(), name="disease-detail"),
    # path("image", InputViewSet.as_view(), name="input-image"),
]