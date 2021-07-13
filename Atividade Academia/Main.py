from Atendentes import Atendentes
from Instrutores import Instrutores
from Clientes import Clientes
from Coordenador import Coordenador
from Aula import Aula

# a1 = Atendentes("01", "Marcelo", "12/12/1980", 1200, "madrugada")
i1 = Instrutores("02", "Joel", "08/03/1990", 2000, "vespertino", "1234556456", "musculação")
coor1 = Coordenador("05", "Junior", "1/12/1980", 3000, "vespertino", "123512", "crossfit")
coor1.instrutores = i1
print(coor1.instrutores)

c1 = Clientes("00001", "José", "10/07/2003", "premium")
alunos = [c1]
crossfit = Aula(30, "crossfit", i1, alunos)
print(crossfit.alunos)





# c1.plano = "economico"
# print(c1.plano)

# c1.plano = "platinum"
# print(c1.plano)

# c1.plano = "gold"
# print(c1.plano)
