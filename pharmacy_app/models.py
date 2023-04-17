from django.db import models

# Create your models here.
class DoctorSpecialty(models.TextChoices):
    CARDIOLOGIST=('Cardiologist','Cardiologist specialty')
    DERMATOLOGIST=('Dermatologist','Dermatologist specialty')
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
    #this column is the primary key and it's optional because django already create it
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
    speciality=models.CharField(max_length=100,choices=DoctorSpecialty.choices,default=DoctorSpecialty.CARDIOLOGIST)
    class Meta:
        db_table = 'doctor'

class Patient(Person):
    email=models.EmailField(max_length=254,unique=True,default='')
    phone=models.CharField(max_length=20,null=True,blank=True)
    class Meta:
        db_table = 'patient'
        #Patients are ordered by lastName and email in descending order
        ordering=['-lastName','-email']

class Drug(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    manufacturingDate=models.DateField(null=True,blank=True)
    expirationDate=models.DateField(null=True,blank=True)
    stock=models.PositiveIntegerField(default=0)
    description=models.TextField(null=True,blank=True)
    photo=models.ImageField(upload_to='photos',null=True,blank=True)
    class Meta:
        db_table = 'drug'

# class Prescription(models.Model):
#     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
#     patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
#     drug=models.ForeignKey(Drug,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=0)
#     class Meta:
#         db_table = 'Prescription'