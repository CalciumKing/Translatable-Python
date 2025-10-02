"""
Gen Alpha Python (GAP) - A Python-like language with Gen Alpha slang.
This is a rudimentary interpreter, not a full compiler.  It translates
Gen Alpha slang into valid Python code and then *executes* that Python code.
This approach has significant limitations, but it's a good way to demonstrate
the basic concept without building a full-blown compiler and virtual machine. 😁

Key Design Choices:

*   **Interpreter, not Compiler:** This is easier to implement for a demo.
*   **Line-by-Line Translation:** We process the Gen Alpha code one line at a time.
    This simplifies parsing.
*   **`exec()` for Execution:** After translating a line to Python, we use `exec()`
    to run it.  `exec()` is powerful but can be dangerous with untrusted input.
    In a real language, you'd build an Abstract Syntax Tree (AST) and evaluate it.
*   **Limited Scope:** This interpreter supports only a subset of Python features.
*   **Global Namespace:**  We use a single global dictionary (`global_vars`) to
    store variables. This keeps things simple but would be problematic in a
    real language (no function-local scope, etc.).
*    **String handeling** Strings are supported, so the rant is very functional.

"""

import re  # For regular expressions (used for parsing)
import sys
import os


def translate_line(line, global_vars):
    """Translates a single line of Gen Alpha Python to standard Python.

    Args:
        line (str): The line of Gen Alpha Python code.
        global_vars (dict): The dictionary holding global variables.

    Returns:
        str: The equivalent Python code, or None if the line should be skipped.
    Raises:
        ValueError: If the Gen Alpha syntax is invalid.
    """

    if not line:  # Skip empty lines TODO: also skip on comment indicator
        return None

    # TODO: optimize using dictionary or tuple
    # --- Lexical Replacements (Simple Keywords) ---
    line = line.replace("нечего", "None")
    line = line.replace("цел", "int")  # Still useful for type hinting (though not enforced)
    line = line.replace("вещ", "float")
    # line = line.replace("gigachad", "float") # float in this simple interpretor
    line = line.replace("стр", "str")
    line = line.replace("бул", "bool")
    line = line.replace("да", "True")
    line = line.replace("нет", "False")
    line = line.replace("если", "if")
    line = line.replace("иначе", "else")
    line = line.replace("пока", "while")
    line = line.replace("прервать", "break")
    line = line.replace("продолжить", "continue")
    line = line.replace("для", "for")
    line = line.replace("воз", "return")  # Limited 'return' support (see below)
    line = line.replace("печать", "print") # Keep print
    line = line.replace("ввод", "input") # keep input
    line = line.replace("соп", "match")  #  match/case (Python 3.10+)
    line = line.replace("поп", "try")
    line = line.replace("случай", "case")
    # line = line.replace("based", "case _")   #Default case match
    line = line.replace("выб", "raise") # Better for exceptions
    # line = line.replace("equals", "=")
    # line = line.replace("plus", "+")
    # line = line.replace("minus", "-")
    # line = line.replace("times", "*")
    # line = line.replace("divide", "/")
    # line = line.replace("modulo", "%")
    line = line.replace(" не ", " not ")
    line = line.replace(" и ", " and ")
    line = line.replace(" или ", " or ")
    # line = line.replace("equals_equals", "==")
    # line = line.replace("not_equals", "!=")
    # line = line.replace("less_than", "<")
    # line = line.replace("greater_than", ">")
    # line = line.replace("less_than_or_equal", "<=")
    # line = line.replace("greater_than_or_equal", ">=")
    # line = line.replace("semicolon", "") # Remove semicolons
    # line = line.replace("comma", ",")
    # line = line.replace("lparen", "(")
    # line = line.replace("rparen", ")")
    # line = line.replace("lbrace", ":")   # Use : for blocks (Python style)
    line = line.replace("{", ":")  # start of a block
    line = line.replace("}", "")  # end of a block (just remove)
    line = line.replace('функ', 'def')


    # --- Function Definition (Very Basic) ---
    #   def my_function(arg1, arg2):
    match = re.match(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*)\)\s*:", line)
    if match:
        func_name = match.group(1)
        args_str = match.group(2).strip()
        return f"def {func_name}({args_str}):"

    # --- Return Statements (Limited) ---
    # We can't *really* handle return values properly without a full AST.
    # This is a VERY basic "return" that works *only* at the top level
    # (outside of functions) and only for simple expressions.  It stores
    # the return value in a special variable.
    if line.startswith("return"):
        return_value_expression = line[len("return"):].strip()
        return f"__return_value__ = {return_value_expression}"
    
    return line

def run_gap_code(code):
    """Executes Gen Alpha Python code.

    Args:
        code (str): The Gen Alpha Python code.
    """

    global_vars = {}  # Initialize the global namespace
    global_vars["__return_value__"] = None # Initialize for return
    lines = code.split('\n')
    indent_level = 0
    in_function_def = False
    translated_program = []

    for original_line in lines:
        translated_line = translate_line(original_line, global_vars)

        if translated_line is None:  # Skip empty or comment lines
            continue

        # --- Indentation Handling (Crucial for Python) ---
        # This is a *very* simplified indentation handler.  It assumes:
        # 1. Indentation is always consistent (e.g., always 4 spaces).
        # 2. There's no multi-line statements within blocks (which is illegal in Python anyway).
        #leading_spaces = len(original_line) - len(original_line.lstrip())  
        #  Assume 4 spaces per indent
        
        # --- Function Definition Indentation
        if translated_line.startswith("def"):
            in_function_def = True

        if not in_function_def:
            pass
          # Adjust to be outside function defs

        # Prepend the correct number of spaces for indentation
        translated_program.append(translated_line)

    # --- Execute the Translated Line ---
    try:
        exec('\n'.join(translated_program), global_vars)
        return '\n'.join(translated_program)
    except Exception as e:
        # print(f"Error executing line: {original_line.strip()}")
        # print(f"Translated line: {translated_line.strip()}")
        print(f"Error: {e}")
        return  # Stop on error

    # --- Print the "Return Value" (if any) ---
    if global_vars["__return_value__"] is not None:
        print(f"Returned: {global_vars['__return_value__']}")

def main():
    """Main function: handles file input or interactive input."""

    if len(sys.argv) > 1:
        # Read code from file
        filename = sys.argv[1]

        if not filename.endswith('.blyad'):
            print('Your Chosen File Is Not A .blyad File')
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            python_program = run_gap_code(code)

            if (len(sys.argv) > 2 and sys.argv[2] == '--debug'):
                if not os.path.exists("debug"):
                    os.makedirs("debug")
                with open(f"debug/{filename.removesuffix('.blyad')}.py", "w", encoding="utf-8") as debug_file:
                    debug_file.write(python_program)
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")

    else: # TODO: remove later
        # Interactive mode
        print("Gen Alpha Python Interpreter (Interactive Mode)")
        print("Enter 'exit' to quit.")
        code_buffer = []
        while True:
            try:
                line = input("gap> ")  # Prompt
                if line.strip().lower() == "exit":
                    break
                code_buffer.append(line)
                # Check if the entered line completes a block (very basic check)
                if line.strip().endswith(":"):
                  #If colon start multi line statement
                    continue
                else:
                    # Run accumulated code if no more multi-line input is needed
                    run_gap_code('\n'.join(code_buffer))
                    code_buffer = [] #Reset Buffer
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except EOFError:
                print("\nExiting...")
                break

if __name__ == "__main__":
    main()
