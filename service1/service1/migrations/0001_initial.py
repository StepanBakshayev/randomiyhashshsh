# Generated by Django 2.1.4 on 2018-12-06 11:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart', models.ImageField(upload_to='chart/')),
                ('generated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('generated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('y=t*t+2/t', 'first'), ('y=sin(t)', 'second')], max_length=9)),
                ('interval', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('dt', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AddField(
            model_name='error',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service1.Function', unique=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service1.Function', unique=True),
        ),
    ]
