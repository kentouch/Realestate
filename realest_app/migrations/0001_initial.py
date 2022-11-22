# Generated by Django 4.1.1 on 2022-11-09 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.IntegerField(choices=[(0, 'available'), (1, 'sold'), (2, 'taken')], default=0)),
                ('car_name', models.CharField(max_length=100)),
                ('version', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('image_car', models.ImageField(default='car.png', upload_to='Images/carImg/')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.IntegerField(choices=[(0, 'available'), (1, 'sold'), (2, 'taken')], default=0)),
                ('location', models.CharField(max_length=100)),
                ('NumbOfBeds', models.IntegerField()),
                ('NumberOfBathroom', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('image_house', models.ImageField(default='house.png', upload_to='Images/houseImg/')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='realest_app.category')),
                ('classification', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='realest_app.classification')),
            ],
            options={
                'ordering': ['-uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.IntegerField(choices=[(0, 'available'), (1, 'sold'), (2, 'taken')], default=0)),
                ('location', models.CharField(max_length=100)),
                ('numberOfSqrtMeter', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image_land', models.ImageField(default='land.png', upload_to='Images/landImg/')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='Property_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='LandGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='Images/')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LandPhoto', to='realest_app.land')),
            ],
        ),
        migrations.AddField(
            model_name='land',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='realest_app.property_status'),
        ),
        migrations.CreateModel(
            name='HouseGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='Images/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HousePhoto', to='realest_app.house')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='realest_app.property_status'),
        ),
        migrations.CreateModel(
            name='CarGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='Images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CarPhoto', to='realest_app.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realest_app.property_status'),
        ),
    ]