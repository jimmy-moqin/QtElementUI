import sass

with open("resource\qss\light\common.scss","r",encoding="utf-8") as f:
    css = f.read()
qss = sass.compile(string=css,output_style="compressed")
print(qss)
