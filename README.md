# Translatable Python (`.tpy`)

Translatable Python (TPY) is a lightweight python compiler that lets you swap Python keywords with your own words. 
Whether you want to code in slang, inside jokes, or another language, you can! 

`lang.py` translates specified keywords contained in `lang.csv` into valid Python code and then executes that python 
code.

This project also has the potential to translate any language supported by UTF-8 into valid python code.

## Installation

You don't need to "install" anything special. Just make sure you have Python 3 (preferably 3.10 or later, for 
`match`/`case` support) installed on your system.

## Running Translatable Python

1.  **Specify Keywords In Your Language**
    
    To specify keywords, open `lang.csv` and add each translation in place of the current translation in the format 
    `PythonKeyword,TranslatedKeyword`. The first column must be the original Python keyword (e.g. if, else, print), 
    and the second column is your custom translation. Do not add multiple keywords or different translatable 
    keywords for the same Python keyword, each line should contain strictly a python keyword and a unique 
    translatable keyword. Make sure to save the file with UTF-8 encoding if your language uses special characters. 
    The program will automatically read these pairs and use them to translate your code.

2.  **File Input:**

    Create a `.tpy` file containing your translatable code (e.g., `example.tpy`). Then, run the compiler with the 
    filename as an argument:

    ```bash
    python lang.py example.tpy
    ```

## Example

1. `lang.csv` (Example):
	```csv
	def,myfunc
	return,sendback
	if,whenever
	else,otherwise
	print,say
	```

2. Custom Code (hello.tpy):
	```text
	myfunc greet(name) {
	    say("Hello " + name)
	    sendback "done"
	}
	
	greet("World")
	```

3. Run It:
	```bash
	python lang.py hello.tpy
	```

4. Output:
	```text
	Hello World
	```