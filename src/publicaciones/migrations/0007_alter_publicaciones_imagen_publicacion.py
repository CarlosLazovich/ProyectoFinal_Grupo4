# Generated by Django 4.2.3 on 2023-07-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0006_alter_publicaciones_imagen_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='imagen_publicacion',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_publicacion'),
        ),
    ]
