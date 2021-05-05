# Generated by Django 3.1.3 on 2021-04-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='Duration of the quiz in minutes')),
                ('required_score_to_pass', models.IntegerField(help_text='minimum score to pass in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'meduim'), ('hard', 'hard')], max_length=6)),
                ('quiz_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
