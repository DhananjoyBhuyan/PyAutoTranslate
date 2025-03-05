# **PyAutoTranslate** 🚀  

## **The Future of Code Translation is Here!**  
Tired of writing code in different programming languages? And remembering their very hard syntaxes?? PyAutoTranslate is here to change the game. This powerful tool **converts pseudo-code, structured English, or abstract syntax or your custom code in custom syntax into real, executable programming languages**. Whether you're a beginner, a coder experimenting with ideas, or just someone who wants to see code in different languages effortlessly—PyAutoTranslate has you covered!  

---

# **🤖 What is PyAutoTranslate?**  

PyAutoTranslate is a **code translator** that allows you to write **plain English, structured pseudo-code, or high-level code descriptions or any custom code in your style,** and converts them into real programming languages such as **C, Python, Java, JavaScript, and all the languages which exist!**  

Imagine writing:  

```python

from pyautotranslate import init, execute_code

init("output_file_name", extension_of_output_file=".output language extension", language="the output language you want to translate to")

"""pycode
define x = 10
define y = 20

print("Sum is", x + y)
"""
execute_code()
```  

And instantly getting the equivalent C, html, Java or any language code—without manually converting anything.  

---

# **🔥 Why Use PyAutoTranslate?**  

- **🚀 Fast & Efficient** – No more wasting time manually converting code between languages.    
- **🎯 Beginner-Friendly** – Even if you don't know a language, you can still get working code.  
- **🔄 Supports Multiple Languages** – Convert your pseudo-code or any custom syntax code or existing code in any language into C, Python, Java, JavaScript, and more.  
- **🔗 Seamless Integration** – Just add a few lines to your script, and you're good to go!  

---

# EXAMPLES of Usage:

1. C testing:

File: c_testing.py:


```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:38:58 2025

@author: Dhananjoy Bhuyan
"""
import pyautotranslate

pyautotranslate.init("c_testing", "c", "c")

"""pycode
define A = integer_array([
    ["item1", "item2"],
    ["item3", "item4"],
    ["item5", "item6"]
    ], type="2D array")

for i in A:
    print(A[i])
    for j in i:
        print(A[i][j])

"""

pyautotranslate.execute_code()
```
Output:

file: c_testing.c

```c
# include <stdio.h>

int main() {
    // Define a 2D array of strings
    char A[3][10][10] = {
        {"item1", "item2"},
        {"item3", "item4"},
        {"item5", "item6"}
    };

    // Loop through the 2D array
    for (int i = 0; i < 3; i++) {
        printf("%s %s\n", A[i][0], A[i][1]); // Print the row
        for (int j = 0; j < 2; j++) {
            printf("%s\n", A[i][j]); // Print each item in the row
        }
    }

    return 0;
}

```

Input:

File: html_testing.py

```python

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 23:15:17 2025

@author: Dhananjoy Bhuyan
"""

from pyautotranslate import init, execute_code

init("html_testing", ".html", "html")

"""pycode
title_of_page = "Python"

display code block(id = "code_block", content=
```python []
print("Hello World")
```).border_radius = 8px and padding = 10px
code_block.find("print").set_ID("theprinttext")

theprinttext.color = Orange

code_block.find("(", ")").color = White

code_block.background-color = Black

code_block.find('"Hello World"').color = Light Green

code_block.display = "inline-block"


"""

execute_code()
```
Output:

file: html_testing.html

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python</title>
    <style>
        #code_block {
            border-radius: 8px;
            padding: 10px;
            background-color: black;
            display: inline-block;
            color: white; /* Default text color */
            font-family: monospace;
        }
        #theprinttext {
            color: orange;
        }
        .parentheses {
            color: white;
        }
        .string {
            color: lightgreen;
        }
    </style>
</head>
<body>
    <pre id="code_block">
<span id="theprinttext">print</span><span class="parentheses">(</span><span class="string">"Hello World"</span><span class="parentheses">)</span>
    </pre>
</body>
</html>
```



# **🛠 How to Use PyAutoTranslate**  

### **1️⃣ Initialize the Translator**  
Start by importing PyAutoTranslate and setting up the output file name, extension, and target language.  

```python
import pyautotranslate

# Initialize with output file name, extension, and target language
pyautotranslate.init("translated_file", ".c", "c")
```  
#### OR
```python
from pyautotranslate import init

init("output_file_name", ".c", "c")
```
### **2️⃣ Write Your Custom-Code**  
You need to write your code inside a **`pycode` block** as shown below:  

```python
"""pycode
define numbers = [1, 2, 3, 4, 5]

for each num in numbers:
    print(num)
"""
```  

### **3️⃣ Execute and Get Your Translated Code**  
```python
pyautotranslate.execute_code()
```  

This will generate a `translated_file.c` file with the translated C code.  

---

# **📦 Installation**  

Make sure you have **Python 3** installed. Then, install the required dependency:  

```bash
pip install huggingface_hub
```  

And then we have the file named "pyautotranslate.py", you just need to download it from this here.



# Small setup needed:
### You need to setup your own hugging face api token to use the code. Here's what to do:
1. Go to <a href="https://huggingface.co">HuggingFace.co</a>
2. Sign up or Log in.
3. You'll see a profile button on the left hand side. Click on that.
4. Click on settings button in the left hand side now just below your name.
5. Navigate to "Access Tokens".
6. Enter the password if a prompt comes up asking for the password you gave in huggingface when you were logging in or signing up.
7. There should be a button for creating new tokens. Click on it.
8. Choose set mode to "fine-grained".
9. Set a token name.
10. Under "User permissions" section, you need to check 4 permissions, those are:
        - Read access to contents of all repos under your personal namespace
        - Read access to contents of all public gated repos you can access
        Under the name "Repositories"
        And :
        - Make calls to inference providers
        - Make calls to Inference Endpoints
        Under the name "Inference."
        
11. Copy the token.
12. Insert the token into line 40 in the pyautotranslate.py file, 
```python
40 | token="Your_HuggingFace_API_token"
```




---

# **🎯 The End**  
PyAutoTranslate is an innovative step toward **bridging the gap between human thinking and programming languages**. Whether you’re learning a new language, testing ideas, or just automating code translation, this tool makes it all **simple, fast, and efficient**.  

> **Created with passion by Dhananjoy Bhuyan**   

If you find this project useful, feel free to share it and improve it with your own ideas! 🚀  
