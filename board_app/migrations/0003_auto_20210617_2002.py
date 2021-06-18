# Generated by Django 3.2.4 on 2021-06-17 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0002_sub_board'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_board',
            old_name='sub_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='sub_board',
            old_name='sub_created_date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='sub_board',
            name='board_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board_app.board'),
        ),
    ]
