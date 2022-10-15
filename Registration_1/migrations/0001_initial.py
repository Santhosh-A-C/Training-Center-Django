# Generated by Django 4.1.1 on 2022-10-06 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_ID', models.CharField(max_length=264, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_ID', models.CharField(max_length=264, unique=True)),
                ('course_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=264, unique=True)),
                ('student_name', models.CharField(max_length=264)),
                ('qualification', models.CharField(max_length=264)),
                ('branch', models.CharField(max_length=264)),
                ('year', models.CharField(max_length=264)),
                ('experience', models.CharField(max_length=264)),
                ('url', models.URLField()),
                ('batch_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration_1.batch')),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration_1.course')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration_1.course'),
        ),
    ]
