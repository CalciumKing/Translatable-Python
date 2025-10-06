import re
import sys
import os
import csv


def get_strings(original_program: str) -> list[tuple[int, int]]:
	"""
	Searches through entire file program, saves indexes of double/single
	quotes in a list of tuples, returns that list.
	
	Uses list to avoid translations within quotes.
	
	:param original_program: non-translated program in string format
	:return: list of start and end positions of quotes
	"""
	
	string_locations: list[tuple[int, int]] = []
	
	inside: str | None = None
	pointer: int = -1
	for i, char in enumerate(original_program):
		if inside is None:
			if char in ("'", '"'):
				inside = char
				pointer = i
		elif char == inside:
			inside = None
			string_locations.append((pointer, i))
	
	return string_locations


def is_in_string(idx: int, string_positions: list[tuple[int, int]]) -> bool:
	"""
	Checks if index of keyword is within start and end index of single/double quotes
	
	Returns bool based on result
	
	:param idx: index of translatable keyword
	:param string_positions: list of start and end positions of quotes
	:return: ``True`` if index of keyword is within string indexes, ``False`` otherwise
	"""
	
	for start, end in string_positions:
		if start <= idx < end:
			return True
	return False


def get_translations() -> list[tuple[str, str]]:
	"""
	Reads translatable keywords from a csv file.
	
	:return: list of tuples containing python keywords and translatable keyword
	"""
	
	translations: list[tuple[str, str]] = []
	
	with open('lang.csv', encoding='utf-8', newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			translations.append((row[0], row[1]))
	
	return translations


def translate_program(program: str) -> str:
	"""
	Replaces all translatable keywords in program with python keywords.
	
	:param program: python-like program with translatable keywords
	:return: translated python program
	"""
	
	def replacer(match) -> str:
		"""Replaces translatable keywords if they are not located in a string"""
		
		idx = match.start()
		return py_word \
			if not is_in_string(idx, strings) \
			else match.group(0)
	
	strings = get_strings(program)
	
	for py_word, lang_word in get_translations():
		pattern = r'\b' + re.escape(lang_word) + r'\b'
		program = re.sub(pattern, replacer, program)
	
	return program


def run_program(program: str) -> None:
	"""
	Executes the python program
	
	:param program: fully translated python program
	:raises Exception: if any error occurs
	"""
	
	try:
		exec(program, {'__return_value__': None})
	except Exception as e:
		raise Exception(e)


def main() -> None:
	"""Main function: handles file input."""
	
	if len(sys.argv) == 1:
		raise IOError('Must Provide Additional Arguments')
	
	# Read code from file
	filename = sys.argv[1]
	
	if not filename.endswith('.tpy'):
		raise FileNotFoundError('Your Chosen File Is Not A .tpy File')
	
	with open(filename, 'r', encoding='utf-8') as f:
		code = f.read()
	
	python_program = translate_program(code)
	
	if len(sys.argv) == 2:
		run_program(python_program)
		return
	
	if not os.path.exists('debug'):
		os.makedirs('debug')
	
	with open(f'debug/debug.py', 'w', encoding='utf-8') as f:
		f.write(python_program)
	
	run_program(python_program)


if __name__ == '__main__':
	main()
