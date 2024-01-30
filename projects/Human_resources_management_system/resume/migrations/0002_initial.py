# Generated by Django 4.2 on 2024-01-18 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experinece',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='resume.resume'),
        ),
        migrations.AddField(
            model_name='degree',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degrees', to='resume.resume'),
        ),
    ]
