# Generated by Django 4.2.13 on 2024-09-30 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ToDoList", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="categories",),
        migrations.AddField(
            model_name="task",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ToDoList.category",
            ),
        ),
    ]
