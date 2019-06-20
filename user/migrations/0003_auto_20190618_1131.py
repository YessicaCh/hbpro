# Generated by Django 2.2 on 2019-06-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190618_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hbprouser',
            name='e_mail',
            field=models.EmailField(blank='False', default='example@gmail', max_length=50),
        ),
        migrations.AlterField(
            model_name='hbprouser',
            name='github',
            field=models.URLField(default='https://github.com/example', max_length=50),
        ),
        migrations.AlterField(
            model_name='hbprouser',
            name='number_phone',
            field=models.IntegerField(blank='False', default=999999999, null='True'),
        ),
    ]
