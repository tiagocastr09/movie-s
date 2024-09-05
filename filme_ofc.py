import os 
from time import sleep
def avaliar_filme(nome_filme):

  avaliacao = input(f"Qual a sua avaliação para o filme {nome_filme} (de 1 a 5 estrelas)? ")
  while not avaliacao.isdigit() or int(avaliacao) < 1 or int(avaliacao) > 5:
    print("Avaliação inválida. Digite um número de 1 a 5.")
    avaliacao = input(f"Qual a sua avaliação para o filme {nome_filme} (de 1 a 5 estrelas)? ")
  avaliacao = int(avaliacao)

  if avaliacao >= 4:
    return "Excelente! Recomendo este filme."
  elif avaliacao == 3:
    return "Bom filme, mas existem melhores opções."
  else:
    return "Não recomendo este filme."

def recomendar_filme(genero):

  filmes = {
    "AÇÃO": ["Mad Max: Estrada da Fúria (2015)"],
    "AVENTURA": ["Indiana Jones e os Caçadores da Arca Perdida (1981)"],
    "COMÉDIA": ["Gente Grande 1 (2010)"],
    "DRAMA": ["Parasita (2019)"],
    "FICÇÃO CIENTÍFICA": ["Star Wars (1977) "],
    "MUSICAL": ["La La Land (2016)"],
    "ROMANCE": ["Orgulho e Preconceito (2005)"],
    "TERROR": ["O Exorcista (1973)"]
  }

  if genero in filmes:
    filme_recomendado = filmes[genero][0]
    for filme in filme_recomendado:
     return f"Recomendo que você assista ao filme: {filme_recomendado}. Um ótimo filme de {genero}!"
  else:
    return "Desculpe, não tenho filmes recomendados para este gênero."

while True:
  opcao = input("""
  -------------- O que você deseja fazer?--------------
                 1 - Avaliar um filme
                 2 - Obter uma recomendação de filme
                 3 - Sair\n"""
                 "Digite o número da opção desejada: " )

  if opcao == '1':
    nome_filme = input("Digite o nome do filme que você deseja avaliar: ")
    avaliacao = avaliar_filme(nome_filme)
    sleep (0.5)
    os.system ("cls")
    print(avaliacao)
  elif opcao == '2':
    genero = input("Digite gênero do filme que você deseja (ex: ação, comédia, romance, terror..): ").strip().upper()
    recomendacao = recomendar_filme(genero)
    sleep (0.5)
    os.system ("cls")
    print(recomendacao)
  elif opcao == '3':
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida. Por favor, digite um número de 1 a 3.")