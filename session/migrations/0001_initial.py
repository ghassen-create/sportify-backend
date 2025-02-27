# Generated by Django 4.1.7 on 2023-03-25 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('score', models.CharField(max_length=10)),
                ('infrastructure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.infrastructure')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2_set', to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.infrastructure')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.sport')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jersey_number', models.PositiveSmallIntegerField()),
                ('role', models.CharField(choices=[('GK', 'Gardien de but'), ('DF', 'Défenseur'), ('MD', 'Milieu de terrain'), ('FW', 'Attaquant')], max_length=2)),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('fouls', models.PositiveSmallIntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(through='session.Participation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1_set', to='team.team'),
        ),
    ]
