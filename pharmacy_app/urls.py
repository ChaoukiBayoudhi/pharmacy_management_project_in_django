from django.urls import path,include
from rest_framework import routers
from .views import DoctorViewSet,PatientViewSet,DrugViewSet
#get the default router defined by DRF and then add our routers
#for each model
router=routers.DefaultRouter()
#add routers for doctors management
router.register(r'doctors',DoctorViewSet)
#add routers for patients management
router.register(r'patients',PatientViewSet)
#add routers for drugs management
router.register(r'drugs',DrugViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
