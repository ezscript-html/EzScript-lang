# ZenScript by Dumo178
import os

compiledlines = []
font = "Arial"
zsreadpath = ""
while not os.path.exists(zsreadpath):
    zsreadpath = input("Enter a ZenScript file path>")
with open(zsreadpath, "r") as file:
    file_content = file.read()
arraycode = file_content.split("\n")
for itm in arraycode:
    wordarr = itm.split(" ")
    base = wordarr[0]
    if base == "title":
        argument = " ".join(wordarr[1:])
        compiledlines.append(f"<title>{argument}</title>")
    elif base == "heading":
        argument = " ".join(wordarr[1:])
        compiledlines.append(f'<h1 style="font-family: {font};">{argument}</h1>')
    elif base == "text":
        argument = " ".join(wordarr[1:])
        compiledlines.append(f'<p style="font-family: {font};">{argument}</p>')
    elif base == "font":
        argument = " ".join(wordarr[1:])
        font = argument
    elif base == "icon":
        argument = " ".join(wordarr[1:])
        compiledlines.append(
            f'<link rel="icon" href="{argument}" type="image/x-icon"/>'
        )
    elif base == "main":
        compiledlines.append("<html>")
    elif base == "endmain":
        compiledlines.append("</html>")
    elif base == "init":
        compiledlines.append("<head>")
    elif base == "endinit":
        compiledlines.append("</head>")
    elif base == "body":
        compiledlines.append("<body>")
    elif base == "endbody":
        compiledlines.append("</body>")
print("Compiled successfully")
compiledtext = ""
for item in compiledlines:
    compiledtext = f"{compiledtext}{item}\n"
outputpath = input("Choose what to output as>")
with open(outputpath, "w") as file:
    file.write(compiledtext)
