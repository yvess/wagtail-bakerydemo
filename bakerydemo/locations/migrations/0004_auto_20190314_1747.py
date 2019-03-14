# Generated by Django 2.1.7 on 2019-03-14 17:47

from django.db import migrations, models
import django.db.models.deletion
import wagtail_i18n.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0001_initial'),
        ('locations', '0003_auto_20170329_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationpage',
            name='language',
            field=models.ForeignKey(default=wagtail_i18n.models.Language.default, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Language'),
        ),
        migrations.AddField(
            model_name='locationpage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='locationsindexpage',
            name='language',
            field=models.ForeignKey(default=wagtail_i18n.models.Language.default, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Language'),
        ),
        migrations.AddField(
            model_name='locationsindexpage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='locationoperatinghours',
            name='closed',
            field=models.BooleanField(blank=True, help_text='Tick if location is closed on this day', verbose_name='Closed?'),
        ),
    ]
