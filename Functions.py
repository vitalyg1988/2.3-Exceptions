# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

# задание доп:

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;



documents_list = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories_dict = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def show_people(number, documents_list):
  for document in documents_list:
    if number == document['number']:
      return document['name']
  return 'Такого номера нет в архиве!'

def show_list(documents):
  for document in documents:
    print(f'{document["type"]}: "{document["number"]}" "{document["name"]}"')

def show_shelf(number, directories):
  for directory in directories:
    if number in directories[directory]:
      return directory
  return 'Такого номера документа нет в архиве!'

def add_document(number_directory, number, documents, directories):
  if directory(number_directory, directories) is False:
    return
  add_to_directories(number_directory, number, directories)
  create_document(number,documents)
  print('Документ добавлен')

def create_document(number, documents):
  inform_document = dict()
  inform_document['type'] = input('Введите тип документа: ')
  inform_document['number'] = number
  inform_document['name'] = input('Введите имя и фамилию через пробел: ')
  documents.append(inform_document)

def directory(number_directory, directories):
  if number_directory not in directories:
    print('Такого каталога не существует')
    return False

def add_to_directories(number_directory, number, directories):
  for directory in directories:
    if number_directory == directory:
      directories[directory].append(number)


def check_name(documents_list):
    try:
        for document in documents_list:
            print(document['name'])
    except KeyError:
        print('Поля name не существует в документе')


def main_menu():
  number_document = lambda: input('Введите номер документа: ')
  number_directory = lambda: input('Введите номер каталога для сохранения документа: ')
  print('''
        p - вывести имя владелца по номеру документа
        l - вывести список всех документов
        an - вывести имена всех владельцев документов
        s - вывести номер полки на которой находится документ
        a - добавить новый документ
        q - выход из программы
        ''')
  while True:
    user_input = input('Введите команду: ').lower()
    if user_input == 'p':
      print(show_people(number_document(), documents_list))
    elif user_input == 'l':
      show_list(documents_list)
    elif user_input == 'an':
      check_name(documents_list)
    elif user_input == 's':
      print(f'Номер каталога в которой находится документ: {show_shelf(number_document(), directories_dict)}')
    elif user_input == 'a':
      add_document(number_directory(), number_document(), documents_list, directories_dict)
    elif user_input == 'q':
      print('Выход из программы')
      break
    else:
      print('Такой команды нет')


main_menu()