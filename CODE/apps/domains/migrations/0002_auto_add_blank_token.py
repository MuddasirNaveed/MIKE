from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='verification_token',
            field=models.CharField(max_length=64, unique=True, blank=True),
        ),
    ]
