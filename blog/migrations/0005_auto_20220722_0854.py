# Generated by Django 3.2.13 on 2022-07-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_comment_form_commentform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentForm',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]