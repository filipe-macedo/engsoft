class Funcionario:
    def cadastrar(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}")
