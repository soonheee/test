# Generated by Django 3.2.5 on 2021-08-04 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=60)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('reviews', models.PositiveIntegerField(default=0)),
                ('tmp_flag', models.BooleanField()),
                ('d_date', models.DateField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviewapp.review')),
                ('user_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviewapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviewapp.user'),
        ),
    ]