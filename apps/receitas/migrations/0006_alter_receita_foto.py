# Generated by Django 3.2.4 on 2021-07-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_receita_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]
