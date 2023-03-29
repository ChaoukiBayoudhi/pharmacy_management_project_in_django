from django.db import models

# Create your models here.
class DoctorSpeciality(models.TextChoices):
    CARDIOLOGIST=('Cardiologist','Cardiologist speciality')
    DERMATOLOGIST=('Dermatologist','Dermatologist speciality')
    # GASTROENTEROLOGIST='Gastroenterologist'
    # NEUROLOGIST='Neurologist'
    # ONCOLOGIST='Oncologist'
    # ORTHOPEDIST='Orthopedist'
    # PEDIATRICIAN='Pediatrician'
    # PSYCHIATRIST='Psychiatrist'
    # UROLOGIST='Urologist'
    
class Address(models.Model):
    number=models.PositiveBigIntegerField(default=0)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalCode = models.PositiveIntegerField(default=1000,unique=True)
    country = models.CharField(max_length=100)
    class Meta:
        db_table = 'Address'
    def __str__(self):
        #return '(',',',self.number,',',self.street,')'
        return '(%s,%s,%s,%s,%s)'%(self.number,self.street,self.city,self.postalCode,self.country)
class Person(models.Model):
    id=models.BigAutoField(primary_key=True,default=0)
    firstName = models.CharField(max_length=100,default='')
    lastName = models.CharField(max_length=100,default='')
    birthDate = models.DateField(null=True,blank=True)
    class Meta:
        #The model Persion is abstract
        #It can't be used to create a table in the database
        abstract=True
    def __str__(self):
        return '(%s,%s,%s)'%(self.firstName,self.lastName,self.address)
class Doctor(Person):
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=20)
    #speciality=models.CharField(max_length=100,choices=[('Cardiologist','Cardiologist speciality'),('Dermatologist','Dermatologist speciality')],default='Cardiologist')
    speciality=models.CharField(max_length=100,choices=DoctorSpeciality.choices,default=DoctorSpeciality.CARDIOLOGIST)
    class Meta:
        db_table = 'Doctor'