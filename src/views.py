from django.shortcuts import render
from django.http import HttpResponse
#from .models import Usuario
#from .models import Perfil
from django.db import connection
from collections import namedtuple
from django.template import loader

def index(request):
    return HttpResponse("MAC0350: EP3")
    
def query1(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM paciente')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('query1.html')
    context = {'query1_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query2(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM exame')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('query2.html')
    context = {'query2_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query3(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM amostra')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('query3.html')
    context = {'query3_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query4(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM Paciente_Exame_Amostra')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('query4.html')
    context = {'query4_result_list': result,}
    
    return HttpResponse(template.render(context, request))
#metodos auxiliares

def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    result = [nt_result(*row) for row in cursor.fetchall()]

    return result

