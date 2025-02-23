# Generated by Django 4.0.6 on 2022-08-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_rename_address_usermodel_useraddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='privacyPolicyQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_policyUseChoice', models.CharField(max_length=50)),
                ('userLocate', models.BooleanField()),
                ('userCreateAccount', models.BooleanField()),
                ('websiteOffer', models.BooleanField()),
                ('other_personalInfo', models.CharField(max_length=50)),
                ('collectPersonalInfo', models.BooleanField()),
                ('marketingCommnuication', models.BooleanField()),
                ('acceptPayments', models.BooleanField()),
                ('containAds', models.BooleanField()),
                ('upPostContent', models.BooleanField()),
                ('disclosePerInfo', models.BooleanField()),
                ('discloseCollectInfo', models.BooleanField()),
                ('secureMeausre', models.BooleanField()),
                ('provideService', models.BooleanField()),
                ('provideEmailAdd', models.CharField(max_length=50)),
                ('legalName', models.CharField(max_length=200)),
                ('tradeNameBusiness', models.BooleanField()),
                ('companyEmail', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('compAddressLine', models.CharField(max_length=200)),
                ('cityTown', models.CharField(max_length=150)),
                ('zipCode', models.IntegerField()),
                ('versionDate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
