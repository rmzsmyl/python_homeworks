# Generated by Django 4.2.7 on 2023-11-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('decs', models.TextField()),
                ('priority', models.IntegerField()),
                ('created_at', models.IntegerField(blank=True)),
            ],
        ),
    ]