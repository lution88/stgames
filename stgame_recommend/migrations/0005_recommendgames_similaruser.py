# Generated by Django 4.0.1 on 2022-02-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgame_recommend', '0004_alter_favoritegames_game_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_game', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'recommendsgames',
            },
        ),
        migrations.CreateModel(
            name='SimilarUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sim_user', models.CharField(default='', max_length=50)),
                ('sim_game_list', models.TextField(default='')),
            ],
            options={
                'db_table': 'similar_users',
            },
        ),
    ]