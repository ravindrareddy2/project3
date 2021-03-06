# Generated by Django 2.0.3 on 2019-02-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, max_digits=4)),
                ('large', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('large', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RenameModel(
            old_name='Type_of_pizza',
            new_name='Category',
        ),
        migrations.RemoveField(
            model_name='dinner_platters',
            name='name',
        ),
        migrations.RemoveField(
            model_name='salads',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='name',
        ),
        migrations.RemoveField(
            model_name='toppings',
            name='name',
        ),
        migrations.AlterField(
            model_name='pasta',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='regular_pizza',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='sicilian_pizza',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Dinner_platters',
        ),
        migrations.DeleteModel(
            name='Salads',
        ),
        migrations.DeleteModel(
            name='Subs',
        ),
        migrations.DeleteModel(
            name='Toppings',
        ),
    ]
