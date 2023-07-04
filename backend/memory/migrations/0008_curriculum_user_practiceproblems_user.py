# Generated by Django 4.0.3 on 2023-03-18 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memory', '0007_alter_curriculum_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curriculums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='practiceproblems',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PracticeProblems', to=settings.AUTH_USER_MODEL),
        ),
    ]
