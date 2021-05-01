endereco = "Rua DOmingos Afonos 72, apartamento 150, Angelim, Sousa, Paraíba, 58801-680"
#ou endereco = "Rua DOmingos Afonos 72, apartamento 150, Angelim, Sousa, Paraíba, 58801680"

import re #Regular Expression == RegEx

# 5 dígiots + hifen (Opcional) + 3 dígitos
#rastreia padrões em uma expressão regular
#Para informar que um caráctere é opcional eu coloco uma ? depois do caractere
'''padrao = re.compile(
	"[0123456789]"
	"[0123456789]"
	"[0123456789]"
	"[0123456789]"
	"[0123456789][-]?"
	"[0123456789]"
	"[0123456789]"
	"[0123456789]"
	)'''
#Aprendendo quantificadores
#{numero} indica quantas vezes aquele padrão pode acontecer em seguida
padrao = re.compile(
	#"[0123456789]{5}"
	#"[-]?"
	#"[0123456789]{3}"
	#Poso representar isso da seguinte maneira:
	#"[0-9]{5}[-]?[0-9]{3}"
	#O caractere [-]? posso dizer para o script que ele aparece 1 vez ou pode nenhuma
	"[0-9]{5}[-]{0,1}[0-9]{3}"
	)
busca = padrao.search(endereco) #Match
if (busca):
	#Retorna a string do padrão
	cep = busca.group()
	print(cep)
