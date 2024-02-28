# ZenScript by Dumo178
# EzScript is a fork of ZenScript :D
import os

compiledlines = []
font = "Arial"
zsreadpath = ""
while not os.path.exists(zsreadpath):
    zsreadpath = input("Enter a EzScript file path>")
with open(zsreadpath, "r") as file:
    file_content = file.read()
arraycode = file_content.split("\n")
for itm in arraycode:
    wordarr = itm.split(" ")
    base = wordarr[0]
    if base == "<title>":
        argument = " ".join(wordarr[1:])
        compiledlines.append(f"<title>{argument}</title>")
    elif base == "<heading>":
        argument = " ".join(wordarr[1:])
        compiledlines.append(f'<h1 style="font-family: {font};">{argument}</h1>')
    elif base == "<text>":
        argument = " ".join(wordarr[1:])
        compiledlines.append(f'<p style="font-family: {font};">{argument}</p>')
    elif base == "<font>":
        argument = " ".join(wordarr[1:])
        font = argument
    elif base == "<icons>":
        argument = " ".join(wordarr[1:])
        compiledlines.append(
            f'<link rel="icon" href="{argument}" type="image/x-icon"/>'
        )
    elif base == "<main>":
        compiledlines.append("<html>")
    elif base == "<endmain>":
        compiledlines.append("</html>")
    elif base == "<init>":
        compiledlines.append("<head>")
    elif base == "<endinit>":
        compiledlines.append("</head>")
    elif base == "<body>":
        compiledlines.append("<body>")
    elif base == "<endbody>":
        compiledlines.append("</body>")
    elif base == "<js>":
        compiledlines.append("<script>")
    elif base == "<css>":
        compiledlines.append("<style>")
    elif base == "<endcss>":
        compiledlines.append("</style>")
    elif base == "<endjs>":
        compiledlines.append("</script>")
    elif base == "<endetails>":
        compiledlines.append("</details>")
    elif base == "<details>":
        compiledlines.append("<details>")
    elif base == "<summary>":
        compiledlines.append("<summary>")
    elif base == "<endsummary>":
        compiledlines.append("</summary>")
    elif base == "<div>":
        compiledlines.append("<div>")
    elif base == "<enddiv>":
        compiledlines.append("</div>")
    elif base == "<tb>":
        compiledlines.append("<hr>")
    elif base == "<break>":
        compiledlines.append("<br>")
    else:
        compiledlines.append(itm)
print("Compiled successfully")
compiledtext = ""
for item in compiledlines:
    compiledtext = f"{compiledtext}{item}\n"
outputpath = input("Choose what to output as>")
with open(outputpath, "w") as file:
    file.write(compiledtext)
