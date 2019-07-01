#operands = input('Введите операции +, -, *, / и два числа')
class OperandsCountException(Exception):
	def __init__(self, text):
		self.txt = text

def sum(value1, value2):
	return value1 + value2

def sub(value1, value2):
	return value1 - value2

def mux(value1, value2):
	return value1 * value2

def div(value1, value2):
	try:
		return value1 / value2
	except ZeroDivisionError as e:
		print('Что то пошло не так')
		print('Ошибка: ', e)
		return 0
	except TypeError as e:
		print('Что то пошло не так')
		print('Ошибка: ', e)
		return 0


def main_circle():
	repeat = True
	while repeat:
		user_input = input('Введите операции +, -, *, / и два числа, q - выход: ')
		print('User input', user_input)
		try:
			usr_splitted = user_input.split()
			if len(usr_splitted) > 3 or len(usr_splitted) < 1:
				raise OperandsCountException('incorrect arguments number')
				print(usr_splitted)
				assert usr_splitted[0] in ['q', '+', '-', '*', '/']
			try:
				for k in usr_splitted:
					print('Splitted input: ', k)
				if usr_splitted[0] == 'q':
					repeat = False
				elif usr_splitted[0] == '+':
					print('Считаем сумму, результат: ', sum(int(usr_splitted[1]),int(usr_splitted[2])))
				elif usr_splitted[0] == '-':
					print('Считаем вычитание, результат: ', sub(int(usr_splitted[1]),int(usr_splitted[2])))
				elif usr_splitted[0] == '*':
					print('Считаем умножение, результат: ', mux(int(usr_splitted[1]),int(usr_splitted[2])))
				elif usr_splitted[0] == '/':
				# div после комментария в следующей строке для отладки трай эксепшн на ошибку типов
					print('Считаем деление, результат: ', div(int(usr_splitted[1]),int(usr_splitted[2]))) #div((usr_splitted[1]),(usr_splitted[2])))
			except Exception as e:
				print('Ооопс, ошибка: ', e)
		except OperandsCountException as errs:
			print(errs)


main_circle()