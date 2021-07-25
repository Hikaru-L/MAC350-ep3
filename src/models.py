from django.db import models
    
class paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    nascimento = models.DateField()
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['cpf'], name='unique_cpf')
                ]

    def __str__(self):
        return self.nome

class exame(models.Model):
    id_exame = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255)
    virus = models.CharField(max_length=255)
    id_paciente = models.ForeignKey(paciente, on_delete=models.PROTECT)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['tipo'], name='unique_tipo'),
                models.UniqueConstraint(fields=['virus'], name='unique_virus')
                ]

    def __str__(self):
        return self.id_exame

class amostra(models.Model):
    id_amostra = models.IntegerField(primary_key=True)
    codigo_amostra = models.CharField(max_length=255)
    metodo_de_coleta = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['codigo_amostra'], name='unique_codigo_amostra')
                ]

    def __str__(self):
        return self.codigo_amostra


class paciente_exame_amostra(models.Model):
    id_paciente = models.ForeignKey(paciente, on_delete=models.PROTECT)
    id_amostra = models.ForeignKey(amostra, on_delete=models.PROTECT)
    id_exame = models.ForeignKey(exame, on_delete=models.PROTECT)
    data_de_realizacao = models.DateField()
    data_de_solicitacao = models.DateField()
    
    class Meta:
        #not sure if this is right
        constraints = [
                models.UniqueConstraint(fields=['id_paciente', 'id_amostra', ' id_exame', 'data_de_realizacao'], name='unique_id_paciente_amostra_exame')
                ]


