# Generated by Django 3.2.4 on 2021-08-02 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='article/')),
                ('content', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
