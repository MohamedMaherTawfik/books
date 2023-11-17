# Generated by Django 4.2.7 on 2023-11-17 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_alter_book_name_alter_book_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Review', to='book.review'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Book_Author', to='book.author'),
        ),
    ]
