from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('sale_start', models.DateTimeField(blank=True, null=True, default=None)),
                ('sale_end', models.DateTimeField(blank=True, null=True, default=None)),
                ('photo', models.ImageField(blank=True, null=True, default=None, upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
                ('shopping_cart', models.ForeignKey(related_name='items', related_query_name='item', on_delete=django.db.models.deletion.CASCADE, to='store.ShoppingCart')),
            ],
        ),
    ]
