from datetime import timedelta
from django.utils import timezone
from django.db import migrations

def create_sample_product_data(apps, schema_editor):
    Product = apps.get_model('store', 'Product')
    Product(
        id=1, name='Mineral Water Strawberry', description='Natural-flavored strawberry with an anti-oxidant kick.', price=1.00,
        photo='products/mineralwater-strawberry.jpg',
    ).save()
    Product(
        id=2, name='Mineral Water Raspberry', description='Flavoured with raspberry, loaded with anti-oxidants.', price=2.00,
        photo='products/mineralwater-raspberry.jpg',
    ).save()
    Product(
        id=3, name='Vitamin A 10,000 IU (125 caplets)', price=3.00,
        description='Vitamin A is essential for normal and night vision, and helps maintain healthy skin and mucous membranes.',
        sale_start=timezone.now(),
        sale_end=timezone.now() + timedelta(days=10),
        photo='products/vitamin-a.jpg',
    ).save()
    Product(
        id=4, name='Vitamin B-Complex (100 caplets)', price=3.00,
        description='Contains a combination of essential B vitamins that help convert food to energy.',
        sale_start=timezone.now(),
        sale_end=timezone.now() + timedelta(days=10),
        photo='products/vitamin-bcomplex.jpg',
    ).save()

class Migration(migrations.Migration):
    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_product_data),
    ]
