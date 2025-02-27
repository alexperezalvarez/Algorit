# Generated by Django 5.1.6 on 2025-02-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_client_alter_type_name_product_sale_detsale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detsale',
            options={'ordering': ['id'], 'verbose_name': 'Detalle de Venta', 'verbose_name_plural': 'Detalle de Ventas'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='names',
        ),
        migrations.RemoveField(
            model_name='client',
            name='surname',
        ),
        migrations.AddField(
            model_name='client',
            name='surnames',
            field=models.CharField(default=2, max_length=150, verbose_name='Apellidos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=10, unique=True, verbose_name='Dni'),
        ),
        migrations.AlterField(
            model_name='client',
            name='sexo',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='male', max_length=10, verbose_name='Sexo'),
        ),
        migrations.AlterModelTable(
            name='category',
            table=None,
        ),
        migrations.AlterModelTable(
            name='client',
            table=None,
        ),
        migrations.AlterModelTable(
            name='detsale',
            table=None,
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
        migrations.AlterModelTable(
            name='sale',
            table=None,
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
