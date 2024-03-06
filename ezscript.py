# ZenScript by Dumo178
# EzScript is a fork of ZenScript :D
import os
def setup_directories():
    os.mkdir("ezproject")
    with open("ezproject/main.ez", "w") as file:
        file.write("<text>Hello, World!")
    with open("ezproject/packages.json", "w") as file:
        file.write('''
{
  "lockedpackage": "ezscript-core"
}
''')

def compile_script():
    compiledlines = []
    font = "Arial"
    zsreadpath = ""
    while not os.path.exists(zsreadpath):
        zsreadpath = input("Enter an EzScript file path>")
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
        elif base == "<lua>":
            compiledlines.append("<script type=\"application/lua\">")
        elif base == "<initlua>":
            compiledlines.append("<script src=\"https://nmsderp.is-a.dev/EzScript/scripts/fengari-web.js\"></script>")
        elif base == "<css>":
            compiledlines.append("<style>")
        elif base == "<endcss>":
            compiledlines.append("</style>")
        elif base == "<initpy>":
            compiledlines.append('<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jspython-interpreter/dist/jspython-interpreter.min.js"></script>')
        elif base == "<py>":
            compiledlines.append('<script>\nconst jsPython = window.jspython.jsPython</script>')
        elif base == "<endjs>" or base == "<endlua>" or base == "<endpy>":
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
        print("Saved in the EzScript root!")

def main():
    print("Welcome to EzScript!")
    print("1. Setup directories (init)")
    print("2. Compile script")
    print("3. Install Package Into Dir [BETA DON'T USE YET]")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        setup_directories()
        print("Directories set up successfully.")
    elif choice == "2":
        compile_script()
    elif choice == "3":
        print("This hasn't been made yet, check back soon!")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
