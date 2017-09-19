# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CcbCardbin(models.Model):
    cardbin = models.CharField(max_length=6, blank=True, null=True)
    card_type = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ccb_cardbin'


class ConfigRevision(models.Model):
    seq_id = models.BigIntegerField(primary_key=True)
    node_id = models.CharField(max_length=50, blank=True, null=True)
    config_name = models.CharField(max_length=50, blank=True, null=True)
    revision = models.BigIntegerField(blank=True, null=True)
    publish_date = models.CharField(max_length=14, blank=True, null=True)
    update_date = models.CharField(max_length=14, blank=True, null=True)
    update_result = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_revision'


class DelFlag(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'del_flag'


class DelFlagOrder(models.Model):
    payment_order_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'del_flag_order'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FlagLogBak(models.Model):
    log_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'flag_log_bak'


class FlagLogDel(models.Model):
    log_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'flag_log_del'


class FlagOrderBak(models.Model):
    payment_order_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'flag_order_bak'


class FlagOrderDel(models.Model):
    payment_order_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'flag_order_del'


class LuceneUser(models.Model):
    name_field = models.CharField(db_column='name_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    value_field = models.BinaryField(db_column='value_', blank=True, null=True)  # Field renamed because it ended with '_'.
    size_field = models.IntegerField(db_column='size_', blank=True, null=True)  # Field renamed because it ended with '_'.
    lf_field = models.DateTimeField(db_column='lf_', blank=True, null=True)  # Field renamed because it ended with '_'.
    deleted_field = models.CharField(db_column='deleted_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'lucene_user'


class Q1(models.Model):
    payment_order_id = models.CharField(max_length=100)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q1'


class Q2(models.Model):
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'q2'


class Q21(models.Model):
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q21'


class Q2Log(models.Model):
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    pay_status = models.BigIntegerField(blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    pay_org_id = models.CharField(max_length=30)
    sl = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q2log'


class Q3(models.Model):
    order_id = models.CharField(max_length=100, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    o_settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    l_settle_rate = models.FloatField(blank=True, null=True)
    l_fee = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q3'


class Q4(models.Model):
    payment_order_id = models.CharField(max_length=100)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'q4'


class QrtzBlobTriggers(models.Model):
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    blob_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_blob_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class QrtzCalendars(models.Model):
    calendar_name = models.CharField(primary_key=True, max_length=200)
    calendar = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'qrtz_calendars'


class QrtzCronTriggers(models.Model):
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    cron_expression = models.CharField(max_length=120)
    time_zone_id = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_cron_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class QrtzFiredTriggers(models.Model):
    entry_id = models.CharField(primary_key=True, max_length=95)
    trigger_name = models.CharField(max_length=200)
    trigger_group = models.CharField(max_length=200)
    is_volatile = models.CharField(max_length=1)
    instance_name = models.CharField(max_length=200)
    fired_time = models.BigIntegerField()
    priority = models.BigIntegerField()
    state = models.CharField(max_length=16)
    job_name = models.CharField(max_length=200, blank=True, null=True)
    job_group = models.CharField(max_length=200, blank=True, null=True)
    is_stateful = models.CharField(max_length=1, blank=True, null=True)
    requests_recovery = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_fired_triggers'


class QrtzJobDetails(models.Model):
    job_name = models.CharField(max_length=200)
    job_group = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True, null=True)
    job_class_name = models.CharField(max_length=250)
    is_durable = models.CharField(max_length=1)
    is_volatile = models.CharField(max_length=1)
    is_stateful = models.CharField(max_length=1)
    requests_recovery = models.CharField(max_length=1)
    job_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_job_details'
        unique_together = (('job_name', 'job_group'),)


class QrtzJobListeners(models.Model):
    job_name = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='job_name')
    job_group = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='job_group')
    job_listener = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'qrtz_job_listeners'
        unique_together = (('job_name', 'job_group', 'job_listener'),)


class QrtzLocks(models.Model):
    lock_name = models.CharField(primary_key=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'qrtz_locks'


class QrtzPausedTriggerGrps(models.Model):
    trigger_group = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'qrtz_paused_trigger_grps'


class QrtzSchedulerState(models.Model):
    instance_name = models.CharField(primary_key=True, max_length=200)
    last_checkin_time = models.BigIntegerField()
    checkin_interval = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'qrtz_scheduler_state'


class QrtzSimpleTriggers(models.Model):
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    repeat_count = models.IntegerField()
    repeat_interval = models.BigIntegerField()
    times_triggered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qrtz_simple_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class QrtzTriggerListeners(models.Model):
    trigger_name = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_name')
    trigger_group = models.ForeignKey('QrtzTriggers', models.DO_NOTHING, db_column='trigger_group')
    trigger_listener = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'qrtz_trigger_listeners'
        unique_together = (('trigger_name', 'trigger_group', 'trigger_listener'),)


class QrtzTriggers(models.Model):
    trigger_name = models.CharField(max_length=200)
    trigger_group = models.CharField(max_length=200)
    job_name = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='job_name')
    job_group = models.ForeignKey(QrtzJobDetails, models.DO_NOTHING, db_column='job_group')
    is_volatile = models.CharField(max_length=1)
    description = models.CharField(max_length=250, blank=True, null=True)
    next_fire_time = models.BigIntegerField(blank=True, null=True)
    prev_fire_time = models.BigIntegerField(blank=True, null=True)
    priority = models.BigIntegerField(blank=True, null=True)
    trigger_state = models.CharField(max_length=16)
    trigger_type = models.CharField(max_length=8)
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField(blank=True, null=True)
    calendar_name = models.CharField(max_length=200, blank=True, null=True)
    misfire_instr = models.IntegerField(blank=True, null=True)
    job_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrtz_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class SysExportSchema01(models.Model):
    process_order = models.FloatField(blank=True, null=True)
    duplicate = models.FloatField(blank=True, null=True)
    dump_fileid = models.FloatField(blank=True, null=True)
    dump_position = models.FloatField(blank=True, null=True)
    dump_length = models.FloatField(blank=True, null=True)
    dump_orig_length = models.FloatField(blank=True, null=True)
    dump_allocation = models.FloatField(blank=True, null=True)
    completed_rows = models.FloatField(blank=True, null=True)
    error_count = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    object_type_path = models.CharField(max_length=200, blank=True, null=True)
    object_path_seqno = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    in_progress = models.CharField(max_length=1, blank=True, null=True)
    object_name = models.CharField(max_length=500, blank=True, null=True)
    object_long_name = models.CharField(max_length=4000, blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    original_object_schema = models.CharField(max_length=30, blank=True, null=True)
    original_object_name = models.CharField(max_length=4000, blank=True, null=True)
    partition_name = models.CharField(max_length=30, blank=True, null=True)
    subpartition_name = models.CharField(max_length=30, blank=True, null=True)
    dataobj_num = models.FloatField(blank=True, null=True)
    flags = models.FloatField(blank=True, null=True)
    property = models.FloatField(blank=True, null=True)
    trigflag = models.FloatField(blank=True, null=True)
    creation_level = models.FloatField(blank=True, null=True)
    completion_time = models.DateField(blank=True, null=True)
    object_tablespace = models.CharField(max_length=30, blank=True, null=True)
    size_estimate = models.FloatField(blank=True, null=True)
    object_row = models.FloatField(blank=True, null=True)
    processing_state = models.CharField(max_length=1, blank=True, null=True)
    processing_status = models.CharField(max_length=1, blank=True, null=True)
    base_process_order = models.FloatField(blank=True, null=True)
    base_object_type = models.CharField(max_length=30, blank=True, null=True)
    base_object_name = models.CharField(max_length=30, blank=True, null=True)
    base_object_schema = models.CharField(max_length=30, blank=True, null=True)
    ancestor_process_order = models.FloatField(blank=True, null=True)
    domain_process_order = models.FloatField(blank=True, null=True)
    parallelization = models.FloatField(blank=True, null=True)
    unload_method = models.FloatField(blank=True, null=True)
    load_method = models.FloatField(blank=True, null=True)
    granules = models.FloatField(blank=True, null=True)
    scn = models.FloatField(blank=True, null=True)
    grantor = models.CharField(max_length=30, blank=True, null=True)
    xml_clob = models.TextField(blank=True, null=True)
    parent_process_order = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    value_t = models.CharField(max_length=4000, blank=True, null=True)
    value_n = models.FloatField(blank=True, null=True)
    is_default = models.FloatField(blank=True, null=True)
    file_type = models.FloatField(blank=True, null=True)
    user_directory = models.CharField(max_length=4000, blank=True, null=True)
    user_file_name = models.CharField(max_length=4000, blank=True, null=True)
    file_name = models.CharField(max_length=4000, blank=True, null=True)
    extend_size = models.FloatField(blank=True, null=True)
    file_max_size = models.FloatField(blank=True, null=True)
    process_name = models.CharField(max_length=30, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    work_item = models.CharField(max_length=30, blank=True, null=True)
    object_number = models.FloatField(blank=True, null=True)
    completed_bytes = models.FloatField(blank=True, null=True)
    total_bytes = models.FloatField(blank=True, null=True)
    metadata_io = models.FloatField(blank=True, null=True)
    data_io = models.FloatField(blank=True, null=True)
    cumulative_time = models.FloatField(blank=True, null=True)
    packet_number = models.FloatField(blank=True, null=True)
    instance_id = models.FloatField(blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    seed = models.FloatField(blank=True, null=True)
    last_file = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    job_mode = models.CharField(max_length=30, blank=True, null=True)
    queue_tabnum = models.FloatField(blank=True, null=True)
    control_queue = models.CharField(max_length=30, blank=True, null=True)
    status_queue = models.CharField(max_length=30, blank=True, null=True)
    remote_link = models.CharField(max_length=4000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    job_version = models.CharField(max_length=30, blank=True, null=True)
    db_version = models.CharField(max_length=30, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    phase = models.FloatField(blank=True, null=True)
    guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    metadata_buffer_size = models.FloatField(blank=True, null=True)
    data_buffer_size = models.FloatField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    platform = models.CharField(max_length=101, blank=True, null=True)
    abort_step = models.FloatField(blank=True, null=True)
    instance = models.CharField(max_length=60, blank=True, null=True)
    cluster_ok = models.FloatField(blank=True, null=True)
    service_name = models.CharField(max_length=100, blank=True, null=True)
    object_int_oid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_export_schema_01'
        unique_together = (('process_order', 'duplicate'),)


class SysIcon(models.Model):
    icon_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    url = models.CharField(max_length=765, blank=True, null=True)
    icon_type = models.CharField(max_length=100, blank=True, null=True)
    icon_content = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_icon'


class SysIconRole(models.Model):
    item_id = models.BigIntegerField(primary_key=True)
    icon_id = models.BigIntegerField()
    role_id = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'sys_icon_role'


class SysLogs(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    log_time = models.CharField(max_length=14, blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    client_ip = models.CharField(max_length=50, blank=True, null=True)
    log_level = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_logs'


class SysPermission(models.Model):
    permission_id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=100, blank=True, null=True)
    permission_type = models.BigIntegerField(blank=True, null=True)
    parent_id = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    system_id = models.CharField(max_length=100, blank=True, null=True)
    delete_flag = models.BigIntegerField(blank=True, null=True)
    order_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_permission'


class SysRole(models.Model):
    role_id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=50)
    status = models.BigIntegerField()
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRolePermission(models.Model):
    role_permission_id = models.BigIntegerField(primary_key=True)
    permission_id = models.CharField(max_length=32, blank=True, null=True)
    role_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role_permission'


class SysUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    authenticator = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    failure_times = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    user_role_id = models.BigIntegerField(primary_key=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    role_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class SystemLock(models.Model):
    entity_key = models.CharField(primary_key=True, max_length=50)
    node_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_lock'


class SystemNode(models.Model):
    node_id = models.CharField(primary_key=True, max_length=50)
    ticket = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_node'


class T1(models.Model):
    ip = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't1'


class T2(models.Model):
    n1 = models.CharField(max_length=30, blank=True, null=True)
    n2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2'


class TAlarm(models.Model):
    id = models.BigIntegerField(primary_key=True)
    alarm_category = models.CharField(max_length=250, blank=True, null=True)
    alarm_time = models.CharField(max_length=14, blank=True, null=True)
    alarm_level = models.CharField(max_length=250, blank=True, null=True)
    alarm_description = models.CharField(max_length=250, blank=True, null=True)
    alarm_status = models.FloatField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_alarm'


class TAreaProvince(models.Model):
    area_code = models.CharField(primary_key=True, max_length=30)
    province_code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    crm_interface = models.BigIntegerField(blank=True, null=True)
    crm_operator = models.CharField(max_length=32, blank=True, null=True)
    crm_area_code = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_area_province'


class TAuditAccountLog(models.Model):
    account_log_id = models.BigIntegerField(primary_key=True)
    log_id = models.BigIntegerField(blank=True, null=True)
    org_id = models.CharField(max_length=30, blank=True, null=True)
    audit_date = models.CharField(max_length=8)
    account_no = models.CharField(max_length=50)
    file_locstr = models.CharField(max_length=100, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    download_status = models.BigIntegerField(blank=True, null=True)
    download_fail_reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.BigIntegerField()
    upload_status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_audit_account_log'


class TAuditChannelFile(models.Model):
    audit_id = models.BigIntegerField()
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    merchant_id = models.CharField(max_length=50, blank=True, null=True)
    service_id = models.CharField(max_length=50, blank=True, null=True)
    audit_type = models.NullBooleanField()
    audit_time_type = models.NullBooleanField()
    audit_file_type = models.CharField(max_length=10, blank=True, null=True)
    file_generate_type = models.NullBooleanField()
    file_generate_time = models.CharField(max_length=14, blank=True, null=True)
    start_time = models.CharField(max_length=14, blank=True, null=True)
    end_time = models.CharField(max_length=14, blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    audit_status = models.NullBooleanField()
    audit_file = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_audit_channel_file'


class TAuditCompanyFile(models.Model):
    audit_id = models.BigIntegerField()
    company_code = models.CharField(max_length=30, blank=True, null=True)
    org_code = models.CharField(max_length=30, blank=True, null=True)
    audit_date = models.CharField(max_length=8, blank=True, null=True)
    file_acquire_time = models.CharField(max_length=14, blank=True, null=True)
    account_no = models.CharField(max_length=50, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    audit_status = models.NullBooleanField()
    audit_file = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_audit_company_file'


class TAuditFailureRecord(models.Model):
    audit_failure_id = models.BigIntegerField(primary_key=True)
    org_id = models.CharField(max_length=30, blank=True, null=True)
    audit_date = models.CharField(max_length=14, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    node_id = models.CharField(max_length=100, blank=True, null=True)
    filepath = models.CharField(max_length=250, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    content = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_audit_failure_record'


class TAuditLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    org_id = models.CharField(max_length=30, blank=True, null=True)
    audit_date = models.CharField(max_length=8)
    audit_time = models.CharField(max_length=14)
    status = models.BigIntegerField()
    fee_settle_status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 't_audit_log'


class TAuditTask(models.Model):
    task_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.BigIntegerField(blank=True, null=True)
    audit_type = models.BigIntegerField(blank=True, null=True)
    start_time = models.CharField(max_length=14, blank=True, null=True)
    end_time = models.CharField(max_length=14, blank=True, null=True)
    org_id = models.CharField(max_length=30, blank=True, null=True)
    account_id = models.CharField(max_length=50, blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_audit_task'


class TBankBranch(models.Model):
    branch_id = models.CharField(max_length=32)
    company_code = models.CharField(max_length=30)
    title = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bank_branch'
        unique_together = (('branch_id', 'company_code'),)


class TBatchRefund(models.Model):
    batch_id = models.CharField(primary_key=True, max_length=20)
    operator_name = models.CharField(max_length=40)
    start_time = models.CharField(max_length=14, blank=True, null=True)
    end_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    handle_result = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_batch_refund'


class TBatchRefundOrder(models.Model):
    batch_id = models.CharField(max_length=20)
    channel_id = models.CharField(max_length=30)
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    order_amount = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_batch_refund_order'


class TBrand(models.Model):
    brand_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_brand'


class TCashierDeskColumn(models.Model):
    cashier_desk_column_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30)
    service_id = models.CharField(max_length=30)
    column_id = models.CharField(max_length=30)
    order_no = models.BigIntegerField(blank=True, null=True)
    merchant_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cashier_desk_column'


class TCashierDeskPaymentOrg(models.Model):
    cashier_desk_payment_org_id = models.BigIntegerField(primary_key=True)
    cashier_desk_sub_column_id = models.BigIntegerField()
    org_id = models.CharField(max_length=30)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    bank_abbr = models.CharField(max_length=30, blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    pay_channel_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cashier_desk_payment_org'


class TCashierDeskSubColumn(models.Model):
    cashier_desk_sub_column_id = models.BigIntegerField(primary_key=True)
    cashier_desk_column_id = models.BigIntegerField()
    sub_column_id = models.CharField(max_length=30)
    order_no = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cashier_desk_sub_column'


class TChannel(models.Model):
    channel_id = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    pswd = models.CharField(max_length=100, blank=True, null=True)
    encrypt_algorithm = models.CharField(max_length=30, blank=True, null=True)
    view_flag = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    notify_url = models.CharField(max_length=250, blank=True, null=True)
    timeout = models.BigIntegerField(blank=True, null=True)
    notify_flag = models.CharField(max_length=250, blank=True, null=True)
    back_url = models.CharField(max_length=250, blank=True, null=True)
    repay_flag = models.BigIntegerField(blank=True, null=True)
    auto_upload_audit_file_flag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_channel'


class TChannelAuditLog(models.Model):
    audit_log_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30)
    order_channel_id = models.CharField(max_length=30, blank=True, null=True)
    audit_req_time = models.CharField(max_length=14)
    audit_time_type = models.FloatField(blank=True, null=True)
    start_time = models.CharField(max_length=14, blank=True, null=True)
    end_time = models.CharField(max_length=14, blank=True, null=True)
    audit_resp_time = models.CharField(max_length=14, blank=True, null=True)
    audit_result = models.FloatField(blank=True, null=True)
    audit_fail_reason = models.CharField(max_length=250, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    audit_file = models.CharField(max_length=150, blank=True, null=True)
    notify_req_time = models.CharField(max_length=14, blank=True, null=True)
    notify_resp_time = models.CharField(max_length=14, blank=True, null=True)
    download_req_time = models.CharField(max_length=14, blank=True, null=True)
    download_resp_time = models.CharField(max_length=14, blank=True, null=True)
    s_upload_status = models.BigIntegerField(blank=True, null=True)
    o_upload_status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_channel_audit_log'


class TChannelInterface(models.Model):
    channel_id = models.CharField(max_length=30)
    service = models.CharField(max_length=50)
    action = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_channel_interface'
        unique_together = (('channel_id', 'service', 'action'),)


class TChannelIp(models.Model):
    ip_addr = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_channel_ip'
        unique_together = (('ip_addr', 'channel_id'),)


class TChannelMerchant(models.Model):
    channel_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 't_channel_merchant'
        unique_together = (('channel_id', 'user_id', 'user_type'),)


class TChannelService(models.Model):
    service_id = models.CharField(max_length=30)
    channel_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_channel_service'
        unique_together = (('service_id', 'channel_id'),)


class TCity(models.Model):
    city_code = models.CharField(primary_key=True, max_length=20)
    city_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_city'


class TColumn(models.Model):
    column_id = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_column'


class TCompanyBank(models.Model):
    company_code = models.CharField(max_length=32)
    bank_company_code = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    sign_flag = models.BigIntegerField(blank=True, null=True)
    card_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_company_bank'
        unique_together = (('company_code', 'bank_company_code', 'code'),)


class TComplaint(models.Model):
    payment_complaint_id = models.CharField(primary_key=True, max_length=100)
    complaint_id = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=30)
    channel_type = models.BigIntegerField(blank=True, null=True)
    complaint_type = models.BigIntegerField()
    complaint_user = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    complaint_content = models.CharField(max_length=500, blank=True, null=True)
    complaint_status = models.BigIntegerField(blank=True, null=True)
    complaint_date = models.CharField(max_length=8, blank=True, null=True)
    complaint_time = models.CharField(max_length=14, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    accept_time = models.CharField(max_length=14, blank=True, null=True)
    refusal_reason = models.CharField(max_length=250, blank=True, null=True)
    deal_time = models.CharField(max_length=14, blank=True, null=True)
    deal_detail = models.CharField(max_length=500, blank=True, null=True)
    complaint_num = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.CharField(max_length=100, blank=True, null=True)
    create_user_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_complaint'


class TComplaintLog(models.Model):
    complaint_log_id = models.BigIntegerField(primary_key=True)
    payment_complaint_id = models.CharField(max_length=100)
    complaint_id = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=30)
    complaint_date = models.CharField(max_length=8, blank=True, null=True)
    complaint_content = models.CharField(max_length=500, blank=True, null=True)
    accept_type = models.BigIntegerField(blank=True, null=True)
    accept_time = models.CharField(max_length=14, blank=True, null=True)
    refusal_reason = models.CharField(max_length=250, blank=True, null=True)
    deal_time = models.CharField(max_length=14, blank=True, null=True)
    deal_detail = models.CharField(max_length=500, blank=True, null=True)
    deal_user_id = models.CharField(max_length=100, blank=True, null=True)
    deal_user_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_complaint_log'


class TDict(models.Model):
    dict_code = models.CharField(primary_key=True, max_length=100)
    dict_name = models.CharField(max_length=100)
    dict_value = models.CharField(max_length=255)
    dict_type = models.BigIntegerField()
    dict_parent_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict'


class TDimChannel(models.Model):
    channel_key = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_channel'


class TDimHour(models.Model):
    hour_key = models.IntegerField(primary_key=True)
    time_key = models.IntegerField(blank=True, null=True)
    calendar_month = models.CharField(max_length=32, blank=True, null=True)
    calendar_quarter = models.CharField(max_length=32, blank=True, null=True)
    calendar_year = models.CharField(max_length=32, blank=True, null=True)
    calendar_semester = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_hour'


class TDimIntelligentChannel(models.Model):
    intelligent_channel_key = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=8, blank=True, null=True)
    end_date = models.CharField(max_length=8, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_intelligent_channel'


class TDimMerchant(models.Model):
    merchant_key = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_merchant'


class TDimPaymentCompany(models.Model):
    payment_org_key = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_payment_company'


class TDimPaymentOrg(models.Model):
    org_key = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    payment_org_key = models.CharField(max_length=32, blank=True, null=True)
    payment_method = models.BigIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_payment_org'


class TDimService(models.Model):
    service_key = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_service'


class TDimTime(models.Model):
    time_key = models.IntegerField(primary_key=True)
    fulldate_key = models.DateField(blank=True, null=True)
    calendar_month = models.CharField(max_length=32, blank=True, null=True)
    calendar_quarter = models.CharField(max_length=32, blank=True, null=True)
    calendar_year = models.CharField(max_length=32, blank=True, null=True)
    calendar_semester = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dim_time'


class TFactBillSummary(models.Model):
    payment_order_id = models.CharField(max_length=100)
    pay_type = models.BigIntegerField()
    order_id = models.CharField(max_length=100, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    city_code = models.CharField(max_length=20, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_bill_summary'
        unique_together = (('payment_order_id', 'pay_type'),)


class TFactPaymentDaily(models.Model):
    hour_key = models.IntegerField()
    time_key = models.IntegerField(blank=True, null=True)
    service_key = models.CharField(max_length=32, blank=True, null=True)
    org_key = models.CharField(max_length=32, blank=True, null=True)
    channel_key = models.CharField(max_length=32, blank=True, null=True)
    merchant_key = models.CharField(max_length=32, blank=True, null=True)
    payment_num = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    unpaid_num = models.BigIntegerField(blank=True, null=True)
    reversed_num = models.BigIntegerField(blank=True, null=True)
    paid_amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_payment_daily'


class TFactPaymentDailyExp(models.Model):
    hour_key = models.IntegerField(blank=True, null=True)
    time_key = models.IntegerField(blank=True, null=True)
    intelligent_channel_key = models.BigIntegerField(blank=True, null=True)
    intelligent_channel_type = models.BigIntegerField(blank=True, null=True)
    org_key = models.CharField(max_length=32, blank=True, null=True)
    payment_org_key = models.CharField(max_length=32, blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    paid_amount = models.BigIntegerField(blank=True, null=True)
    expected_trans_proportion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_payment_daily_exp'


class TFactPaymentLog(models.Model):
    time_key = models.IntegerField()
    month_key = models.IntegerField(blank=True, null=True)
    year_key = models.IntegerField(blank=True, null=True)
    service_key = models.CharField(max_length=32, blank=True, null=True)
    org_key = models.CharField(max_length=32, blank=True, null=True)
    channel_key = models.CharField(max_length=32, blank=True, null=True)
    merchant_key = models.CharField(max_length=32, blank=True, null=True)
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    pay_user = models.CharField(max_length=50, blank=True, null=True)
    order_time = models.CharField(max_length=14, blank=True, null=True)
    paid_time = models.CharField(max_length=14, blank=True, null=True)
    pay_status = models.BigIntegerField(blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_payment_log'


class TFactPaymentMonth(models.Model):
    time_key = models.IntegerField()
    month_key = models.IntegerField(blank=True, null=True)
    service_key = models.CharField(max_length=32, blank=True, null=True)
    org_key = models.CharField(max_length=32, blank=True, null=True)
    channel_key = models.CharField(max_length=32, blank=True, null=True)
    merchant_key = models.CharField(max_length=32, blank=True, null=True)
    payment_num = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    unpaid_num = models.BigIntegerField(blank=True, null=True)
    reversed_num = models.BigIntegerField(blank=True, null=True)
    paid_amount = models.BigIntegerField(blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    unpaid_amount = models.BigIntegerField(blank=True, null=True)
    reversed_amount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_payment_month'


class TFactSettleFee(models.Model):
    pay_com_code = models.CharField(max_length=30, blank=True, null=True)
    pay_com_name = models.CharField(max_length=50, blank=True, null=True)
    pay_org_code = models.CharField(max_length=30, blank=True, null=True)
    pay_org_alias = models.CharField(max_length=50, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    merchant_code = models.CharField(max_length=30, blank=True, null=True)
    merchant_name = models.CharField(max_length=50, blank=True, null=True)
    pay_service_code = models.CharField(max_length=30, blank=True, null=True)
    pay_service_name = models.CharField(max_length=50, blank=True, null=True)
    total_trans_amount = models.BigIntegerField(blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    total_trans_fee = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_settle_fee'


class TFactSettleFeeCity(models.Model):
    pay_com_code = models.CharField(max_length=30, blank=True, null=True)
    pay_com_name = models.CharField(max_length=50, blank=True, null=True)
    pay_org_code = models.CharField(max_length=30, blank=True, null=True)
    pay_org_alias = models.CharField(max_length=50, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    pay_service_code = models.CharField(max_length=30, blank=True, null=True)
    pay_service_name = models.CharField(max_length=50, blank=True, null=True)
    total_trans_amount = models.BigIntegerField(blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    total_trans_fee = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_settle_fee_city'


class TFactSettleFeeMerchant(models.Model):
    pay_com_code = models.CharField(max_length=30, blank=True, null=True)
    pay_com_name = models.CharField(max_length=50, blank=True, null=True)
    pay_org_code = models.CharField(max_length=30, blank=True, null=True)
    pay_org_alias = models.CharField(max_length=50, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    channel_name = models.CharField(max_length=50, blank=True, null=True)
    merchant_code = models.CharField(max_length=30, blank=True, null=True)
    merchant_name = models.CharField(max_length=50, blank=True, null=True)
    pay_service_code = models.CharField(max_length=30, blank=True, null=True)
    pay_service_name = models.CharField(max_length=50, blank=True, null=True)
    total_trans_amount = models.BigIntegerField(blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    total_trans_fee = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fact_settle_fee_merchant'


class TIntelligentChannel(models.Model):
    intelligent_channel_id = models.BigIntegerField(primary_key=True)
    intelligent_channel_name = models.CharField(max_length=100, blank=True, null=True)
    intelligent_channel_type = models.BigIntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=8, blank=True, null=True)
    end_date = models.CharField(max_length=8, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    create_user_id = models.CharField(max_length=100, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    modify_user_id = models.CharField(max_length=100, blank=True, null=True)
    modify_reason = models.CharField(max_length=250, blank=True, null=True)
    proportion_threshold = models.FloatField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_intelligent_channel'


class TIntelligentChannelChannel(models.Model):
    intelligent_channel_id = models.BigIntegerField()
    channel_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_intelligent_channel_channel'
        unique_together = (('intelligent_channel_id', 'channel_id'),)


class TIntelligentChannelOrg(models.Model):
    intelligent_channel_org_id = models.BigIntegerField(primary_key=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    intelligent_channel_type = models.BigIntegerField(blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    company_code = models.CharField(max_length=30, blank=True, null=True)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    round_flag = models.BigIntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate_order_no = models.BigIntegerField(blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_intelligent_channel_org'


class TIntelligentChannelScale(models.Model):
    scale_id = models.BigIntegerField(primary_key=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    payment_method_num = models.BigIntegerField(blank=True, null=True)
    trans_amount_proportion = models.FloatField(blank=True, null=True)
    trans_num = models.BigIntegerField(blank=True, null=True)
    rate_order_no = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_intelligent_channel_scale'


class TInterfaceChannel(models.Model):
    channel_id = models.CharField(max_length=30)
    service = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    order_channel_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_interface_channel'
        unique_together = (('channel_id', 'service', 'action', 'order_channel_id'),)


class TLog4JConfig(models.Model):
    pac_key = models.CharField(primary_key=True, max_length=200)
    pac_desc = models.CharField(max_length=250, blank=True, null=True)
    pac_level = models.CharField(max_length=20, blank=True, null=True)
    appender_type = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log4j_config'


class TLog4JMessage(models.Model):
    mes_id = models.BigIntegerField(primary_key=True)
    level_name = models.CharField(max_length=20, blank=True, null=True)
    thread_name = models.CharField(max_length=300, blank=True, null=True)
    mes_content = models.CharField(max_length=2000, blank=True, null=True)
    client_identify = models.CharField(max_length=50, blank=True, null=True)
    date_time = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log4j_message'


class TMessage(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    msg_type = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.BigIntegerField(blank=True, null=True)
    data = models.CharField(max_length=2500, blank=True, null=True)
    sent_count = models.BigIntegerField(blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    deliver_time = models.CharField(max_length=14)
    ack_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 't_message'


class TMessageDef(models.Model):
    msg_type = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    ack_flag = models.BigIntegerField(blank=True, null=True)
    retry_times = models.BigIntegerField(blank=True, null=True)
    wait_time = models.BigIntegerField(blank=True, null=True)
    priority = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_message_def'


class TMsisdnArea(models.Model):
    seq_id = models.BigIntegerField(primary_key=True)
    area_code = models.CharField(max_length=30, blank=True, null=True)
    prefix_low = models.CharField(max_length=15, blank=True, null=True)
    prefix_high = models.CharField(max_length=15, blank=True, null=True)
    crm_interface = models.BigIntegerField(blank=True, null=True)
    crm_operator = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_msisdn_area'


class TMsisdnAreaBak(models.Model):
    seq_id = models.BigIntegerField(primary_key=True)
    area_code = models.CharField(max_length=30, blank=True, null=True)
    prefix_low = models.CharField(max_length=15, blank=True, null=True)
    prefix_high = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_msisdn_area_bak'


class TOrgCooperation(models.Model):
    org_id = models.CharField(max_length=30)
    service_id = models.CharField(max_length=30)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    fixed_fee = models.BigIntegerField(blank=True, null=True)
    floating_rate = models.FloatField(blank=True, null=True)
    floating_threshold = models.BigIntegerField(blank=True, null=True)
    rating_mode = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_org_cooperation'
        unique_together = (('org_id', 'service_id'),)


class TOrgMaintainPlan(models.Model):
    plan_id = models.BigIntegerField(primary_key=True)
    org_id = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    start_time = models.CharField(max_length=6, blank=True, null=True)
    end_time = models.CharField(max_length=6, blank=True, null=True)
    create_user = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modify_user = models.CharField(max_length=32, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    period_type = models.BigIntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=8, blank=True, null=True)
    end_date = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_org_maintain_plan'


class TPaymentAccount(models.Model):
    account_id = models.CharField(max_length=50)
    org_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.BigIntegerField(blank=True, null=True)
    account_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_account'
        unique_together = (('account_id', 'org_id'),)


class TPaymentAccountParam(models.Model):
    account_id = models.CharField(max_length=50)
    org_id = models.CharField(max_length=30)
    param_code = models.CharField(max_length=100)
    param_value = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_account_param'
        unique_together = (('account_id', 'org_id', 'param_code'),)


class TPaymentCompany(models.Model):
    company_code = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=100)
    company_type = models.BigIntegerField(blank=True, null=True)
    small_logo = models.BinaryField(blank=True, null=True)
    medium_logo = models.BinaryField(blank=True, null=True)
    large_logo = models.BinaryField(blank=True, null=True)
    status = models.BigIntegerField()
    company_alias = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_company'


class TPaymentDelegation(models.Model):
    service_id = models.CharField(max_length=30)
    account_id = models.CharField(max_length=50)
    org_id = models.CharField(max_length=30)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    dele_usage = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_delegation'
        unique_together = (('service_id', 'account_id', 'org_id'),)


class TPaymentLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    pay_org_id = models.CharField(max_length=30)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    pay_trans_id = models.CharField(max_length=100, blank=True, null=True)
    pay_request_id = models.CharField(max_length=100, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    pay_response_id = models.CharField(max_length=100, blank=True, null=True)
    pay_response_time = models.CharField(max_length=14, blank=True, null=True)
    pay_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    pay_status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    cancel_time = models.CharField(max_length=14, blank=True, null=True)
    reverse_status = models.BigIntegerField(blank=True, null=True)
    reverse_trans_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_request_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_request_time = models.CharField(max_length=14, blank=True, null=True)
    reverse_response_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_response_time = models.CharField(max_length=14, blank=True, null=True)
    reverse_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_result_code = models.CharField(max_length=100, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    bank_pay_amount = models.BigIntegerField(blank=True, null=True)
    point_pay_trans_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_request_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    point_pay_response_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_response_time = models.CharField(max_length=14, blank=True, null=True)
    point_pay_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_status = models.BigIntegerField(blank=True, null=True)
    point_pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    point_cancel_time = models.CharField(max_length=14, blank=True, null=True)
    point_reverse_status = models.BigIntegerField(blank=True, null=True)
    point_reverse_trans_id = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_request_id = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_request_time = models.CharField(max_length=14, blank=True, null=True)
    point_reverse_response_id = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_response_time = models.CharField(max_length=14, blank=True, null=True)
    point_reverse_result_code = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    reverse_audit_status = models.BigIntegerField(blank=True, null=True)
    reverse_audit_time = models.CharField(max_length=14, blank=True, null=True)
    bank_pay_status = models.BigIntegerField(blank=True, null=True)
    bank_reverse_status = models.BigIntegerField(blank=True, null=True)
    bank_reverse_amount = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    reversal_settle_date = models.CharField(max_length=8, blank=True, null=True)
    pay_channel_type = models.BigIntegerField(blank=True, null=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    frontend_notify_flag = models.NullBooleanField()
    backend_notify_flag = models.NullBooleanField()
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    pay_link = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_log'


class TPaymentLogHistory(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    pay_org_id = models.CharField(max_length=30)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    pay_trans_id = models.CharField(max_length=100, blank=True, null=True)
    pay_request_id = models.CharField(max_length=100, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    pay_response_id = models.CharField(max_length=100, blank=True, null=True)
    pay_response_time = models.CharField(max_length=14, blank=True, null=True)
    pay_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    pay_status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    cancel_time = models.CharField(max_length=14, blank=True, null=True)
    reverse_status = models.BigIntegerField(blank=True, null=True)
    reverse_trans_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_request_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_request_time = models.CharField(max_length=14, blank=True, null=True)
    reverse_response_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_response_time = models.CharField(max_length=14, blank=True, null=True)
    reverse_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_result_code = models.CharField(max_length=100, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    bank_pay_amount = models.BigIntegerField(blank=True, null=True)
    point_pay_trans_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_request_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    point_pay_response_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_response_time = models.CharField(max_length=14, blank=True, null=True)
    point_pay_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    point_pay_status = models.BigIntegerField(blank=True, null=True)
    point_pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    point_cancel_time = models.CharField(max_length=14, blank=True, null=True)
    point_reverse_status = models.BigIntegerField(blank=True, null=True)
    point_reverse_trans_id = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_request_id = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_request_time = models.CharField(max_length=14, blank=True, null=True)
    point_reverse_response_id = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_response_time = models.CharField(max_length=14, blank=True, null=True)
    point_reverse_result_code = models.CharField(max_length=100, blank=True, null=True)
    point_reverse_org_trans_id = models.CharField(max_length=100, blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    reverse_audit_status = models.BigIntegerField(blank=True, null=True)
    reverse_audit_time = models.CharField(max_length=14, blank=True, null=True)
    bank_pay_status = models.BigIntegerField(blank=True, null=True)
    bank_reverse_status = models.BigIntegerField(blank=True, null=True)
    bank_reverse_amount = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    reversal_settle_date = models.CharField(max_length=8, blank=True, null=True)
    pay_channel_type = models.BigIntegerField(blank=True, null=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    frontend_notify_flag = models.NullBooleanField()
    backend_notify_flag = models.NullBooleanField()
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    pay_link = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_log_history'


class TPaymentMethodHistory(models.Model):
    payment_method_history_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30)
    service_id = models.CharField(max_length=30)
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    org_id = models.CharField(max_length=30, blank=True, null=True)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    bank_abbr = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    last_used_time = models.CharField(max_length=14, blank=True, null=True)
    used_num = models.BigIntegerField(blank=True, null=True)
    pay_channel_type = models.BigIntegerField(blank=True, null=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_method_history'


class TPaymentMethodHistoryNew(models.Model):
    payment_method_history_id = models.BigIntegerField(primary_key=True)
    channel_id = models.CharField(max_length=30)
    service_id = models.CharField(max_length=30)
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    org_id = models.CharField(max_length=30, blank=True, null=True)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    bank_abbr = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    last_used_time = models.CharField(max_length=14, blank=True, null=True)
    used_num = models.BigIntegerField(blank=True, null=True)
    pay_channel_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_method_history_new'


class TPaymentOrder(models.Model):
    payment_order_id = models.CharField(primary_key=True, max_length=100)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    rcv_user_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_user_type = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_time = models.CharField(max_length=14, blank=True, null=True)
    order_url = models.CharField(max_length=250, blank=True, null=True)
    back_url = models.CharField(max_length=250, blank=True, null=True)
    pay_failed_op = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    paid_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    pay_cny_status = models.BigIntegerField(blank=True, null=True)
    pay_points_status = models.BigIntegerField(blank=True, null=True)
    reversal_cny_status = models.BigIntegerField(blank=True, null=True)
    reversal_points_status = models.BigIntegerField(blank=True, null=True)
    topup_no = models.CharField(max_length=32, blank=True, null=True)
    topup_type = models.BigIntegerField(blank=True, null=True)
    delivery_status = models.BigIntegerField(blank=True, null=True)
    delivery_time = models.CharField(max_length=14, blank=True, null=True)
    delivery_error_code = models.CharField(max_length=50, blank=True, null=True)
    notify_status = models.BigIntegerField(blank=True, null=True)
    notify_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_reason = models.CharField(max_length=250, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    notify_url = models.CharField(max_length=250, blank=True, null=True)
    digest = models.CharField(max_length=250, blank=True, null=True)
    required_payment_methods = models.CharField(max_length=250, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    paid_success_num = models.BigIntegerField(blank=True, null=True)
    reversed_time = models.CharField(max_length=14, blank=True, null=True)
    direct_flag = models.BigIntegerField(blank=True, null=True)
    pay_timeout = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    reserve1 = models.CharField(max_length=128, blank=True, null=True)
    reversal_notify_url = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    cashier_desk_type = models.BigIntegerField(blank=True, null=True)
    login_flag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_order'


class TPaymentOrderHistory(models.Model):
    payment_order_id = models.CharField(primary_key=True, max_length=100)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    rcv_user_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_user_type = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_time = models.CharField(max_length=14, blank=True, null=True)
    order_url = models.CharField(max_length=250, blank=True, null=True)
    back_url = models.CharField(max_length=250, blank=True, null=True)
    pay_failed_op = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    paid_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    pay_cny_status = models.BigIntegerField(blank=True, null=True)
    pay_points_status = models.BigIntegerField(blank=True, null=True)
    reversal_cny_status = models.BigIntegerField(blank=True, null=True)
    reversal_points_status = models.BigIntegerField(blank=True, null=True)
    topup_no = models.CharField(max_length=32, blank=True, null=True)
    topup_type = models.BigIntegerField(blank=True, null=True)
    delivery_status = models.BigIntegerField(blank=True, null=True)
    delivery_time = models.CharField(max_length=14, blank=True, null=True)
    delivery_error_code = models.CharField(max_length=50, blank=True, null=True)
    notify_status = models.BigIntegerField(blank=True, null=True)
    notify_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_reason = models.CharField(max_length=250, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    notify_url = models.CharField(max_length=250, blank=True, null=True)
    digest = models.CharField(max_length=250, blank=True, null=True)
    required_payment_methods = models.CharField(max_length=250, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    paid_success_num = models.BigIntegerField(blank=True, null=True)
    reversed_time = models.CharField(max_length=14, blank=True, null=True)
    direct_flag = models.BigIntegerField(blank=True, null=True)
    pay_timeout = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    reserve1 = models.CharField(max_length=128, blank=True, null=True)
    reversal_notify_url = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    cashier_desk_type = models.BigIntegerField(blank=True, null=True)
    login_flag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_order_history'


class TPaymentOrderP(models.Model):
    payment_order_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    rcv_user_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_user_type = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_time = models.CharField(max_length=14, blank=True, null=True)
    order_url = models.CharField(max_length=250, blank=True, null=True)
    back_url = models.CharField(max_length=250, blank=True, null=True)
    pay_failed_op = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    paid_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    pay_cny_status = models.BigIntegerField(blank=True, null=True)
    pay_points_status = models.BigIntegerField(blank=True, null=True)
    reversal_cny_status = models.BigIntegerField(blank=True, null=True)
    reversal_points_status = models.BigIntegerField(blank=True, null=True)
    topup_no = models.CharField(max_length=32, blank=True, null=True)
    topup_type = models.BigIntegerField(blank=True, null=True)
    delivery_status = models.BigIntegerField(blank=True, null=True)
    delivery_time = models.CharField(max_length=14, blank=True, null=True)
    delivery_error_code = models.CharField(max_length=50, blank=True, null=True)
    notify_status = models.BigIntegerField(blank=True, null=True)
    notify_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_reason = models.CharField(max_length=250, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    notify_url = models.CharField(max_length=250, blank=True, null=True)
    digest = models.CharField(max_length=250, blank=True, null=True)
    required_payment_methods = models.CharField(max_length=250, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    paid_success_num = models.BigIntegerField(blank=True, null=True)
    reversed_time = models.CharField(max_length=14, blank=True, null=True)
    direct_flag = models.BigIntegerField(blank=True, null=True)
    pay_timeout = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    reserve1 = models.CharField(max_length=128, blank=True, null=True)
    reversal_notify_url = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    cashier_desk_type = models.BigIntegerField(blank=True, null=True)
    login_flag = models.BigIntegerField(blank=True, null=True)
    interest_total = models.BigIntegerField(blank=True, null=True)
    interest_rate = models.FloatField(blank=True, null=True)
    instalment_term = models.IntegerField(blank=True, null=True)
    busi_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_order_p'


class TPaymentOrg(models.Model):
    org_id = models.CharField(primary_key=True, max_length=30)
    company_code = models.CharField(max_length=30, blank=True, null=True)
    org_name = models.CharField(max_length=100, blank=True, null=True)
    interface_type = models.BigIntegerField(blank=True, null=True)
    org_ability = models.BigIntegerField(blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    modified_time = models.CharField(max_length=14, blank=True, null=True)
    small_logo = models.BinaryField(blank=True, null=True)
    medium_logo = models.BinaryField(blank=True, null=True)
    large_logo = models.BinaryField(blank=True, null=True)
    auth_mode = models.BigIntegerField(blank=True, null=True)
    payment_method = models.BigIntegerField(blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    display_bank_flag = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=2500, blank=True, null=True)
    reverse_period = models.BigIntegerField(blank=True, null=True)
    direct_flag = models.BigIntegerField(blank=True, null=True)
    reverse_max_time = models.BigIntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    part_reversal_flag = models.BigIntegerField(blank=True, null=True)
    org_type = models.BigIntegerField(blank=True, null=True)
    org_alias = models.CharField(max_length=100, blank=True, null=True)
    market_info = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_org'


class TPaymentOrgBranch(models.Model):
    org_id = models.CharField(max_length=30)
    company_code = models.CharField(max_length=30)
    branch_id = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    branch_name = models.CharField(max_length=250, blank=True, null=True)
    test_flag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_org_branch'
        unique_together = (('org_id', 'company_code', 'branch_id', 'city'),)


class TPaymentOrgDict(models.Model):
    seq_id = models.BigIntegerField(primary_key=True)
    org_id = models.CharField(max_length=30, blank=True, null=True)
    dict = models.BigIntegerField(blank=True, null=True)
    std_code = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_org_dict'


class TPaymentOrgParamDef(models.Model):
    param_code = models.CharField(max_length=100)
    org_id = models.CharField(max_length=30)
    title = models.CharField(max_length=250, blank=True, null=True)
    vtype = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payment_org_param_def'
        unique_together = (('param_code', 'org_id'),)


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


class TPaymentUser(models.Model):
    user_id = models.CharField(max_length=50)
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
        unique_together = (('user_id', 'user_type'),)


class TPayorgSettleConfig(models.Model):
    config_id = models.FloatField(primary_key=True)
    pay_org_code = models.CharField(max_length=30)
    start_date = models.CharField(max_length=8)
    end_date = models.CharField(max_length=8)
    settle_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 't_payorg_settle_config'


class TPayorgSucRateMon(models.Model):
    mon_id = models.BigIntegerField()
    stat_time = models.CharField(max_length=12)
    pay_org_code = models.CharField(max_length=30)
    pay_org_alias = models.CharField(max_length=100)
    pay_com_alias = models.CharField(max_length=50, blank=True, null=True)
    page_notify_suc_rate = models.FloatField(blank=True, null=True)
    backend_notify_suc_rate = models.FloatField(blank=True, null=True)
    order_suc_rate = models.FloatField(blank=True, null=True)
    comparison_date = models.CharField(max_length=8, blank=True, null=True)
    comparison_suc_rate = models.FloatField(blank=True, null=True)
    suc_rate_dif = models.FloatField(blank=True, null=True)
    dif_threshold = models.FloatField(blank=True, null=True)
    alarm = models.BigIntegerField(blank=True, null=True)
    pay_log_num = models.BigIntegerField(blank=True, null=True)
    pay_log_suc_num = models.BigIntegerField(blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    audit_start_time = models.CharField(max_length=12, blank=True, null=True)
    audit_end_time = models.CharField(max_length=12, blank=True, null=True)
    auidt_task_info = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_payorg_suc_rate_mon'


class TProvince(models.Model):
    province_code = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_province'


class TReversalLogs(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    reversal_batch_no = models.CharField(max_length=18, blank=True, null=True)
    reversal_channel = models.BigIntegerField(blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_log_time = models.CharField(max_length=14, blank=True, null=True)
    payment_log_id = models.BigIntegerField(blank=True, null=True)
    payment_order_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_trans_id = models.CharField(max_length=100, blank=True, null=True)
    reverse_request_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_status = models.BigIntegerField(blank=True, null=True)
    reversal_failed_reason = models.CharField(max_length=250, blank=True, null=True)
    order_amount = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    surplus_amount = models.BigIntegerField(blank=True, null=True)
    reversal_phone = models.CharField(max_length=250, blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reversal_logs'


class TRoundLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    scale_id = models.BigIntegerField(blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    company_code = models.CharField(max_length=30, blank=True, null=True)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    create_reason = models.CharField(max_length=100, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    create_date = models.CharField(max_length=8, blank=True, null=True)
    expected_trans_num = models.BigIntegerField(blank=True, null=True)
    round_trans_num = models.BigIntegerField(blank=True, null=True)
    round_trans_amount = models.BigIntegerField(blank=True, null=True)
    total_trans_num = models.BigIntegerField(blank=True, null=True)
    total_trans_amount = models.BigIntegerField(blank=True, null=True)
    round_order_no = models.CharField(max_length=30, blank=True, null=True)
    rate_order_no = models.BigIntegerField(blank=True, null=True)
    round_end_flag = models.BigIntegerField(blank=True, null=True)
    round_choose_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_round_log'


class TRoundLogHistory(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    scale_id = models.BigIntegerField(blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    company_code = models.CharField(max_length=30, blank=True, null=True)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    create_reason = models.CharField(max_length=100, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    create_date = models.CharField(max_length=8, blank=True, null=True)
    expected_trans_num = models.BigIntegerField(blank=True, null=True)
    round_trans_num = models.BigIntegerField(blank=True, null=True)
    round_trans_amount = models.BigIntegerField(blank=True, null=True)
    total_trans_num = models.BigIntegerField(blank=True, null=True)
    total_trans_amount = models.BigIntegerField(blank=True, null=True)
    round_order_no = models.CharField(max_length=30, blank=True, null=True)
    rate_order_no = models.BigIntegerField(blank=True, null=True)
    round_end_flag = models.BigIntegerField(blank=True, null=True)
    round_choose_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_round_log_history'


class TSession(models.Model):
    token = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()
    last_update_time = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_session'


class TShortUrlToken(models.Model):
    token = models.CharField(primary_key=True, max_length=10)
    payment_order_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=30)
    service_id = models.CharField(max_length=30)
    create_time = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_short_url_token'


class TSubColumn(models.Model):
    sub_column_id = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sub_column'


class TSucRateThrConfig(models.Model):
    config_id = models.BigIntegerField(primary_key=True)
    pay_org_code = models.CharField(max_length=30)
    suc_rate_dif_trh = models.FloatField()
    min_suc_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 't_suc_rate_thr_config'


class TSysParam(models.Model):
    param_code = models.CharField(primary_key=True, max_length=50)
    param_name = models.CharField(max_length=100, blank=True, null=True)
    param_value = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_param'


class TTactics(models.Model):
    tactics_code = models.CharField(primary_key=True, max_length=50)
    tactics_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tactics'


class TTacticsMsisdn(models.Model):
    tactics_code = models.CharField(max_length=50)
    msisdn = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_tactics_msisdn'
        unique_together = (('tactics_code', 'msisdn'),)


class TTacticsPaymentOrg(models.Model):
    tactics_payment_org_id = models.BigIntegerField(primary_key=True)
    tactics_code = models.CharField(max_length=50, blank=True, null=True)
    pay_org_id = models.CharField(max_length=50, blank=True, null=True)
    pay_channel_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tactics_payment_org'


class TUserChannelMerchant(models.Model):
    user_id = models.CharField(max_length=32)
    channel_id = models.CharField(max_length=30)
    rcv_user_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_user_channel_merchant'
        unique_together = (('user_id', 'channel_id', 'rcv_user_id'),)


class TUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    f_name = models.CharField(max_length=20)
    age = models.BigIntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_users'


class Tmp01(models.Model):
    city_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tmp_01'


class TmpTPaymentOrder(models.Model):
    payment_order_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    rcv_user_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_user_type = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_time = models.CharField(max_length=14, blank=True, null=True)
    order_url = models.CharField(max_length=250, blank=True, null=True)
    back_url = models.CharField(max_length=250, blank=True, null=True)
    pay_failed_op = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    paid_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    pay_cny_status = models.BigIntegerField(blank=True, null=True)
    pay_points_status = models.BigIntegerField(blank=True, null=True)
    reversal_cny_status = models.BigIntegerField(blank=True, null=True)
    reversal_points_status = models.BigIntegerField(blank=True, null=True)
    topup_no = models.CharField(max_length=32, blank=True, null=True)
    topup_type = models.BigIntegerField(blank=True, null=True)
    delivery_status = models.BigIntegerField(blank=True, null=True)
    delivery_time = models.CharField(max_length=14, blank=True, null=True)
    delivery_error_code = models.CharField(max_length=50, blank=True, null=True)
    notify_status = models.BigIntegerField(blank=True, null=True)
    notify_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_reason = models.CharField(max_length=250, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    notify_url = models.CharField(max_length=250, blank=True, null=True)
    digest = models.CharField(max_length=250, blank=True, null=True)
    required_payment_methods = models.CharField(max_length=250, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    paid_success_num = models.BigIntegerField(blank=True, null=True)
    reversed_time = models.CharField(max_length=14, blank=True, null=True)
    direct_flag = models.BigIntegerField(blank=True, null=True)
    pay_timeout = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    reserve1 = models.CharField(max_length=128, blank=True, null=True)
    reversal_notify_url = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    cashier_desk_type = models.BigIntegerField(blank=True, null=True)
    login_flag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_t_payment_order'


class TmpTRoundLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    intelligent_channel_id = models.BigIntegerField(blank=True, null=True)
    scale_id = models.BigIntegerField(blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    company_code = models.CharField(max_length=30, blank=True, null=True)
    bank_code = models.CharField(max_length=30, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    create_reason = models.CharField(max_length=100, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    create_date = models.CharField(max_length=8, blank=True, null=True)
    expected_trans_num = models.BigIntegerField(blank=True, null=True)
    round_trans_num = models.BigIntegerField(blank=True, null=True)
    round_trans_amount = models.BigIntegerField(blank=True, null=True)
    total_trans_num = models.BigIntegerField(blank=True, null=True)
    total_trans_amount = models.BigIntegerField(blank=True, null=True)
    round_order_no = models.CharField(max_length=30, blank=True, null=True)
    rate_order_no = models.BigIntegerField(blank=True, null=True)
    round_end_flag = models.BigIntegerField(blank=True, null=True)
    round_choose_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_t_round_log'


class Tp1(models.Model):
    payment_order_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    channel_id = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=50)
    user_type = models.BigIntegerField()
    pay_user_id = models.CharField(max_length=50)
    pay_user_type = models.BigIntegerField()
    rcv_user_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_user_type = models.BigIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_time = models.CharField(max_length=14, blank=True, null=True)
    order_url = models.CharField(max_length=250, blank=True, null=True)
    back_url = models.CharField(max_length=250, blank=True, null=True)
    pay_failed_op = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    cny_amount = models.BigIntegerField(blank=True, null=True)
    points_amount = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    create_time = models.CharField(max_length=14, blank=True, null=True)
    pay_request_time = models.CharField(max_length=14, blank=True, null=True)
    modify_time = models.CharField(max_length=14, blank=True, null=True)
    paid_time = models.CharField(max_length=14, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    pay_error_code = models.CharField(max_length=100, blank=True, null=True)
    pay_cny_status = models.BigIntegerField(blank=True, null=True)
    pay_points_status = models.BigIntegerField(blank=True, null=True)
    reversal_cny_status = models.BigIntegerField(blank=True, null=True)
    reversal_points_status = models.BigIntegerField(blank=True, null=True)
    topup_no = models.CharField(max_length=32, blank=True, null=True)
    topup_type = models.BigIntegerField(blank=True, null=True)
    delivery_status = models.BigIntegerField(blank=True, null=True)
    delivery_time = models.CharField(max_length=14, blank=True, null=True)
    delivery_error_code = models.CharField(max_length=50, blank=True, null=True)
    notify_status = models.BigIntegerField(blank=True, null=True)
    notify_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_time = models.CharField(max_length=14, blank=True, null=True)
    reversal_reason = models.CharField(max_length=250, blank=True, null=True)
    pay_org_id = models.CharField(max_length=30, blank=True, null=True)
    pay_account_id = models.CharField(max_length=50, blank=True, null=True)
    pay_account_name = models.CharField(max_length=100, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)
    rcv_account_name = models.CharField(max_length=100, blank=True, null=True)
    notify_url = models.CharField(max_length=250, blank=True, null=True)
    digest = models.CharField(max_length=250, blank=True, null=True)
    required_payment_methods = models.CharField(max_length=250, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    settle_date = models.CharField(max_length=8, blank=True, null=True)
    audit_time = models.CharField(max_length=14, blank=True, null=True)
    audit_status = models.BigIntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=32, blank=True, null=True)
    reversal_user_id = models.CharField(max_length=100, blank=True, null=True)
    reversal_user_name = models.CharField(max_length=100, blank=True, null=True)
    reversal_client_ip = models.CharField(max_length=50, blank=True, null=True)
    reversal_type = models.BigIntegerField(blank=True, null=True)
    paid_num = models.BigIntegerField(blank=True, null=True)
    paid_success_num = models.BigIntegerField(blank=True, null=True)
    reversed_time = models.CharField(max_length=14, blank=True, null=True)
    direct_flag = models.BigIntegerField(blank=True, null=True)
    pay_timeout = models.BigIntegerField(blank=True, null=True)
    reversal_amount = models.BigIntegerField(blank=True, null=True)
    reserve1 = models.CharField(max_length=128, blank=True, null=True)
    reversal_notify_url = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    settle_rate = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    cashier_desk_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tp1'


class Tp123(models.Model):
    id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tp123'


class Tp201312(models.Model):
    order_id = models.CharField(max_length=100, blank=True, null=True)
    flag = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tp201312'


class Tp1001User(models.Model):
    user_id = models.CharField(max_length=50)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    zftime = models.DateField(blank=True, null=True)
    tztime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tp_1001_user'


class TpChannel(models.Model):
    channel_id = models.CharField(max_length=30)
    title = models.CharField(max_length=50, blank=True, null=True)
    jishu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tp_channel'


class TpChoujin(models.Model):
    log_id = models.BigIntegerField()
    org_id = models.CharField(max_length=30, blank=True, null=True)
    audit_date = models.CharField(max_length=8)
    audit_time = models.CharField(max_length=14)
    status = models.BigIntegerField()
    fee_settle_status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'tp_choujin'


class TpFlagOrder(models.Model):
    payment_order_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tp_flag_order'


class Tpydjh(models.Model):
    id = models.FloatField(blank=True, null=True)
    order_date = models.CharField(max_length=8, blank=True, null=True)
    rcv_account_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpydjh'
