# Generated by Django 5.0.2 on 2024-04-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('sname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sprinciple', models.CharField(max_length=50)),
                ('scontact', models.CharField(max_length=50)),
            ],
        ),
    ]
