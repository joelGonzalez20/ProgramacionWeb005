# Generated by Django 4.1.9 on 2023-05-21 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230512_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Cargo')),
                ('nombreCargo', models.CharField(max_length=50, verbose_name='Nombre de la Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut del Cliente')),
                ('dv', models.CharField(max_length=50, verbose_name='Digito Verificador')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('appaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno del cliente')),
                ('apmaterno', models.CharField(max_length=50, verbose_name='Apellido Materno del cliente')),
                ('email', models.CharField(max_length=50, verbose_name='Email del Cliente')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id compra')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('precioTotal', models.IntegerField(verbose_name='Precio Total de la compra')),
                ('fechaCompra', models.DateField(verbose_name='Fecha Compra')),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='detalle_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de la compra')),
                ('precioNeto', models.IntegerField(verbose_name='Precio neto de la compra')),
                ('descuento', models.IntegerField(verbose_name='Porcentaje de Descuento')),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('idPedido', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Pedido')),
                ('fechaEntrega', models.DateField(verbose_name='Fecha de Entrega')),
                ('direccionEntrega', models.CharField(max_length=50, verbose_name='Dirección de Entrega')),
                ('estadoEntrega', models.CharField(max_length=50, verbose_name='Estado de la Compra')),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
                ('idDetalleCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.detalle_compra')),
            ],
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descuentoProducto', models.IntegerField(verbose_name='Descuento del Producto')),
                ('FechaExpiracion', models.DateField(verbose_name='Fecha Expiración')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='vigente',
        ),
        migrations.AddField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='id de la Producto '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(default=1, max_length=50, verbose_name='Nombre de la Producto '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precioProducto',
            field=models.IntegerField(default=1, verbose_name='Precio de el Producto '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(verbose_name='Stock del Producto'),
        ),
        migrations.DeleteModel(
            name='TipoProducto',
        ),
        migrations.AddField(
            model_name='promociones',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
        migrations.AddField(
            model_name='detalle_compra',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
            preserve_default=False,
        ),
    ]