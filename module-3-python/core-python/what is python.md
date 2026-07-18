# What is Python?

Python is a high-level, interpreted programming language that emphasizes code readability and simplicity. It was created by Guido van Rossum and first released in 1991.

## Key Points about Python

- Interpreted language: Python code is executed line by line by the interpreter (it is converted high level language into binary level language).

- High-level language: Python abstracts away low-level details, making it easier to write and understand.

- Dynamically typed: Variable types are determined at runtime, so you do not need to declare types explicitly.

- Easy syntax: The syntax is concise and readable, which helps beginners and experienced developers.

- Object-oriented: Python supports object-oriented programming with classes and objects.

- Cross-platform: Python runs on many operating systems, including Windows, macOS, and Linux.

- Extensive standard library: Python includes many built-in modules for common programming tasks.

- Large ecosystem: Python has many third-party libraries and frameworks for web development, data science, automation, and more.


- Community support: Python has a large and active community that contributes tutorials, packages, and tools.


## Advantages of Using Python

- Easy to learn: Python has simple syntax and a gentle learning curve, ideal for beginners.

- Fast development: Python enables rapid prototyping and shorter development cycles.

- Versatile: Python is used in web development, data science, machine learning, automation, 
scripting, game development, and more.

- Readability: Python code is easy to read and maintain, which improves collaboration.

- Productivity: Python’s libraries and frameworks reduce the amount of code needed for many tasks.

- Integration: Python can integrate with other languages and tools, such as C, C++, Java, and databases.

- Strong community: A large community means lots of support, tutorials, and reusable code.

- Portability: Python programs can run on different platforms with little or no modification.

- Open source: Python is free to use and distribute, with an open-source license.

**examples : python , php , java , android etc**

# how to download and check python is install or not 

1. https://www.python.org/downloads/ 

2. cmd : py 

E:\data_science_data_analytics-tts2pm\module-3-python\core-python>py
Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

3. How to run python 

1. script method 
**examples.py**
```
#print name 
name="hello meet"
print(name)

```
2. terminal method (REPL method)

**REPL : read | evaluate | print | loop**

```
# Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> name="meet"
# >>> print(name)
# meet
# >>> a=10
# >>> b=20
# >>> c=a+b
# >>> print("additions of numbers is ",c)
# additions of numbers is  30
# >>>

```
# how to print or check version of python ......

1. using terminal 

```
E:\data_science_data_analytics-tts2pm\module-3-python\core-python>python
Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

2. script method to used to check version of python via python script file

   a) sys
   b) plateform


   ```
   import sys
   # print version 
   print("python version is :",sys.version_info)

   or 

   import platform
   # check version 
   # print("Version is :",platform.version)
   print("Version is :",platform.python_version()) 
   
   ```


# what is print() ?

  1. print is a inbuilt function that can be print any values in python 
  2. print() return a single value
  3. print() is inbuilt function of python 
  
  ```
  name="brijesh kumar pandey"
  print(name)

  ```

# comments in python 

  1. single line comments
     examples : # hey brijesh

  2. multi line comments
     examples : 
     """
      name="hi i am brijesh" 
      print(name)
     """ 


# what is python operator ? 

  