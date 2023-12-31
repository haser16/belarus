# Generated by Django 3.2.12 on 2023-12-06 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_content')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='paragraphs')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='main.content')),
            ],
        ),
    ]
