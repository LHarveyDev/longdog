# Generated by Django 3.2.25 on 2024-05-02 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0002_auto_20240428_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=90)),
                ('review', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reviewed_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
