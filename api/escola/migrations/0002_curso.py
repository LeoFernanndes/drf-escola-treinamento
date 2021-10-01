# Generated by Django 3.2.6 on 2021-09-08 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nivel', models.CharField(max_length=255)),
                ('preco', models.FloatField()),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.escola')),
            ],
        ),
    ]