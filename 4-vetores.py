'''
Petrus, 10/03/2025
Criação de vetores com números igualmente espaçados e/ou aleatórios (inteiros e ponto flutuante)
'''

import numpy as np

vetor_aleatorio_inteiro = np.random.randint(0, 10, 5)
vetor_aletorio_pontoflutuante = np.random.uniform(0, 10, 5)
vetor_espaçado = np.linspace(0, 20, 100) 
