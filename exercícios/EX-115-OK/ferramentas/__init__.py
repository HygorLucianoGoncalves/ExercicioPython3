from ferramentas.menu import *
from ferramentas.arquivos import *
from ferramentas.cadastro import *

nomeArquivo = "testeex115.txt"

def dados():
  aquivoExiste(nomeArquivo)
  criaArquivo(nomeArquivo)
  while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa","Sair do Sistema"])#resp tem o valor de menu
    if resp == 1:
      #opção de listar o conteúdo de um arquivo.
      lerArquivo(nomeArquivo)
    elif resp == 2:
      #opção de cadastrar uma nova pessoa
      cabeçalho("NOVO CADASTRO")
      nome = str(input("Nome: "))
      idade = leiaInt("Idade: ")
      cadastrar(nomeArquivo,nome, idade)
    elif resp == 3:
      #opção de sair do sistema
      cabeçalho("Saindo do sistema...Até Logo")
      break
    else:
      #digitou uma opção errada no menu.
      print(f"\033[0;31mERRO! Digite um numero válido.\033[m")
  