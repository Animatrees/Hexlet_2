from django.db.models import Count, Avg, Max, Q, F
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import GeneticTestSerializer, StatisticsSerializer, GeneticTestCreateSerializer
from .models import GeneticTest
from rest_framework.response import Response


class TestListAPIView(generics.ListCreateAPIView):
    queryset = GeneticTest.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['species']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GeneticTestCreateSerializer
        return GeneticTestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            {"message": "Данные успешно добавлены", "id": instance.id},
            status=status.HTTP_201_CREATED
        )


class TestDetailAPIView(generics.RetrieveAPIView):
    queryset = GeneticTest.objects.all()
    serializer_class = GeneticTestSerializer


class StatisticsView(APIView):
    def get(self, request):
        stats = GeneticTest.objects.values('species').annotate(
            total_tests=Count('id'),
            avg_milk_yield=Avg('milk_yield'),
            max_milk_yield=Max('milk_yield'),
            good_health_count=Count('id', filter=Q(health_status='good')),
            total_health_count=Count('id')
        ).annotate(
            good_health_percentage=Coalesce(
                (100.0 * F('good_health_count') / F('total_health_count')),
                0.0
            )
        )
        serializer = StatisticsSerializer(stats, many=True)
        return Response({"statistics": serializer.data})
