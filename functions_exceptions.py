documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
	{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
	{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
# "плохой" словарь для проверки исключения:
	{"type": "driverlicense", "number": "201"}
	]

directories = {
	'1': ['2207 876234', '11-2'],
	'2': ['10006'],
	'3': []
}

def doc_owner(doc_list):
	print('----- Список всех владельцев документов -----')
	try:
		for document in documents:
			print('Имя владельца', document['name'])
		print('----- Ищем имя по номеру документа -----')
	except KeyError as e:
		print('Что то пошло не так, не хватает ключа: ', e)
	print('----- Конец списка владельцев -----')

def my_help():
	print('   Помощь по командам: ')
	print('   p - people,  введите номер документа и получите имя ')
	print('   l - list')
	print('   s - shelf')
	print('   a - add')
	print('   o - список владельцев')	

def search_by_docnumber(doc_list):
	print('----- Ищем имя по номеру документа -----')
	doc_number = input('  Введите номер документа: ')
	founded = False
	for doc_element in doc_list:
		if doc_element['number'] == doc_number :
			print('  Имя человека с этим документом: ', doc_element['name'])
			founded = True
	if not founded :
		print('  Документа с таким номером не существует')
	print('----- Конец поиска -----')

def list_of_docs(doc_list):
	try:
		print('----- Список документов: -----')
		for doc_element in doc_list:
			print('  ', doc_element['type'], doc_element['number'], doc_element['name'])
		print('----- Конец списка -----')
	except KeyError as e:
		print('Что то пошло не так, не хватает ключа: ', e)

def search_in_shelves(list_of_shelves):
	print('----- Поиск полки по документу ---')
	doc_number = input('  Введите номер документа: ')
	doc_founded = False
	#print('Список полок с содержимым ', list_of_shelves)
	for shelf in list_of_shelves :
		#принт для дебага
		#print('Значение ключа shelf: ', shelf)
		for shelf_contain in list_of_shelves[shelf]:
			#принт для дебага
			#print('Значение в словаре list_of_shelves',shelf_contain)
			if doc_number == shelf_contain:
				print('  Этот документ на полке номер: ', shelf)
				doc_founded = True
			#else for debug
	if not doc_founded:
		print('  документ на полках не найден')
	print('----- Конец поиска -----')

def add_document(doc_list, list_of_shelves):
	print('------ Добавляем документ -----')
	new_doc = {}
	new_doc['type'] = input('  тип документа: ')
	new_doc['number'] = input('  номер: ')
	new_doc['name'] = input('  имя: ')
	shelf_number = input('  номер полки (1-3): ')
	if (int(shelf_number) > 3) or (int(shelf_number) < 1) :
		print('  Неправильный ввод номера полки')
	else :
		doc_list.append(new_doc)
		#принт для дебага
		'''
		print('Добавляем на полку номер: ', shelf_number, 'документ номер',new_doc['number'] )
		print('На полке было: ', list_of_shelves[shelf_number])
		'''
		list_of_shelves[shelf_number].append(new_doc['number'])
		# для дебага
		#print('  На полке стало: ', list_of_shelves[shelf_number])
	print('----- Конец добавления -----')

def main_repeater(doc_list,list_of_shelves):
	repeat = True
	while repeat:
		command = input('  Введите команду (p,l,s,a,o; h - помощь; q - выход)')
		if command == 'q' :
			repeat = False
			break
		elif command == 'h' :
			my_help()
		elif command == 'p':
			search_by_docnumber(doc_list)
		elif command == 'l':
			list_of_docs(doc_list)
		elif command == 's':
			search_in_shelves(list_of_shelves)
		elif command == 'a':
			add_document(doc_list, list_of_shelves)
		elif command == 'o':
			doc_owner(doc_list)
		else:
			print('  Нет такой команды. Попробуйте еще.')

main_repeater(documents, directories)
