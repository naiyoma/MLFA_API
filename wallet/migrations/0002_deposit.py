# Generated by Django 3.2.14 on 2022-07-17 23:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('deposit_amount', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='balance')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wallet.wallet')),
            ],
        ),
    ]
