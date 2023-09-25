from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaDos(request):
    html="""
    <h1 style="color:purple">FYVF_Evaluacion1</h1>
    """
    return HttpResponse(html)