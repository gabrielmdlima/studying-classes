from utils import clear_screen
from random import shuffle

class Personagens:
  def __init__(self, name, vida, ataque, defesa):
    self.name = name
    self.vida = vida
    self.ataque = ataque
    self.defesa = defesa


  def realizar_ataque(self, ataque, defesa):
    print(ataque)
    print(defesa)


  def cura(self):
    pass


def print_personagens(personagem):
  if not personagem[0].defesa == 0:
    print(f'{"Heróis":^37}')
    print(' '+'-'*37)
    print(f'|{"CLASSE":^12}|{"VIDA":^6}|{"ATAQUE":^8}|{"DEFESA":^8}|')
    print('|'+'-'*37+'|')
    for i, d in enumerate(personagem):
      vida = f'{d.vida:02}'
      ataque = f'{d.ataque:02}'
      defesa = f'{d.defesa:02}'
      print(f'|{i+1}.{d.name:10}|{vida:^6}|{ataque:^8}|{defesa:^8}|')
  else:
    print(f'{"Monstros":^37}')
    print(' '+'-'*37)
    print(f'|{"CLASSE":^12}|{"VIDA":^11}|{"ATAQUE":^12}|')
    print('|'+'-'*37+'|')
    for i, d in enumerate(personagem):
      vida = f'{d.vida:02}'
      ataque = f'{d.ataque:02}'
      print(f'| {d.name:11}|{vida:^11}|{ataque:^12}|')
  print(' '+'-'*37)


def get_player_choice(personagem):
  while True:
    try:
      player = str(input('Escolha seu personagem: ')).strip()
      print()
      if player.isdigit():
        ind = int(player) - 1

        if ind < len(personagem):
          return ind
        else:
          raise ValueError('Escolha um índice válido!')
      else:
        name = []
        for p in personagem:
          name.append(p.name)
        
        if player in name:
          return name.index(player)
        else:
          raise ValueError('Escolha um nome válido!')
    except ValueError as error:
      print(f'\033[31m{error}\033[m')
      continue


def monster_sequence(monstro):
  indices = list(range(len(monstro)))
  shuffle(indices)
  print('A ordem de monstros a ser enfrentada será:')
  for c, i in enumerate(indices):
    print(f'{c+1}º {monstro[i].name}')
  print()
  return indices


def run(heroi, monstro):
  while True:
    clear_screen()
    print_personagens(heroi)
    player = get_player_choice(heroi)
    character = [heroi[player].name, heroi[player].vida, heroi[player].ataque, heroi[player].defesa]
    print_personagens(monstro)
    monsters = monster_sequence(monstro)
    while True:
      stay = str(input('Sim - Confirmar partida.\nNão - Selecionar novamente\nDigite: ')).strip().upper()[0]
      if stay in 'SN':
        break
    if stay == 'S':
      break
    else:
      continue

  print(f'\n{character[0]} VS. ', end='')
  for i in monsters:
    print(f'{monstro[i].name}', end=', ')

if __name__ == '__main__':
  heroi = [
    Personagens('Cavaleiro', 10, 10, 5),
    Personagens('Mago', 15, 8, 8),
    Personagens('Tanque', 20, 5, 15),
    Personagens('Arqueiro', 5, 15, 5)
  ]

  monstro = [
    Personagens('Goblin', 5, 4, 0),
    Personagens('Lobo', 10, 7, 0),
    Personagens('Orc', 15, 10, 0)
  ]

  run(heroi, monstro)
