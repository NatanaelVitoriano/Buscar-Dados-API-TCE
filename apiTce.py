import requests
import os
from pathlib import Path
print("Informe o numero do municipio: ")
codigoDoMunicipio = str(input())
rContratos = requests.get('https://api-dados-abertos.tce.ce.gov.br/contrato?codigo_municipio=' + codigoDoMunicipio + '&data_contrato=2010-01-01_2023-12-31&quantidade=0&deslocamento=0')
rLicitacao = requests.get('https://api-dados-abertos.tce.ce.gov.br/licitacoes?codigo_municipio=' + codigoDoMunicipio + '&data_realizacao_autuacao_licitacao=2010-01-01_2023-12-31')
listaDeLicitacoesTxt = []
listaDeContratosTxt = []

def licitacao():
    json = rLicitacao.json()
    listaDelicitacoes = json['data']

    i = len(listaDelicitacoes) 
    for x in range(i):
        licitacao = listaDelicitacoes[x]
        listaDeLicitacoesTxt.append(licitacao['numero_licitacao'])
        print("Licitacao: " + listaDeLicitacoesTxt[x])

    listagemDeLicitacoes = Path("C:/Users/Supor/Desktop/licitacoes.txt")
    listagemDeLicitacoes.write_text("\n".join(listaDeLicitacoesTxt))


def contrato():
    json = rContratos.json()
    listaDeContratos = json['data']

    i = len(listaDeContratos) 
    for x in range(i):
        contratos = listaDeContratos[x]
        listaDeContratosTxt.append(contratos['numero_contrato'])
        print("Contrato: " + listaDeContratosTxt[x])

    listagemDeContratos = Path("C:/Users/Supor/Desktop/contratos.txt")
    listagemDeContratos.write_text("\n".join(listaDeContratosTxt))

licitacao()
contrato()

os.system('cls' if os.name == 'nt' else 'clear')
print(str(len(listaDeLicitacoesTxt)) + " licitações importadas")
print(str(len(listaDeContratosTxt)) + " contratos importados")
os.system("PAUSE")
