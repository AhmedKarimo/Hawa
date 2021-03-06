# Generated by Django 3.2.6 on 2022-02-28 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HawaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('firstname', models.CharField(blank=True, max_length=500)),
                ('lastname', models.CharField(blank=True, max_length=500)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('birthdate', models.DateField(max_length=500)),
                ('rathe', models.CharField(max_length=500)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_question', models.CharField(max_length=200)),
                ('ex_result', models.CharField(max_length=200)),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pho_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_question', models.CharField(max_length=200)),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pred_feature1', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature2', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature3', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature4', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature5', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature6', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature7', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature8', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature9', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature10', models.DecimalField(decimal_places=10, max_digits=20)),
                ('pred_feature11', models.DecimalField(decimal_places=10, max_digits=20)),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OprateRisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ope_risk_date', models.DateField()),
                ('ope_risk_answer', models.DecimalField(decimal_places=10, max_digits=20)),
                ('ope_risk_result', models.DecimalField(decimal_places=10, max_digits=20)),
                ('risk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.riskcalculator')),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OprateExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ope_ex_date', models.DateField()),
                ('ope_ex_answer', models.DateField()),
                ('ex_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.examination')),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diag_date', models.DateField()),
                ('diag_diagnosis', models.CharField(max_length=500)),
                ('pred_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.prediction')),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hawauser',
            name='per_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hawaapp.perioddate'),
        ),
        migrations.AddField(
            model_name='hawauser',
            name='phone',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hawaapp.phone'),
        ),
        migrations.AddField(
            model_name='hawauser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
