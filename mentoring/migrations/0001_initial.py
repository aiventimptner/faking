# Generated by Django 3.0.8 on 2020-07-30 16:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('color', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Es sind nur Farben als Hexadezimal-Code erlaubt.', regex='[0-9A-F]{6}')])),
                ('ask_for_phone', models.BooleanField(default=False)),
                ('ask_for_program', models.BooleanField(default=True)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message="Es sind nur Adressen mit der Domain 'st.ovgu.de' erlaubt.", regex='(\\w+\\.)?\\w+@st.ovgu.de')])),
                ('phone', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Die Mobilnummer ist nur im Format '0123/456789' erlaubt.", regex='01\\d{2}\\/\\d{6,7}')])),
                ('qualification', models.BooleanField(default=True)),
                ('supervision', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.Faculty')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mentoring.Program')),
            ],
        ),
    ]
