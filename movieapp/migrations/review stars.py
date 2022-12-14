from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='movies', to='movie_app.director', verbose_name='director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=5, verbose_name='rating'),
        ),
    ]