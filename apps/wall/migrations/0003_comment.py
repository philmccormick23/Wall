# Generated by Django 2.1.1 on 2018-09-18 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='message_message', to='wall.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='message_user', to='wall.User')),
            ],
        ),
    ]
