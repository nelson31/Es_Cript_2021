import os

''' 
Classe que permite gerar 
nounces que nunca se repetem
'''
class NGenerator :

	# Construtor para objetos da classe NGenerator
	def __init__(self,size) :

		self.size = size
		self.historic = []

	''' 
	Método que nos permite obter um novo nounce
	'''
	def get(self) :

		nounce = os.urandom(self.size)
		while nounce in self.historic :
			nounce = os.urandom(self.size)
		self.historic.append(nounce)
		return nounce

	'''
    Método que nos permnite adicionar um novo nounce 
    ao historico. Método importante para registar os 
    nounces usados pelo peer.
    '''
	def addToHistoric(self,nounce) :

		self.historic.append(nounce)