from rest_framework import serializers
from .models import GeneticTest


class GeneticTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneticTest
        fields = (
            'id',
            'animal_name',
            'species',
            'test_date',
            'milk_yield',
            'health_status',
            'created_at',
        )

class GeneticTestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneticTest
        fields = (
            'animal_name',
            'species',
            'test_date',
            'milk_yield',
            'health_status',
        )

    def validate_animal_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Поле 'animal_name' должно быть строкой.")
        return value

    def validate_species(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Поле 'species' должно быть строкой.")
        return value


    def validate_milk_yield(self, value):
        if value < 0:
            raise serializers.ValidationError("Поле 'milk_yield' не может быть отрицательным.")
        return value


class StatisticsSerializer(serializers.Serializer):
    species = serializers.CharField(max_length=100)
    total_tests = serializers.IntegerField()
    avg_milk_yield = serializers.FloatField()
    max_milk_yield = serializers.FloatField()
    good_health_percentage = serializers.FloatField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['avg_milk_yield'] = round(data['avg_milk_yield'], 2)
        data['max_milk_yield'] = round(data['max_milk_yield'], 2)
        data['good_health_percentage'] = round(data['good_health_percentage'], 2)
        return data
