# Generated by Django 3.1.7 on 2022-10-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('tags', models.TextField()),
                ('pic', models.FileField(upload_to='pic/%y/')),
            ],
        ),
    ]
