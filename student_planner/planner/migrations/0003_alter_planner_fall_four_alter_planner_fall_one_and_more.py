# Generated by Django 5.0.2 on 2024-04-03 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_rename_sem_seven_planner_fall_four_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planner',
            name='fall_four',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_seven', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='fall_one',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_one', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='fall_three',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_five', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='fall_two',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_three', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='spring_four',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_eight', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='spring_one',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_two', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='spring_three',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_six', to='planner.semester'),
        ),
        migrations.AlterField(
            model_name='planner',
            name='spring_two',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_four', to='planner.semester'),
        ),
    ]
