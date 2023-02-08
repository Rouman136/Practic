
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20190125_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('price', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='products/%Y/%m/%d/')),
                ('published_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='categories.Category')),
            ],
        ),
    ]
