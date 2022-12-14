from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', 'review2'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='rating'),
        ),
    ]