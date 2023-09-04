from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Casa(models.Model):
    id = models.AutoField(verbose_name="ID_Casa", primary_key=True, editable=False)
    nome = models.CharField(verbose_name="Nome", max_length=255, null=False, blank=False, unique=True, help_text="Nome da Casa")
    logo = models.ImageField(verbose_name="Logo da Casa", upload_to="media/", max_length=200, null=True, blank=True, help_text="Imagem do Personagem")
    
    def __str__(self):
        return self.nome

class Varinha(models.Model):
    id = models.UUIDField(verbose_name="ID_Varinha", primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(verbose_name="Descrição", max_length=255, null=False, blank=False, help_text="Descrição da Varinha")
    madeira = models.ForeignKey('Madeira', verbose_name="Madeira", on_delete=models.CASCADE, null=False, blank=False, help_text="Madeira da Varinha")
    nucleo = models.ForeignKey('Nucleo', verbose_name="Núcleo", on_delete=models.CASCADE, null=False, blank=False, help_text="Núcleo da Varinha")
    tamanho = models.ForeignKey('Tamanho', verbose_name="Tamanho", on_delete=models.CASCADE, null=False, blank=False, help_text="Tamanho da Varinha")
    
    def __str__(self):
        return self.descricao

class Madeira(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    descricao = models.CharField(verbose_name="Descrição", max_length=255, null=False, blank=False, help_text="Descrição da Madeira")

    def __str__(self):
        return self.descricao
    
    
class Nucleo(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    descricao = models.CharField(verbose_name="Descrição", max_length=255, null=False, blank=False, help_text="Descrição do Núcleo")

    def __str__(self):
        return self.descricao
    

class Tamanho(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    nome = models.CharField(verbose_name="Nome", max_length=3, null=False, blank=False, unique=True, help_text="Nome do Tamanho")
    descricao = models.CharField(verbose_name="Descrição", max_length=255, null=False, blank=False, help_text="Descrição do Tamanho")
    
    def __str__(self):
        return self.nome
    

class Animal(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    nome = models.CharField(verbose_name="Nome", max_length=255, null=False, blank=False, unique=True, help_text="Nome do Animal")
    descricao = models.CharField(verbose_name="Descrição", max_length=255, null=False, blank=False, help_text="Descrição do Animal")

    def __str__(self):
        return self.nome
    

class Aluno(models.Model):
    id = models.UUIDField(verbose_name="ID_Aluno", primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(verbose_name="Nome", max_length=255, null=False, blank=False, unique=True, help_text="Nome do Aluno")
    casa = models.ForeignKey(Casa, to_field='id',verbose_name="Casa", on_delete=models.DO_NOTHING, null=False, blank=False, help_text="Casa do Aluno")   
    varinha = models.ForeignKey(Varinha, verbose_name="Varinha", on_delete=models.DO_NOTHING, null=False, blank=False, help_text="Varinha do Aluno")
    animal = models.ForeignKey(Animal, to_field='id',verbose_name="Animal", on_delete=models.DO_NOTHING, null=False, blank=False, help_text="Animal do Aluno")
    usuario = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, null=True, blank=True, help_text="Usuário do Aluno")
    
    def __str__(self):
        return self.nome

class Personagem(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255, null=False, blank=False, unique=True, help_text="Nome do Personagem")
    descricao = models.TextField(verbose_name="Descrição", max_length=2048, null=False, blank=False, help_text="Descrição do Personagem")
    imagem = models.ImageField(verbose_name="Imagem", upload_to='media/', null=False, blank=False, help_text="Imagem do Personagem")
    
    def __str__(self):
        return self.nome