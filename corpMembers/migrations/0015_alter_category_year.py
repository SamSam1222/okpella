# Generated by Django 4.2.4 on 2024-02-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpMembers', '0014_alter_category_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='year',
            field=models.IntegerField(choices=[(2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029'), (2030, '2030')], max_length=100),
        ),
    ]