#from django.db import models

# Create your models here.
from django.contrib.gis.db import models


# from django.conf import settings

# Create your models here.
# class myPolygon(models.Model):
#    geom = models.PolygonField()

# Create your models here.

class supervisor(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    #position=models.PointField(null=True)
    

    supervisor_id=models.CharField(max_length=100,null=True, unique=True)
    # client = models.ForeignKey(client, on_delete=models.CASCADE, null=True, related_name='%(class)s_related')

    image=models.ImageField(null=True)
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    

class client(models.Model):
    nom=models.CharField(max_length=100,null=True,blank=True)
    prenom=models.CharField(max_length=100,null=True,blank=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    image=models.ImageField(null=True)

    client_id=models.CharField(max_length=100,null=True, unique=True)

    supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE, null=True, related_name='%(class)s_related')

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    #position=models.PointField(null=True)
    image=models.ImageField(null=True)
    def __str__(self):
        return f"{self.prenom} {self.nom}"