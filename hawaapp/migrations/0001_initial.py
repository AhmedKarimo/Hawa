# Generated by Django 3.2.6 on 2022-02-28 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_question', models.CharField(max_length=200)),
                ('ex_result', models.CharField(max_length=200)),
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('us_firstname', models.CharField(max_length=50)),
                ('us_lastname', models.CharField(max_length=50)),
                ('us_email', models.CharField(max_length=50)),
                ('us_birthdate', models.DateField(max_length=50)),
                ('us_rathe', models.CharField(max_length=50)),
                ('per_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.perioddate')),
                ('pho_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hawaapp.phone', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_question', models.CharField(max_length=200)),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.user')),
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
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.user')),
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
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='OprateExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ope_ex_date', models.DateField()),
                ('ope_ex_answer', models.DateField()),
                ('ex_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.examination')),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='examination',
            name='us_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.user'),
        ),
        migrations.CreateModel(
            name='Diagnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diag_date', models.DateField()),
                ('diag_diagnosis', models.CharField(max_length=50)),
                ('pred_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.prediction')),
                ('us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hawaapp.user')),
            ],
        ),
    ]
