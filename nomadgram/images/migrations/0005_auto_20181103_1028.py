# Generated by Django 2.0.8 on 2018-11-03 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20181102_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]