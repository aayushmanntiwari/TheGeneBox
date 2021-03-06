# Generated by Django 3.2.3 on 2021-05-14 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=225)),
                ('book_genre', models.CharField(blank=True, choices=[('Action and Adventure.', 'Action and Adventure.'), ('Classics', 'Classics'), ('Comic Book', 'Comic Book'), ('Detective and Mystery', 'Detective and Mystery'), ('Fantasy', 'Fantasy'), ('Historical Fiction', 'Historical Fiction'), ('Horror', 'Horror'), ('Literary Fiction', 'Literary Fiction'), ('others', 'others')], max_length=225, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.authors')),
            ],
        ),
    ]
