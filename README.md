# Criar um ambiente virtual 

1. Criar o ambiente com:
'''
$ pip3 install -U virtualenv
$ python3 -m virtualenv venv
'''

2. Ativar o ambiente:
'''sh
$ source venv/bin/activate
'''

3. Instalar o Flask
'''sh
pip install flask
'''

- Montei uma página de cadastro com nome e RG e ambos deixei como required no HTML para que o usuário não consiga enviar sem as informações solicitadas.
<img width="549" alt="Captura de Tela 2024-03-21 às 15 02 58" src="https://github.com/Jullyhein/estudyweb/assets/97550028/e2f90082-f4e5-40f0-b3be-9ad325514dd4">



- E no código python para verificar no backend o andamento da minha solicitação peço para imprimir um dicionário para que possa imprimir o resultado no terminal. 
<img width="500" alt="Captura de Tela 2024-03-21 às 15 03 59" src="https://github.com/Jullyhein/estudyweb/assets/97550028/65bd1cff-cb89-4ea9-9c6c-c49b0eaed41e">



- Assim que o usuário inserisse as informações solicitadas o servidor também mandaria uma mensagem para ele avisando que foi feito com sucesso. 
- Deixo aqui também o inspecionar para visualizar o POST das informções, e colocamos no POST para não ter vazamento de informações dentro da URL com GET. 
<img width="1618" alt="Captura de Tela 2024-03-21 às 15 05 20" src="https://github.com/Jullyhein/estudyweb/assets/97550028/d0502a93-17b3-4821-aea4-0110c07f7b99">



