import eel
import json
eel.init("templates")

# Variables

num1 = 0
oper = ''
num2 = 0

# Functions

@eel.expose
def myfunction():
    print("Hello, World!")

@eel.expose
def LoadTheme():
    readFile = open(".\\templates\\settings.json", "rt")
    fileContent = json.loads(readFile.read()) 
    readFile.close()
    return fileContent["theme"]
    
@eel.expose
def py_changetheme(theme):
    readFile = open(".\\templates\\settings.json", "rt")
    data = json.loads(readFile.read())
    readFile.close()
    data["theme"] = theme
    writeFile = open(".\\templates\\settings.json", "wt")
    writeFile.write(json.dumps(data))

@eel.expose
def py_calculate():
    result = ""
    if oper == '+':
        result = str(num1 + num2)
    elif oper == '-':
        result = str(num1 - num2)
    elif oper == 'x':
        result = str(num1 * num2)
    elif oper == '/':
        result = str(num1 / num2)
    elif oper == 'v':
        result = str(num2 ** (1/num1))
    elif oper == '^':
        result = str(num1 ** num2)
    elif oper == '\\':
        result = str(int(num1 // num2)) + ", r = " + str(int(num1 % num2))
    history = open(".\\templates\\history.txt","at")
    history.write(f"{num1} {oper} {num2} = {result}\n")
    return result

@eel.expose
def py_takeValues(n1, op, n2):
    global num1
    global num2
    global oper
    num1 = float(n1)
    num2 = float(n2)
    oper = op

@eel.expose
def py_loadHistory():
    file = open(".\\templates\\history.txt")
    result = []
    for lines in file:
        result.append(lines)
    return result

@eel.expose
def py_clearHis():
    file = open(".\\templates\\history.txt","wt")
    file.write("")
    file.close()

eel.start("calculator.html", size=("312","602"))