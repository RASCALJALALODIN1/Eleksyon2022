from django.db.models import fields
from django.forms import ModelForm
from .models import votes 

class voteform(ModelForm):
    class Meta:
        model= votes
        fields = ['fname', 'mname', 'sname', 'age', 'rvote', 'region', 'pnum', 'pres', 'vpres', 'political_party']
