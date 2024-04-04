# Generated by Django 5.0.2 on 2024-04-04 01:22

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'planner_course',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4)),
                ('num_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4)),
                ('num_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=100)),
                ('long_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('STUDENT', 'Student'), ('ADVISOR', 'Advisor')], default='STUDENT', max_length=7)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('registered', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eagle_id', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('class_year', models.CharField(max_length=4)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='advisor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_hours', models.PositiveIntegerField(default=0)),
                ('courses', models.ManyToManyField(to='planner.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('eagle_id', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('class_year', models.CharField(max_length=4)),
                ('end_semester', models.CharField(choices=[('Spring', 'Spring'), ('Fall', 'Fall')], default='Spring', max_length=6)),
                ('college', models.CharField(choices=[('MCAS', 'Morrissey College of Arts and Sciences'), ('CSOM', 'Carroll School of Management'), ('CSON', 'William F. Connell School of Nursing'), ('LYNCH', 'Carolyn A. and Peter S. Lynch School of Education and Human Development')], max_length=5)),
                ('advisor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='planner.advisor')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('major_one', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='major_one', to='planner.subject')),
                ('major_two', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='major_two', to='planner.subject')),
                ('minor_one', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='minor_one', to='planner.subject')),
                ('minor_two', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='minor_two', to='planner.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fall_four', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_seven', to='planner.semester')),
                ('fall_one', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_one', to='planner.semester')),
                ('fall_three', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_five', to='planner.semester')),
                ('fall_two', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_three', to='planner.semester')),
                ('spring_four', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_eight', to='planner.semester')),
                ('spring_one', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_two', to='planner.semester')),
                ('spring_three', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_six', to='planner.semester')),
                ('spring_two', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planner_sem_four', to='planner.semester')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='planner.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.subject'),
        ),
        migrations.AddConstraint(
            model_name='semester',
            constraint=models.CheckConstraint(check=models.Q(('credit_hours__lte', 21)), name='credit_hours_limit'),
        ),
    ]
