from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Job
from .serializers import JobSerializer

@api_view(["GET"])
def getJobs(request):
    jobs = Job.objects.all()
    serialized = JobSerializer(jobs, many=True)
    return Response(serialized.data)
