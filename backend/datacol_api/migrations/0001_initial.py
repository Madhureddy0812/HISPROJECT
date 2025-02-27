# Generated by Django 4.2.11 on 2024-09-06 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DC_Cases',
            fields=[
                ('CASE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CASE_NUM', models.CharField(blank=True, max_length=6, null=True)),
                ('APP_ID', models.CharField(max_length=6)),
                ('PLAN_ID', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Dc_case',
                'verbose_name_plural': 'Dc_cases',
            },
        ),
        migrations.CreateModel(
            name='DC_Income',
            fields=[
                ('INCOME_ID', models.AutoField(primary_key=True, serialize=False)),
                ('EMP_INCOME', models.CharField(max_length=6)),
                ('PROPERTY_INCOME', models.CharField(max_length=6)),
                ('CASE_NUM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacol_api.dc_cases')),
            ],
            options={
                'verbose_name': 'Dc_income',
                'verbose_name_plural': 'Dc_income',
            },
        ),
        migrations.CreateModel(
            name='DC_Education',
            fields=[
                ('EDU_ID', models.AutoField(primary_key=True, serialize=False)),
                ('HIGHEST_QUALIFICATION', models.CharField(max_length=255)),
                ('GRADUATION_YEAR', models.IntegerField()),
                ('CASE_NUM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacol_api.dc_cases')),
            ],
            options={
                'verbose_name': 'Dc_education',
                'verbose_name_plural': 'Dc_education',
            },
        ),
        migrations.CreateModel(
            name='DC_Childrens',
            fields=[
                ('CHILDREN_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CHILDREN_DOB', models.IntegerField()),
                ('CHILDREN_SSN', models.IntegerField()),
                ('CASE_NUM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacol_api.dc_cases')),
            ],
            options={
                'verbose_name': 'Dc_children',
                'verbose_name_plural': 'Dc_childrens',
            },
        ),
    ]
