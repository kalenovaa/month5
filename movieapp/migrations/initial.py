from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': 'director',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='desc')),
                ('duration', models.IntegerField(help_text='duration', verbose_name='duration')),
                ('director', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='movie_app.director', verbose_name='Режиссер')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.movie', verbose_name='movie')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'review',
            },
        ),
    ]