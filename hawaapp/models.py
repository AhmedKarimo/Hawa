from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields import IntegerField

# Create your models here.


class Phone(models.Model):

    pho_number = models.IntegerField()


class PeriodDate(models.Model):
    per_date = models.DateField()


class User(models.Model):
    pho_id = models.OneToOneField(
        Phone, on_delete=models.CASCADE, unique=True, null=True)
    per_date = models.ForeignKey(PeriodDate, on_delete=models.CASCADE)

    us_firstname = models.CharField(max_length=50)
    us_lastname = models.CharField(max_length=50)
    us_email = models.CharField(max_length=50)
    us_birthdate = models.DateField(max_length=50)
    us_rathe = models.CharField(max_length=50)


class Examination(models.Model):
    us_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ex_question = models.CharField(max_length=200)
    ex_result = models.CharField(max_length=200)


class OprateExamination(models.Model):
    us_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ex_id = models.ForeignKey(Examination, on_delete=models.CASCADE)

    ope_ex_date = models.DateField()
    ope_ex_answer = models.DateField()


class Prediction(models.Model):
    us_id = models.ForeignKey(User, on_delete=models.CASCADE)

    pred_feature1 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature2 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature3 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature4 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature5 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature6 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature7 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature8 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature9 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature10 = models.DecimalField(max_digits=20, decimal_places=10)
    pred_feature11 = models.DecimalField(max_digits=20, decimal_places=10)


class Diagnos(models.Model):
    us_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pred_id = models.ForeignKey(Prediction, on_delete=models.CASCADE)

    diag_date = models.DateField()
    diag_diagnosis = models.CharField(max_length=50)


class RiskCalculator(models.Model):
    us_id = models.ForeignKey(User, on_delete=models.CASCADE)

    risk_question = models.CharField(max_length=200)


class OprateRisk(models.Model):
    us_id = models.ForeignKey(User, on_delete=models.CASCADE)
    risk_id = models.ForeignKey(RiskCalculator, on_delete=models.CASCADE)

    ope_risk_date = models.DateField()
    ope_risk_answer = models.DecimalField(max_digits=20, decimal_places=10)
    ope_risk_result = models.DecimalField(max_digits=20, decimal_places=10)
