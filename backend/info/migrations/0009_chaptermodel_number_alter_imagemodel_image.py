# Generated by Django 4.0.6 on 2023-01-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_remove_pagemodel_under_construction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaptermodel',
            name='number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
