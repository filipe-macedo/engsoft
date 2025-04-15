from empresa import Empresa

empresa = Empresa("Turma 34")

empresa.cadastrar_pilar("Ética", "Agir de forma correta")
empresa.cadastrar_pilar("Transparência", "Comunicação clara e aberta")


empresa.cadastrar_funcionario("Ana", 4200)
empresa.cadastrar_funcionario("Carlos", 3500)


print("PILARES:")
empresa.consultar_pilares()

print("\nFUNCIONÁRIOS:")
empresa.consultar_funcionarios()
