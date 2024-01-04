#ZenScript by Dumo178
import os
compiledlines = []
font = "Arial"
zsreadpath = ""
while not os.path.exists(zsreadpath):
    zsreadpath = input("Enter a ZenScript file path>")
with open(zsreadpath, 'r') as file:
    file_content = file.read()
arraycode = file_content.split("\n")
for itm in arraycode:
    wordarr = itm.split(" ")
    base = wordarr[0]
    if base == "title":
        pythonisanasshole = " ".join(wordarr[1:])
        compiledlines.append(f"<title>{pythonisanasshole}</title>")
    elif base == "heading":
        pythonisanasshole = " ".join(wordarr[1:])
        compiledlines.append(f"<h1 style=\"font-family: {font};\">{pythonisanasshole}</h1>")
    elif base == "text":
        pythonisanasshole = " ".join(wordarr[1:])
        compiledlines.append(f"<p style=\"font-family: {font};\">{pythonisanasshole}</p>")
    elif base == "font":
        pythonisanasshole = " ".join(wordarr[1:])
        font = pythonisanasshole
print("Compiled successfully")
compiledtext = ""
for item in compiledlines:
    compiledtext = f"{compiledtext}{item}\n"
outputpath = input("Choose what to output as>")
with open(outputpath, 'w') as file:
    file.write(compiledtext)
