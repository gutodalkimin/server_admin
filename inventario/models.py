from django.db import models

class Servidor(models.Model):
    hostname = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    sistema_operacional = models.CharField(max_length=100)
    localizacao = models.CharField(
        max_length=20,
        choices=[
            ('Lever', 'Lever'),
            ('Ramalde', 'Ramalde'),
            ('Gaia', 'Gaia')
        ]
    )
    backup = models.CharField(
        max_length=20,
        choices=[
            ('Baixo', 'Baixo'),
            ('Medio', 'Medio'),
            ('Alto', 'Alto'),
            ('Sem Backup', 'Sem Backup')
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Ativo', 'Ativo'),
            ('A Fazer', 'A Fazer'),
            ('Lixo', 'Lixo')
        ]
    )
    update = models.CharField(
        max_length=20,
        choices=[
            ('CRIT', 'CRIT'),
            ('PROD', 'PROD'),
            ('HOMU', 'HOMU'),
            ('Sem Update', 'Sem Update')
        ]
    )
    data_inclusao = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.hostname
