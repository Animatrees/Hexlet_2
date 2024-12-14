from django.db import models

class GeneticTest(models.Model):
    animal_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    test_date = models.DateField()
    milk_yield = models.FloatField()
    health_status = models.CharField(max_length=4, choices=[('good', 'Good'), ('poor', 'Poor')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "genetic_tests"

    def __str__(self):
        return self.animal_name
