# Generated by Django 3.2.12 on 2022-09-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tws', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slot_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('slotname', models.CharField(max_length=30)),
                ('Arrivalcity', models.CharField(max_length=30)),
                ('Destination', models.CharField(max_length=30)),
                ('Days_of_Trip', models.IntegerField()),
                ('Current_Number_Members', models.IntegerField()),
                ('Number_of_Members', models.IntegerField()),
                ('slot_id', models.IntegerField()),
                ('Minimum_age_Members', models.IntegerField()),
                ('Maximum_age_Members', models.IntegerField()),
                ('Total_Male', models.IntegerField()),
                ('Total_Female', models.IntegerField()),
                ('Starting_Date', models.CharField(max_length=10)),
                ('Returning_Date', models.CharField(max_length=10)),
                ('Current_Number_Male', models.IntegerField()),
                ('Current_Number_Female', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_with_slotdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('slot_id', models.IntegerField()),
                ('slotname', models.CharField(max_length=20)),
            ],
        ),
    ]
