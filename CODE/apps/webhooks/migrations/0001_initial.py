from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint_url', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='webhook', to='applications.application')),
            ],
        ),
    ]
