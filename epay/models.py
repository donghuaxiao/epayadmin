from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class PaymentOrder(models.Model):
#     paymentOrderId = models.CharField(name="PAYMENTORDERID", max_length=100)
#     orderId= models.CharField(name="ORDERID",max_length=100)
#     amount = models.IntegerField(name="AMOUNT")
#     status = models.IntegerField(name='STATUS')
#     orderTime=models.CharField(max_length=14)


class Channel(models.Model):
    channelId = models.CharField(max_length=30, db_column='channel_id', primary_key=True)
    channelName = models.CharField(max_length=50, db_column='title')
    description = models.CharField(max_length=250, db_column='description')
    password = models.CharField(max_length=100, db_column='PSWD')
    encryptAlgorithm = models.CharField(max_length=30, db_column='encrypt_algorithm')
    viewFlag = models.IntegerField(db_column='view_flag')
    status = models.IntegerField(db_column='status')
    notifyUrl = models.CharField(max_length=250, db_column='notify_url')
    timeout = models.IntegerField(db_column='timeout')
    notifyFlag = models.CharField(max_length=250, db_column='notify_flag')
    backUrl = models.CharField(max_length=250, db_column='back_url')
    repayFlag = models.SmallIntegerField(db_column='repay_flag')
    autoUploadAuditFileFlag = models.SmallIntegerField(db_column='AUTO_UPLOAD_AUDIT_FILE_FLAG')

    class Meta:
        db_table = 't_channel'
        managed = False


class PaymentOrg(models.Model):
    orgId = models.CharField(max_length=30, db_column='org_id', primary_key=True)
    companyCode = models.CharField(max_length=30, db_column='company_code')
    orgName = models.CharField(max_length=100, db_column='org_name')
    interfaceType = models.IntegerField(db_column='interface_type')
    orgAbility = models.IntegerField(db_column='org_ability')
    createTime = models.CharField(max_length=14, db_column='create_time')
    modifiedTime = models.IntegerField(db_column='modified_time')
    smallLog = models.BinaryField(db_column='small_logo')
    mediumLog = models.BinaryField(db_column='medium_logo')
    largeLog = models.BinaryField(db_column='large_logo')
    authMode = models.SmallIntegerField(db_column='auth_mode')
    paymentMethod = models.IntegerField(db_column='payment_method')
    orderNo = models.SmallIntegerField(db_column='order_no')
    status = models.SmallIntegerField(db_column='status')
    displayBankFlag = models.IntegerField(db_column='display_bank_flag')
    description = models.CharField(max_length=2500, db_column='description')
    reversePeriod = models.IntegerField(db_column='reverse_period')
    directFlag = models.IntegerField(db_column='direct_flag')
    reverseMaxTime = models.IntegerField(db_column='reverse_max_time')
    rate = models.FloatField(db_column='rate')
    partReversalFlag = models.IntegerField(db_column='part_reversal_flag')
    orgType = models.IntegerField(db_column='org_type')
    orgAlias = models.CharField(max_length=100, db_column='org_alias')
    marketInfo = models.CharField(max_length=250, db_column='market_info')

    class Meta:
        db_table = 't_payment_org'
        managed = False


class TPaymentUser(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    user_type = models.BigIntegerField()
    parent_user_type = models.BigIntegerField(blank=True, null=True)
    parent_user_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    bill_mode = models.BigIntegerField(blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    last_sync_time = models.CharField(max_length=14, blank=True, null=True)
    cert_type = models.CharField(max_length=30, blank=True, null=True)
    cert_id = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    brand_code = models.CharField(max_length=32, blank=True, null=True)
    city_code = models.CharField(max_length=30, blank=True, null=True)
    prov_code = models.CharField(max_length=30, blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    login_password = models.CharField(max_length=200, blank=True, null=True)
    payment_password = models.CharField(max_length=200, blank=True, null=True)
    dynamic_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_user'


class TPaymentService(models.Model):
    service_id = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    pay_timeout = models.CharField(max_length=4, blank=True, null=True)
    date_change_time = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_service'


class MerchantChannelServiceModel(models.Model):
    mearchant_id = models.CharField(max_length=30)
    merchant_name = models.CharField(max_length=50)
    channel_id = models.CharField(max_length=30)
    channel_name = models.CharField(max_length=50)
    service_id = models.CharField(max_length=30)
    service_name = models.CharField(max_length=50)
    account_id = models.CharField(max_length=50)
    pay_org = models.CharField(max_length=50)
    org_name = models.CharField(max_length=50)

    class Meta:
        managed = False


class CronJob(models.Model):
    trigger_name = models.CharField(db_column='trigger_name', max_length=200)
    job_name = models.CharField(db_column='job_name', max_length=200)
    cron_expression = models.CharField(max_length=120)
    next_fire_time = models.BigIntegerField()
    prev_fire_time = models.BigIntegerField()
    trigger_state = models.CharField(max_length=16)

    class Meta:
        managed = False