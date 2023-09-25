from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:pink">FYVF_Evaluacion1</h1>
    """
    return HttpResponse(html)