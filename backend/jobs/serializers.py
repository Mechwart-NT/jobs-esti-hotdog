from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Job

class JobSerializer(ModelSerializer):
    languages = SerializerMethodField()
    tools = SerializerMethodField()

    def get_languages(self, job):
        return list(job.languages.values_list("name", flat=True))

    def get_tools(self, job):
        return list(job.tools.values_list("name", flat=True))

    class Meta:
        model = Job
        fields = "__all__"
