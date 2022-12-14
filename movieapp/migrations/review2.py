from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', 'review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie', verbose_name='Фильм'),
        ),
    ]