from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


@api_view(['GET'])
def job_stats(request):
    count = cache.get("job_count")
    if count is None:
        count = Job.objects.count()
        cache.set("job_count", count, timeout=60)  # cache for 1 min
    return Response({"total_jobs": count})