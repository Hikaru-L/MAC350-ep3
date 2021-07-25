from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
from django.template import loader

def index(request):
    return HttpResponse("MAC0350: EP3")
    
def pacientes(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ep3_paciente')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('pacientes.html')
    context = {'pacientes_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def exames(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ep3_exame')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('exames.html')
    context = {'exames_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def amostras(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ep3_amostra')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('amostras.html')
    context = {'amostras_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def relations(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ep3_Paciente_Exame_Amostra')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('relations.html')
    context = {'relations_result_list': result,}
    
    return HttpResponse(template.render(context, request))
#metodos auxiliares

def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    result = [nt_result(*row) for row in cursor.fetchall()]

    return result

