#Fatiamento e índices de strings

url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

#Procura pelo caractere ?
indice = url.find("?")

url_base = url[:indice]
#print(url_base)

url_parametros = url[indice + 1:]
#print(url_parametros)

busca = 'moedaOrigem'
indice_parametro = url_parametros.find(busca)
indice_valor = indice_parametro + len(busca) + 1
valor = url_parametros[indice_valor:]
print(valor)