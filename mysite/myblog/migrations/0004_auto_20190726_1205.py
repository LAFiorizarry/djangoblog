# Generated by Django 2.1.1 on 2019-07-26 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20190725_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myblog.Post'),
            preserve_default=False,
        ),
    ]
