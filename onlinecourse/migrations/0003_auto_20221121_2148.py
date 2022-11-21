# Generated by Django 3.1.3 on 2022-11-21 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221121_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question_id',
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
    ]
