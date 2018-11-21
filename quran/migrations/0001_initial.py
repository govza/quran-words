# Generated by Django 2.1 on 2018-11-21 13:57

from django.db import migrations, models
import django.db.models.deletion
import quran.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayah',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recitation',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('segments', models.TextField()),
                ('audio', models.FileField(
                    upload_to=quran.models.audio_directory_path)),
                ('ayah', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='recitations', to='quran.Ayah')),
            ],
        ),
        migrations.CreateModel(
            name='Reciter',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quality', models.CharField(
                    blank=True,
                    help_text='This field contain a bitrate of audio file',
                    max_length=10)),
                ('style', models.CharField(
                    blank=True,
                    help_text='This filed describe style \
                    or speed of reading of the reciter',
                    max_length=20)),
                ('slug', models.SlugField(
                    help_text="This field is short label for name, \
                    containing only letters and hyphens. \
                    It's filled automatically during saving.")),
            ],
        ),
        migrations.CreateModel(
            name='Surah',
            fields=[
                ('number', models.PositiveIntegerField(
                    primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('total_ayahs', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='recitation',
            name='reciter',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recitations', to='quran.Reciter'),
        ),
        migrations.AddField(
            model_name='ayah',
            name='surah',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='ayahs', to='quran.Surah'),
        ),
    ]
