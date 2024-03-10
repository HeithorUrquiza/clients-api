from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF informado é inválido'})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não poder haver número ou caracteres especiais no nome'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve conter 9 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve seguir o padrão (DD) 91234-1234'})
        
        return data
    
    
    class Meta:
        model = Cliente
        fields = '__all__'
    