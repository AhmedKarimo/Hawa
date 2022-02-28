from email.policy import default
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from platformdirs import user_runtime_path

# Create your models here.


class Phone(models.Model):

    pho_number = models.IntegerField()


class PeriodDate(models.Model):
    per_date = models.DateField()


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, firstname, lastname, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        return self.create_user(email, firstname, lastname, password, **other_fields)

    def create_user(self, email, firstname, lastname,  password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname,
                          lastname=lastname, **other_fields)
        user.set_password(password)
        user.save()

        return user


class HawaUser(AbstractBaseUser, PermissionsMixin):
    phone = models.OneToOneField(
        Phone, on_delete=models.CASCADE, unique=True, null=True)
    per_date = models.OneToOneField(
        PeriodDate, on_delete=models.CASCADE, null=True)

    firstname = models.CharField(max_length=500, blank=True)
    lastname = models.CharField(max_length=500, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    birthdate = models.DateField(max_length=500, null=True)
    rathe = models.CharField(max_length=500)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']


class Examination(models.Model):
    us_id = models.ForeignKey(HawaUser, on_delete=models.CASCADE)
    ex_question = models.CharField(max_length=200)
    ex_result = models.CharField(max_length=200)


class OprateExamination(models.Model):
    us_id = models.ForeignKey(HawaUser, on_delete=models.CASCADE)
    ex_id = models.ForeignKey(Examination, on_delete=models.CASCADE)

    ope_ex_date = models.DateField()
    ope_ex_answer = models.DateField()


class Prediction(models.Model):
    us_id = models.ForeignKey(HawaUser, on_delete=models.CASCADE)

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
    us_id = models.ForeignKey(HawaUser, on_delete=models.CASCADE)
    pred_id = models.ForeignKey(Prediction, on_delete=models.CASCADE)

    diag_date = models.DateField()
    diag_diagnosis = models.CharField(max_length=500)


class RiskCalculator(models.Model):
    us_id = models.ForeignKey(HawaUser, on_delete=models.CASCADE)

    risk_question = models.CharField(max_length=200)


class OprateRisk(models.Model):
    us_id = models.ForeignKey(HawaUser, on_delete=models.CASCADE)
    risk_id = models.ForeignKey(RiskCalculator, on_delete=models.CASCADE)

    ope_risk_date = models.DateField()
    ope_risk_answer = models.DecimalField(max_digits=20, decimal_places=10)
    ope_risk_result = models.DecimalField(max_digits=20, decimal_places=10)
