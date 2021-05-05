from telnetlib import KERMIT

from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text


class TestCase(models.Model):
    name = models.CharField(max_length=200, unique=True)
    service = models.CharField(max_length=200)
    instance = models.CharField(max_length=10, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "id : {}, name : {}".format(self.id, self.name)


class KeyModel(models.Model):
    key = models.CharField(max_length=50, primary_key=True, null=False)
    test_case = models.ForeignKey(to='params.TestCase', on_delete=models.CASCADE)
    label = models.TextField(max_length=250, null=False)

    def __str__(self):
        return self.key


class Server(models.Model):
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=100)


class CheckFlowParams(KeyModel):
    flow_application_code = models.CharField(max_length=50, null=False)
    server = models.ForeignKey(to='params.Server', null=False, on_delete=models.CASCADE)
    status_to_check = models.CharField(choices=[('20', '20'), ('23', '23'), ('30', '30')], max_length=2)
    expected_files = models.BooleanField(default=False, null=False)


class CleanFlowParams(KeyModel):
    flow_application_code = models.CharField(max_length=50, null=False)


class DeclareFlowParams(models.Model):
    flow_application_code = models.CharField(max_length=50, null=False)
    flow_agent = models.CharField(max_length=50, null=False)
    dir_path = models.FilePathField(allow_folders=True, allow_files=False, null=False)
    file_name = models.CharField(max_length=50, null=False)


class ExtractTableParams(KeyModel):
    spool_file = models.CharField(max_length=300, null=False)
    log_file = models.CharField(max_length=300, null=False)
    sql_file = models.CharField(max_length=300, null=False)
    table_ref = models.CharField(max_length=50, null=False)


class LoadTableParams(KeyModel):
    data_file = models.CharField(max_length=300)
    log_file = models.CharField(max_length=300)
    ctl_file = models.CharField(max_length=300)


class RunOracleActionParams(models.Model):
    key = models.CharField(max_length=50, primary_key=True, null=False)
    log_file = models.CharField(max_length=300)
    sql_file = models.CharField(max_length=300)
    label = models.TextField(max_length=250, null=False)


class RunScriptParams(models.Model):
    key = models.CharField(max_length=50, primary_key=True, null=False)
    script_directory = models.CharField(max_length=300, null=False)
    content_to_launch = models.CharField(max_length=300, null=False)
    label = models.TextField(max_length=250, null=False)


class UpdateStateIdParams(models.Model):
    key = models.CharField(max_length=50, primary_key=True, null=False)
    process_date = models.DateField(null=False)
    process_status = models.CharField(max_length=300, null=True)
    label = models.TextField(max_length=250, null=False)


class CompareParams(KeyModel):
    expected = models.CharField(max_length=300, null=False)
    outgoing = models.CharField(max_length=300, null=False)