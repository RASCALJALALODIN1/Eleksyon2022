from django.db import models


class Voter(models.Model):
	fname = models.CharField(max_length=150, null=True,blank=False)
	mname = models.CharField(max_length=150, null=True,blank=False)
	sname = models.CharField(max_length=150, null=True,blank=False)
	voters_stub = models.CharField(max_length=150, null=True,blank=False)

class votes(models.Model):
	fname = models.CharField(max_length=150, blank=False)
	mname = models.CharField(max_length=150, blank=False)
	sname = models.CharField(max_length=150, blank=False)
	age = models.CharField(max_length=150, blank=False)
	rvote = models.CharField(max_length=150, blank=False)
	region = models.CharField(max_length=150, blank=False)
	pnum = models.CharField(max_length=150, null = True, blank=False)
	pres = models.CharField(max_length=150,  blank=False)
	vpres = models.CharField(max_length=150,  blank=False)
	political_party = models.CharField(max_length=150, blank=False)
class numvotes(models.Model):
	cavite = models.CharField(max_length=150, blank=False)
	batangas = models.CharField(max_length=150, blank=False)
	laguna = models.CharField(max_length=150, blank=False)
	rizal = models.CharField(max_length=150, blank=False)
	qprov = models.CharField(max_length=150, blank=False)










	


