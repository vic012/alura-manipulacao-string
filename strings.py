#Fatiamento e índices de strings
'''sobreMim = "Meu nome é Pedro e minha idade é 26"
print(sobreMim[-2:])'''

url = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
argumento = "moedaorigem=real"

#Método find
index = argumento.find("=")
substring = argumento[index + 1:]
print(substring)
#Método Split, separa texto por separadores informados
lista = argumento.split("=")
print(lista)