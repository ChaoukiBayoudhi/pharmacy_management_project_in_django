from django.shortcuts import render

#We use viewsets.ModelViewSet
#It's a class that provides the implementation for CRUD (CREATE READ UPDATE DELETE) operations
#WE just provide the queryset and serializer_class
#We can also add custom methods to this class
#In django, we have this methods :
#Doctor.objects.all() <==> SELECT * FROM Doctor =>running using the GET method
#d1=Doctor('Ahmed','Ben Mohamed','1990-01-01')
#Doctor.objects.create(d1) <==> INSERT INTO Doctor VALUES() =>running using the POST method
#Or Doctor.objects.save(d1)
#save() is used for updating an existing object or create a new one
#D1=Doctor.objects.get(id=1) <==> SELECT * FROM Doctor WHERE id=1 =>running using the GET method
#d1=Doctor.objects.get(id=1) or d1=Doctor.objects.filter(id=1) or d1.objects.get(pk=1)
#Doctor.objects.save(d1) <==> UPDATE Doctor SET firstName='Ahmed',lastName='Ben Mohamed',birthDate='1991-01-01' WHERE id=1 =>running using the PUT method
#Doctor.objects.delete(d1) <==> DELETE FROM Doctor WHERE id=1 =>running using the DELETE method
#If we want to implement a custom query, we can use filter() or exclude() or aggregate() or order_by() or values() or values_list() or distinct() or count() or exists() or get() or first() or last() or in_bulk() or iterator() or raw() or extra() or defer() or only() or using() or select_related() or prefetch_related() or annotate() or update() or reverse() or dates() or datetimes() or none() or all() or union() or intersection() or difference() or select_for_update() or select_for_update(nowait=False, skip_l
#Examples of use of filter and exclude
#Doctor.objects.filter(firstName='Ahmed') <==> SELECT * FROM Doctor WHERE firstName='Ahmed'
#get Doctors born after 1990
#Doctor.objects.filter(birthDate__year__gt=1990) <==> SELECT * FROM Doctor WHERE birthDate>'1990-01-01'
#we have __gt for greater than
#we have __gte for greater than or equal
#we have __lt for less than
#we have __lte for less than or equal
#we have __exact for equal (==)
#we have __iexact for equal (==) case insensitive
#we have __contains for LIKE %value% or __icontains
#we have __startswith for LIKE value% or __istartswith
#we have __endswith for LIKE %value or __iendswith
#we have __range for BETWEEN
#we have __in for IN
#we have __isnull for IS NULL
#example of use of is null check
#get doctors with null photo
#result=doctor.objects.filter(photo__isnull=True)
#exclude() is the opposite of filter()
#Doctor.objects.exclude(specialty__in=['Cardiology','Dermatology']) <==> SELECT * FROM Doctor WHERE specialty NOT IN ('Cardiology','Dermatology')
# if we want to project the result of a query, we can use values() or values_list() (show only the selected fields)
#Doctor.objects.values('firstName','lastName') <==> SELECT firstName,lastName FROM Doctor
#Return doctors ordered by birthDate and specialty
#Doctor.objects.order_by('birthDate','specialty') <==> SELECT * FROM Doctor ORDER BY birthDate,specialty
#Return doctors ordered by birthDate and specialty DESC
#Doctor.objects.order_by('-birthDate','-specialty') <==> SELECT * FROM Doctor ORDER BY birthDate DESC,specialty DESC
#return doctors with distinct specialty
#Doctor.objects.distinct('specialty') <==> SELECT DISTINCT specialty FROM Doctor
#return doctors number
#Doctor.objects.count() <==> SELECT COUNT(*) FROM Doctor
#return the average of doctors age using the birthDate field
#Doctor.objects.aggregate(Avg('birthDate')) <==> SELECT AVG(birthDate) FROM Doctor

#Implementing the CRUD operations using viewsets.ModelViewSet for each model : Doctor,Patient,Drug, ...
from rest_framework import viewsets
from .models import Doctor,Patient,Drug
from .serializers import DoctorSerializer,PatientSerializer,DrugSerializer
class DoctorViewSet(viewsets.ModelViewSet):
    #ModelViewSet implement the CRUD using methods: list(),retrieve(),create(),...
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    #All http CRUD methods are implemented
class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    #we can customize the http methods allowed for this viewset using http_method_names
    http_method_names = ['get', 'post']