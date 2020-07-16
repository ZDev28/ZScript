# ZScript Documenation
***
This is the ZScript IDE made with Python!
Thanks for @darkshadowshad for helping me!

[![Run on Repl.it](https://repl.it/badge/github/Zuhdi-Hacker1/Z-LANG-IDE)](https://repl.it/github/Zuhdi-Hacker1/Z-LANG-IDE)
***

1. Line
```zsc
line('Hello World!')
```
The line function will print your string or number

2. Make
```zsc
make e = "E MEME"
line(e)
```
So make will make a variable

3. If, else, elif statment
```zsc
make e = "ZDev28"
if e == "ZDev28":
    line('this word is good')
else:
    line('I don\'t like this word')
```

4. Define
```zsc
define function():
    make e = "hey"
    line(e)

function()
```
It will make a function

5. Classes
```zsc
class MyClass:
    define __init__(self):
        self.name = input('What is your name?\n> )
    define greet(self):
        line(self.name)

make myclass = MyClass()
myclass.greet();
```
6. While
```zsc
while True:
    line('E')
```
An endless loop

7. Download
```zsc
downlaod time
time.sleep(3.0)
```
It will download a library

8. For
```zsc
download random
make randomthing = random.choice(['hey', 'hello', 'hola'])
for i in range(3):
    line(randomthing)
```
A loop

9. $
```zsc
$ A comment
```
A comment

10. Take_input
```zsc
make name = take_input('What is your name\n> ')
line(f'Hi, {name}!')
```
An input
