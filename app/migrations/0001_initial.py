# Generated by Django 4.2.7 on 2023-11-16 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('codename', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'group_permission',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'rol',
            },
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_permissions',
            },
        ),
        migrations.AddIndex(
            model_name='permission',
            index=models.Index(fields=['name'], name='permission_name_fa4988_idx'),
        ),
        migrations.AddField(
            model_name='grouppermission',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.AddField(
            model_name='grouppermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.permission'),
        ),
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.rol'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='idx_username_search'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='idx_email_find'),
        ),
    ]
