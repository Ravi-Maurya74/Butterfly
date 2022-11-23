# Generated by Django 4.1.2 on 2022-10-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiuser',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to='api.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='api.apiuser'),
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
