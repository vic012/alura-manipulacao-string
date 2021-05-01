import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
#Se não encontrar nada retorna none
match = padrao_url.match(url)

if not match:
	raise ValueError("A URL é inválida.")
else:
	print("A URL é válida")