"""
Russian Python - A Python-like language with Russian Keywords.
This is a rudimentary interpreter, not a full compiler. It translates
Russian keywords into valid Python code and then *executes* that Python code.
This approach has significant limitations, but it's a good way to demonstrate
the basic concept without building a full-blown compiler and virtual machine.

This project also has potential to translate any languages supported by UTF-8
into valid python code.

Key Design Choices:

-   **Interpreter, not Compiler:** This is easier to implement for a demo.
-   **Entire File Translation:** We process all the Russian code before executing.
-   **exec() for Execution:** After translating a line to Python, we use `exec()`
    to run it. `exec()` is powerful but can be dangerous with untrusted input.
    In a real language, you'd build an Abstract Syntax Tree (AST) and evaluate it.
-   **Limited Scope:** This interpreter supports only a subset of Python features.
-   **Global Namespace:**  We use a single global dictionary (`global_vars`) to
    store variables. This keeps things simple but would be problematic in a
    real language (no function-local scope, etc.).
-   **String handling** Strings are supported, so the rant is very functional.
"""

import re
import sys
import os

translations: list[tuple[str, str]] = [
		('None', 'ничего'),
		('int', 'цел'),
		('float', 'вещ'),
		('str', 'стр'),
		('bool', 'бул'),
		('True', 'да'),
		('False', 'нет'),
		('if', 'если'),
		('else', 'иначе'),
		('while', 'пока'),
		('break', 'прервать'),
		('continue', 'продолжить'),
		('for', 'для'),
		('return', 'воз'),
		('print', 'печать'),
		('input', 'ввод'),
		('match', 'соп'),
		('try', 'поп'),
		('case', 'случай'),
		('raise', 'выб'),
		('def', 'функ'),
		('in', 'в'),
		('range', 'диапазон'),
		
		(' not ', ' не '),
		(' and ', ' и '),
		(' or ', ' или '),
	]

def get_strings(orinigal_programs):
	stringsLocations = []

	inside = "NONE"
	pointer = -1
	for i, char in enumerate(orinigal_programs):
		if (inside == "NONE"):
			if (char == "'" or char == '"'):
				inside = char
				pointer = i
		else:
			if (char == inside):
				inside = "NONE"
				stringsLocations.append((pointer, i))

	return stringsLocations

def is_in_string(idx, string_locs):
		for start, end in string_locs:
			if start <= idx < end:
				return True
		return False

def translate_program(program: str) -> str:
	string_locs = get_strings(program)
	
	for py_word, rus_word in translations:
		def replacer(match):
			idx = match.start()
			return py_word if not is_in_string(idx, string_locs) else match.group(0)
		pattern = r'\b' + re.escape(rus_word) + r'\b'
		program = re.sub(pattern, replacer, program)
	return program



def main():
	"""Main function: handles file input."""
	
	if len(sys.argv) > 1:
		# Read code from file
		filename = sys.argv[1]
		
		if not filename.endswith('.blyad'):
			raise FileNotFoundError('Your Chosen File Is Not A .blyad File')
		
		try:
			with open(filename, 'r', encoding='utf-8') as f:
				code = f.read()

			python_program = translate_program(code)

			if len(sys.argv) == 3 and sys.argv[2] == '--debug':
				if not os.path.exists('debug'):
					os.makedirs('debug')
				
				with open(
						f'debug/{filename.removesuffix('.blyad')}.py', 'w',
						encoding='utf-8'
				) as f:
					f.write(python_program)

			try:
				exec(python_program)
			except Exception as e:
				raise Exception(e)
			
			

		except FileNotFoundError:
			raise FileNotFoundError(f'Error: File not found: {filename}')


if __name__ == '__main__':
	main()
