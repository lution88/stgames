# Generated by Django 4.0.1 on 2022-01-28 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_num', models.BigAutoField(primary_key=True, serialize=False)),
                ('game', models.CharField(max_length=256)),
                ('playtime', models.CharField(max_length=256)),
                ('user_id', models.ForeignKey(db_column='user_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
            ],
            options={
                'db_table': 'games',
            },
        ),
    ]
