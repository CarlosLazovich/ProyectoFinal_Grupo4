# Generated by Django 4.2.3 on 2023-07-29 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('asunto', models.CharField(max_length=255)),
                ('mensaje', models.TextField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]