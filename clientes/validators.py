import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido( nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    padrao = '[0-9]{2} 9[0-9]{4}-[0-9]{4}'
    return re.match(padrao, celular)
            