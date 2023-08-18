# Generated by Django 4.2.4 on 2023-08-19 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import referrals.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('invite_code', models.CharField(default=referrals.services.generate_invite_code, editable=False, max_length=6, unique=True)),
                ('referrer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='referrals', to='referrals.profile')),
            ],
        ),
    ]
