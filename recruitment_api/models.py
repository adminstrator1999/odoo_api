from django.db import models


class HrDepartment(models.Model):
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_department'


class SurveySurvey(models.Model):
    title = models.CharField(max_length=255)
    access_token = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_survey'


class HrJob(models.Model):
    name = models.CharField(max_length=255)
    expected_employees = models.IntegerField(blank=True, null=True)
    no_of_employee = models.IntegerField(blank=True, null=True)
    no_of_recruitment = models.IntegerField(blank=True, null=True)
    no_of_hired_employee = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=10)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'department'),)
