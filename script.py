"""------------------------------------------------------------------------------------------------------"""

# Este método envia uma solicitação get para o Scotch.io.
# Este tipo de solicitação também é feito pelo navegador ao acessar a página.
# A biblioteca Requests não consegue processas as páginas em HTML (diferente do navegador)
# No lugar de processar a página, será recebido apenas o HTML bruto e informações de respostas.

# O Requests permite também utilizar outrsa funções como: .post() e .put()

"""------------------------------------------------------------------------------------------------------"""

import requests #importa a biblioteca requests no python
res = requests.get('https://yuridasilva1704.github.io/ML/')
print(res)
print(res.status_code) # Apenas demonstra o código de resposta

"""------------------------------------------------------------------------------------------------------"""

"No CMD - Prompt de Comando"
# Acessa o diretório onde está o script, e executa:
# Para um script com nome "script.py"
# > script.py

# Os códigos HTTP variam de 1XX a 5XX. Códigos mais comuns são: 200, 404 e 500.

# 1XX - Informação
# 2XX - Sucesso
# 3XX - Redirecionar
# 4XX - Erro de cliente (você cometeu um erro)
# 5XX - Erro de servidor (eles cometeram um erro)

"""------------------------------------------------------------------------------------------------------"""

"Realização de testes para verificar se está tudo ok"
if res:
    print("Response OK")
else:
    print("Response Failed")
"""------------------------------------------------------------------------------------------------------"""

"CABEÇALHOS"
# É possível obter resposta dos cabeçalhos. Tratam-se de como o servidor consegue processar
#e interpretar ps dados que estão sendo enviados e recebidos na solicitação/resposta. 

print(res.headers)
