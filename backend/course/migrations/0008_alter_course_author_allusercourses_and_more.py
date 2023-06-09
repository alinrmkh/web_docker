# Generated by Django 4.1.5 on 2023-03-13 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AllUserCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='courses',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.allusercourses'),
        ),
    ]
