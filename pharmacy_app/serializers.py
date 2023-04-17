#We implements Serializer classes for each model using seializers.ModelSerializer
#the package serializers is imported from rest_framework
#define DoctorSerializer class and inherit from ModelSerializer
from rest_framework import serializers
from .models import Doctor,Patient,Drug
class DoctorSerializer(serializers.ModelSerializer):
    #define Meta class and inherit from ModelSerializer.Meta
    class Meta:
        #define model attribute and set it to Doctor model
        #the model to be serialized
        model = Doctor
        #define fields attribute and set it to all fields of Doctor model
        #the fields to be serialized
        fields = '__all__' #all fields
        #fields = ('firstName','lastName','email','phone','speciality') #specific fields
#define PatientSerializer class and inherit from ModelSerializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

#define DrugSerializer class and inherit from ModelSerializer
class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'