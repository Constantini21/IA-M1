import sys

from nQueens import HillClimbingRandom
from time import time

if __name__ == '__main__':
	# certifique-se de que um número de rainhas para colocar no tabuleiro foi passado
	if len(sys.argv) < 2:
		print('Este programa requer um número de rainhas para colocar como argumento.')
		print('Exemplo: python run.py 8')
		sys.exit(1)
	
	try:
		numQueens = int(sys.argv[1])
	except ValueError:
		print('Valor passado é invalido.')
	
	hillClimbingRandom = HillClimbingRandom(numQueens)
	print('Procurando solução com {}...'.format(hillClimbingRandom.__class__.__name__))
	startTime = time()
	hillClimbingRandom.solve()
	print('Solução encontrada em {}s:'.format(round(time() - startTime, 4)))
	hillClimbingRandom.printBoard()
