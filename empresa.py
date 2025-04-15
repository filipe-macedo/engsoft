from pilar import Pilar
from funcionario import Funcionario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.pilares = []
        self.funcionarios = []

    def cadastrar_pilar(self, nome, descricao):
        p = Pilar()
        p.cadastrar(nome, descricao)
        self.pilares.append(p)

    def consultar_pilares(self):
        for p in self.pilares:
            p.exibir()

    def cadastrar_funcionario(self, nome, salario):
        f = Funcionario()
        f.cadastrar(nome, salario)
        self.funcionarios.append(f)

    def consultar_funcionarios(self):
        for f in self.funcionarios:
            f.exibir()
