# Generated migration for Hotel property_type field

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0002_user_history"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="property_type",
            field=models.CharField(
                choices=[("hotel", "Hotel"), ("hostel", "Hostel")],
                default="hotel",
                max_length=20,
            ),
        ),
    ]