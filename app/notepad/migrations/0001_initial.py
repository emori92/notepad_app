# Generated by Django 2.2 on 2020-06-26 14:10

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
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='タイトル')),
                ('describe', models.TextField(blank=True, max_length=128, null=True, verbose_name='説明')),
                ('public', models.BooleanField(default=0, verbose_name='公開範囲')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(max_length=128, verbose_name='問題')),
                ('hint', models.TextField(blank=True, max_length=64, null=True, verbose_name='ヒント')),
                ('answer', models.TextField(max_length=256, verbose_name='答え')),
                ('review', models.BooleanField(default=0, verbose_name='復習')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notepad.Note', verbose_name='ノート')),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]