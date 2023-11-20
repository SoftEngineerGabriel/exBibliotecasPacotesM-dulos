#9. Importe o pacote requests e faça uma requisição HTTP para um URL e exiba o código de status.

import requests

url = "https://www.google.com"

r = requests.get(url)

print(r.status_code)