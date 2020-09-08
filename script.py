# open json file
import json
bookPath = input("Relative Path of the book's info: ")
jsonFile = open(f"{bookPath}", "r")
book = json.load(jsonFile)
jsonFile.close()

# templates
from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template("toc_template.html")
output = template.render(data = book)

# generate the table of contents website
fileName = bookPath[10:].strip('.json')
filePath = 'table_of_contents/' + fileName + '.html'
with open(filePath, 'x') as webObj:
    webObj.write(output)
