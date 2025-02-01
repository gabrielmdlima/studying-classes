from utils import clear_screen

class Book:
  def __init__(self, title, author, available):
    self.title = title
    self.author = author
    self.available = available


  def borrow_book(self):
    self.available = False


  def return_book(self):
    self.available = True


def print_table(books):
  clear_screen()
  print('='*60)
  print(f'{"LIVROS":^60}')
  print('='*60)

  print(f'\n|{"TÍTULO":^19}|{"AUTOR":^19}|{"SITUAÇÃO":^18}|')
  print('|','-'*56,'|')
  for i, b in enumerate(books):
    available = 'Disponível'
    if not b.available:
      available = 'Indisponível'
    print(f'| {i+1:2}) {b.title:<14}|{b.author:^19}|{available:^18}|')
  print('='*60)
  print()


def menu(books, error):
  while True:
    print_table(books)
    if error:
      print(error)
      error = ''

    print("""[1] Retirada
[2] Devolução
[3] Encerrar""")

    try:
      choice = int(input('Opção: '))
      if choice not in [1, 2, 3]:
        error = 'Erro: Opção inválida! Tente novamente!'
        continue
      else:
        return choice
    except ValueError:
      error = 'Erro: Digite um número válido!'


def get_book(books):
  while True:
    book = str(input('\nSelecione o livro (Nome ou Índice): ')).strip()

    if book.isdigit():
      index = int(book)-1
      if 0 <= index < len(books):
        return index

    else:
      for i, b in enumerate(books):
        if book.lower() == b.title.lower():
          return i
  
    print('Livro não encontrado!')


def validation_and_update_book(books, borrow):
  while True:
    index = get_book(books)
    if books[index].available == borrow:
      if borrow:
        books[index].borrow_book()
      else:
        books[index].return_book()
      break
    print(f'Livro já está {"emprestado" if borrow else "disponível"}! Escolha outro.')


def run(books):
  error = ''
  while True:
    choice = menu(books, error)
    error = ''
    
    if choice == 1:
      if not any(book.available for book in books):
        error = 'Todos os livros já foram emprestados! Retorne um livro antes.'
        continue
      validation_and_update_book(books, True)
    elif choice == 2:
      if all(book.available for book in books):
        error = 'Nenhum livro foi retirado ainda! Escolha um livro para emprestar primeiro.'
        continue
      validation_and_update_book(books, False)
    else:
      return


if __name__ == '__main__':
  books = [
    Book("1984", "Orwell", True),
    Book("Moby Dick", "Melville", True),
    Book("War & Peace", "Tolstoy", True),
    Book("Dune", "Herbert", True),
    Book("It", "King", True),
    Book("Dracula", "Stoker", True),
    Book("Hamlet", "Shakespeare", True),
    Book("Inferno", "Dante", True),
    Book("Utopia", "More", True),
    Book("Emma", "Austen", True)
  ]

  run(books)
