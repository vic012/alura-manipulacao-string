import re

class ExtratorUrl:
	def __init__(self, url):
		self.url = self.sanitiza_url(url)
		self.valida_url()

	def sanitiza_url(self, url):
		if (type(url)==str):
			return url.strip()
		else:
			return ""

	def valida_url(self):
		if (not self.url):
			raise ValueError("A URL está vazia")

		padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
		#Se não encontrar nada retorna none
		match = padrao_url.match(self.url)

		if not match:
			raise ValueError("A URL é inválida.")

	def get_url_base(self):
		indice_interrogacao = self.url.find("?")
		url_base = self.url[:indice_interrogacao]
		return url_base

	def get_url_parametros(self):
		indice_interrogacao = self.url.find("?")
		url_parametros = self.url[indice_interrogacao + 1:]
		return url_parametros

	def get_valor_parametro(self, parametro_busca):
		indice_parametro = self.get_url_parametros().find(parametro_busca)
		indice_valor = indice_parametro + len(parametro_busca) + 1
		indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
		if (indice_e_comercial == -1):
			valor = self.get_url_parametros()[indice_valor:]
		else:
			valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
		return valor

	def __len__(self):
		return len(self.url)

	def __str__(self):
		return self.url

	#Serve para comparar objetos
	def __eq__(self, other):
		return self.url == other.url


#extrator_url = ExtratorUrl(" ")
#extrator_url = ExtratorUrl(None)
extrator_url = ExtratorUrl("bytebank.com/cambio")
extrator_url2 = ExtratorUrl("bytebank.com/cambio")
print(f"O tamanho da URL é: {len(extrator_url)}")
print(extrator_url == extrator_url2)
