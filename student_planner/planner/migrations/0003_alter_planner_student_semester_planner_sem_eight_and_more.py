# Generated by Django 5.0.2 on 2024-03-20 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_advisor_user_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planner',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='planner.student'),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_five', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='class_five', to='planner.course')),
                ('class_four', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='class_four', to='planner.course')),
                ('class_one', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='class_one', to='planner.course')),
                ('class_six', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='class_six', to='planner.course')),
                ('class_three', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='class_three', to='planner.course')),
                ('class_two', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='class_two', to='planner.course')),
            ],
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_eight',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_eight', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_five',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_five', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_four',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_four', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_one',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_one', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_seven',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_seven', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_six',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_six', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_three',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_three', to='planner.semester'),
        ),
        migrations.AddField(
            model_name='planner',
            name='sem_two',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_two', to='planner.semester'),
        ),
    ]