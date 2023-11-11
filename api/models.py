from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Sponsor(models.Model):
    class TypeChoice(models.TextChoices):
        LEGAL = 'legal','yuridik'
        PHYSICAL='physical','jismoniy'
    class TransactionType(models.TextChoices):
        CASH ='cash','yuridik'
        CARD='card','karta'
    class StatusChoice(models.TextChoices):
        MODERATION="Moderation","Modernizatsiya"
        NEW="New","yangi"
        APPROVED="Approved","tasdiqlangan"
        CANCELLED="Cancelled","Bekor Qilingan "

    full_name=models.CharField(max_length=100,verbose_name="To'liq ism")
    organization_name=models.CharField(max_length=100,
                                       verbose_name="tashkilot nomi",
                                       null=True,
                                       blank=True)
    phone_number=models.CharField(max_length=50,validators=[RegexValidator(r'^\+998\d{9}$')],verbose_name="telefon raqami")
    amount=models.PositiveIntegerField(verbose_name="homiylik summasi")
    created_at=models.DateField(auto_now_add=True,verbose_name="ariza sanasi")
    status=models.CharField(max_length=50,
                            choices=StatusChoice.choices,
                            default=StatusChoice.NEW,verbose_name="holati homiy")
    type =models.CharField(max_length=50,
                           choices=TypeChoice.choices,verbose_name="shaxs turi" )
    transaction_type=models.CharField(max_length=50,
                                      verbose_name="to`lov turi",
                                      choices=TransactionType.choices,
                                      default=TransactionType.CARD)
    def __str__(self):
        return f"{self.full_name}-{self.phone_number}"


class University(models.Model):
    name=models.CharField(max_length=200,verbose_name="universitetit nomi")

    def __str__(self):
        return self.name


class Student(models.Model):
    class DegreeChoice(models.TextChoices):
        BACHELOR = 'bachelor', 'bakalvr'
        MASTER = 'master', 'magistr'

    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    contract=models.PositiveIntegerField(verbose_name="kontrakt summasi")
    degree=models.CharField(max_length=50,choices=DegreeChoice.choices,
                            default=DegreeChoice.BACHELOR,
                            verbose_name="Darajasi")
    university=models.ForeignKey(University,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    def __str__(self):
        return self.full_name



class StudentSponsor(models.Model):
    sponsor=models.ForeignKey(Sponsor,
                              on_delete=models.PROTECT,
                              verbose_name="sponsor",
                              related_name="student_sponsors")
    student=models.ForeignKey(Student,
                              on_delete=models.PROTECT,
                              verbose_name="stundent",
                              related_name="student_sponsors")
    amount=models.PositiveIntegerField(verbose_name="ajratilgan summa")


    def __str__(self):
        return f"{self.sponsor}-{self.student}"
















