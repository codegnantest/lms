# Generated by Django 3.0.8 on 2020-08-07 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0009_auto_20200807_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestatus',
            name='completed_lessons',
            field=models.ManyToManyField(blank=True, null=True, related_name='completed_lessons', to='lms.Lesson'),
        ),
        migrations.AlterField(
            model_name='coursestatus',
            name='current_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_lesson', to='lms.Lesson'),
        ),
    ]
