# Gen Alpha Programming (GAP)

Gen Alpha Programming (GAP) is a fun, experimental Python-like language that uses Gen Alpha slang for its syntax.  It's designed as a demonstration of how a simple interpreter can be built and to provide a humorous take on programming languages.  It is *not* intended for serious software development, but rather as an educational and entertaining project.

**Important Note:** This is a simplified interpreter, *not* a full compiler.  It translates GAP code into standard Python and then executes it.  This means it has limitations compared to a fully compiled language.

## Installation

You don't need to "install" anything special.  Just make sure you have Python 3 (preferably 3.10 or later, for `match`/`case` support) installed on your system.  Then, save the interpreter code (provided in the `genalpha_python.py` file) to your computer.

## Running GAP Code

There are two ways to run GAP code:

1.  **Interactive Mode:**

    Open your terminal or command prompt and run the interpreter script:

    ```bash
    python gena.py
    ```

    You'll see a `gap> ` prompt.  Type your GAP code line by line, and it will be executed immediately.  Type `exit` to quit the interactive mode.  Multi-line statements (like `if`, `for`, `while`, and function definitions) are supported; the interpreter will wait for the complete block (indicated by a colon at the end of the initial line) before executing.

2.  **File Input:**

    Create a text file containing your GAP code (e.g., `my_program.gap`).  Then, run the interpreter with the filename as an argument:

    ```bash
    python gena.py my_program.gap
    ```

    The interpreter will read and execute the code from the file.

## Syntax Overview

Here's a mapping of Gen Alpha slang to their Python equivalents, along with examples:

| Gen Alpha Slang | Python Equivalent      | Description                                 | Example                                       |
|-----------------|------------------------|---------------------------------------------|-----------------------------------------------|
| `skibidi`        | `None` / `def`          | No value / Function definition              | `skibidi my_var`  /  `skibidi my_func():`   |
| `rizz`          | `int`                  | Integer type hint (not strictly enforced)   | `rizz x equals 5`                              |
| `chad`          | `float`                | Floating-point type hint (not enforced)    | `chad pi equals 3.14159`                       |
| `gigachad`      | `float`                 |Floating-point number (same as chad)        |`gigachad big_num = 12345.67`                   |
| `yap`           | `str`                  | String type hint                            | `yap my_string equals "Hello"`                |
| `cap`           | `bool`                 | Boolean type hint (not enforced)          | `cap is_true equals W`                        |
| `W`             | `True`                 | Boolean True                                | `cap flag equals W`                            |
| `L`             | `False`                | Boolean False                               | `cap another_flag equals L`                   |
| `edgy`          | `if`                   | If statement                                | `edgy x greater_than y lbrace ...`              |
| `amogus`        | `else`                 | Else statement                              | `edgy x greater_than y lbrace ... amogus lbrace ...` |
| `goon`          | `while`                | While loop                                  | `goon x less_than 10 lbrace ...`             |
| `bruh`          | `break`                | Break statement (exit loop)                 | `goon W lbrace edgy condition lbrace bruh`      |
| `grind`         | `continue`             | Continue statement (skip to next iteration) | `flex i in range(10) lbrace edgy i modulo 2 equals_equals 0 lbrace grind ...` |
| `flex`          | `for`                  | For loop                                    | `flex i in range(5) lbrace ...`                |
| `bussin`        | `return` (limited)     | Return statement (very basic implementation) | `skibidi my_func() lbrace bussin 42`           |
| `print`        | `print`                  | Print statement                               | `print("Hello, world!")`                   |
| `input`         |`input`                  | Read user input                         |`rant user_name = input("Enter name: ")`      |
| `ohio`          | `match`                | Match statement (Python 3.10+)              | `ohio value lbrace ...`                       |
| `sigma_rule`    | `case`                 | Case within a match statement               | `ohio x lbrace sigma_rule 1: ...`               |
| `based`         | `case _`                | Default case in a match statement           | `ohio x lbrace ... based: ...`                |
| `cringe`        | `raise`               | Raise an exception                          | `cringe ValueError("Something went wrong")`   |
| `equals`        | `=`                    | Assignment operator                         | `rizz x equals 10`                            |
| `plus`          | `+`                    | Addition operator                           | `x plus y`                                    |
| `minus`         | `-`                    | Subtraction operator                        | `x minus y`                                   |
| `times`         | `*`                    | Multiplication operator                     | `x times y`                                   |
| `divide`        | `/`                    | Division operator                           | `x divide y`                                  |
| `modulo`        | `%`                    | Modulo operator                             | `x modulo y`                                  |
| `not`           | `not`                  | Logical NOT operator                        | `not cap`                                     |
| `and`           | `and`                  | Logical AND operator                        | `x greater_than 0 and x less_than 10`         |
| `or`            | `or`                   | Logical OR operator                         | `x equals_equals 0 or y equals_equals 0`      |
| `equals_equals` | `==`                   | Equality comparison operator                | `x equals_equals y`                            |
| `not_equals`    | `!=`                   | Inequality comparison operator              | `x not_equals y`                              |
| `less_than`     | `<`                    | Less than comparison operator               | `x less_than y`                               |
| `greater_than`  | `>`                    | Greater than comparison operator            | `x greater_than y`                            |
| `less_than_or_equal` | `<=`                | Less than or equal to comparison           | `x less_than_or_equal y`                     |
| `greater_than_or_equal` | `>=`              | Greater than or equal to comparison        | `x greater_than_or_equal y`                  |
| `semicolon` |  *(removed)*         | Semicolons are removed                       |                               |
| `comma`           | `,`          |    Commas are kept                     |                             |
|`lparen` | `(` | Left Parenthesis | `print(x)` |
|`rparen` | `)` | Right Parenthesis | `print(x)` |
|`lbrace`          |`:`                    |   Colon (for blocks)                           |                                               |
|`rant`            |`str`                   |   Strings                                         |`rant name = "John"`                                              |

**Key Concepts:**

*   **Indentation:** GAP, like Python, uses indentation (4 spaces recommended) to define code blocks (e.g., inside `if`, `for`, `while`, and function definitions).
*   **Functions:**  Functions are defined using `skibidi function_name(arguments) lbrace ...`.  The `bussin` keyword is used for a very basic form of return (see limitations below).
* **Strings:** Strings are supported using the `rant` keyword.

**Limitations:**

*   **Simplified Interpreter:** This is *not* a full-featured programming language.  It's a demonstration project.
*   **Limited `return`:** The `bussin` keyword provides only very basic return functionality.  It works primarily for simple expressions at the top level (outside of functions) and stores the "returned" value in a special variable.  It doesn't handle complex return scenarios within nested functions.
*   **No Classes:**  Object-oriented programming features (classes, objects, methods) are not supported.
*   **No Modules/Imports:** There's no support for importing external modules.
*   **Limited Error Handling:** The error messages might not always be very helpful, especially if the error is caused by the underlying Python code generated by the interpreter.
*   **Global Scope Only:**  All variables are in a single global scope.  There's no concept of local variables within functions (beyond function parameters).
* **No Type Enforcement** Type Hints like `rizz` are replaced but python does not enforce them.

**Example Program (example.gap):**
```Example.gap
skibidi greet(yap name) lbrace
print("Hello, " plus name plus "!")

skibidi factorial(rizz n) lbrace
edgy n equals_equals 0 lbrace
bussin 1
amogus lbrace
bussin n times factorial(n minus 1)

rizz num equals 5
rizz fact equals factorial(num)
print("Factorial of " plus str(num) plus " is " plus str(fact)) # Convert numbers to strings for printing

greet("World")

flex i in range(1, 6) lbrace # Loop from 1 to 5
print("Current number: " plus str(i))

goon W lbrace #Infinite loop
rant user_input = input("Enter a number (or 'quit' to exit): ")
edgy user_input equals_equals "quit" lbrace
bruh
amogus:
rizz number = int(user_input)
print("You entered: " plus str(number))
rbrace```


This README provides a comprehensive guide to using Gen Alpha Python, including installation, running instructions, a detailed syntax overview, key concepts, limitations, and a complete example program. This makes the project much more accessible and understandable for users.
