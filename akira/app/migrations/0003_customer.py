# Generated by Django 4.2.5 on 2023-09-19 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Bahawalpur', 'Bahawalpur'), ('Faisalabad', 'Faisalabad'), ('Gujranwala', 'Gujranwala'), ('Lahore', 'Lahore'), ('Mianwali', 'Mianwali'), ('Multan', 'Multan'), ('Rawalpindi', 'Rawalpindi'), ('Sahiwal', 'Sahiwal'), ('Sargodha', 'Sargodha')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
