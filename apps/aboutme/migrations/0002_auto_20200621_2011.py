# Generated by Django 3.0.6 on 2020-06-21 20:11

import apps.aboutme.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='attribute_Level',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='attribute_Name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree_Title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='institute_Name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='year_Gained',
            field=models.PositiveIntegerField(blank=True, default=2020, validators=[django.core.validators.MinValueValidator(2015), apps.aboutme.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_Name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_Title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='me',
            name='my_Introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='my_Level',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='me',
            name='my_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='skill_Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='skill_Level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Average', 'Average'), ('Skilled', 'Skilled'), ('Specialist', 'Specialist'), ('Expert', 'Expert')], default='Beginner', max_length=16),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='skill_Title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='skill_Type',
            field=models.CharField(blank=True, choices=[('Script or Programming Languages', 'Script or Programming Languages'), ('Other', 'Other')], default='Other', max_length=90),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='year_Started',
            field=models.PositiveIntegerField(blank=True, default=2020, validators=[django.core.validators.MinValueValidator(2015), apps.aboutme.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='work_Exp_Company',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='work_Exp_Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='work_Exp_Title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='year_Finished',
            field=models.PositiveIntegerField(blank=True, default=2020, validators=[django.core.validators.MinValueValidator(2015), apps.aboutme.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='year_Started',
            field=models.PositiveIntegerField(blank=True, default=2020, validators=[django.core.validators.MinValueValidator(2015), apps.aboutme.models.max_value_current_year]),
        ),
    ]
