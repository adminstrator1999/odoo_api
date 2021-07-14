from rest_framework.generics import ListAPIView

from .models import HrJob
from .serializers import HrJobSerializer


class HrAPIView(ListAPIView):
    queryset = HrJob.objects.all()
    serializer_class = HrJobSerializer
    filter_fields = ['state', ]
