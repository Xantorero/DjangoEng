from django.db import models

# Create your models here.
class Match(models.Model):
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    alg1_goals = models.IntegerField(default=0)
    alg2_goals = models.IntegerField(default=0)
    alg3_goals = models.IntegerField(default=0)
    alg4_goals = models.IntegerField(default=0)
    alg5_goals = models.IntegerField(default=0)
    alg6_goals = models.IntegerField(default=0)
    alg7_goals = models.IntegerField(default=0)
    alg8_goals = models.IntegerField(default=0)
    
    def __str__(self):
        return self.home_team +" - "+ self.away_team
    


