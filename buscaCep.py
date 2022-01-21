#Author: Edson Marciano Rodrigues Padilha

from time import sleep
import requests

cep = int(input("🔎 Digite um cep: "))

while True:    
    
    if cep == 0:
        print('Saindo do buscador...🚀')
        sleep(2)
        print('Você saiu do sistema.')
        exit()
    
    elif cep != int:
        print('Somente números...')

    elif len(cep) != 8:
        print("Quantidades de digítos inválida!")
        

    url = requests.get(f"http://viacep.com.br/ws/{cep}/json/")

    {
        "Accept":"application/json",
        "Content-Type": "application/json"
    }

    resp = url
    sts = url.status_code

    if sts == 200:
        print(sts, " - Conexão estabelecida! 🟢")
        print(f"O endereço é: \n", resp.text)

    elif sts == 400:
        print(sts, ' - Requisição diferente do esperado!!! 🟠')

    elif sts == 404:
        print(sts , ' - Página não encontrada! 🔴')

    else:
        print("Verifique as opções de entrada...")

    cep = int(input("🔎 Digite um cep: "))
    
    