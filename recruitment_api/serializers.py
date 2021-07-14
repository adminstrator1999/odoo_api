from rest_framework import serializers

from odoo_api.settings import SURVEY_BASE_URL

from .models import HrJob, SurveySurvey, HrDepartment


class HrDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = HrDepartment
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    survey_url = serializers.SerializerMethodField()

    class Meta:
        model = SurveySurvey
        fields = ['id', 'title', 'access_token', 'survey_url']

    def get_survey_url(self, obj):
        return f"{SURVEY_BASE_URL}/{obj.access_token}"


class HrJobSerializer(serializers.ModelSerializer):
    survey = SurveySerializer()
    department = HrDepartmentSerializer()

    class Meta:
        model = HrJob
        fields = '__all__'
