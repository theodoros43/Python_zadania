#!/usr/bin/python

#parser DOM

from xml.dom.minidom import parse
import xml.dom.minidom

def changeText(node, newText):
	if node.firstChild.nodeType !=node.TEXT_NODE:
		raise Exception("node does not contain text")
	node.firstChild.replaceWholeText(newText)

document = xml.dom.minidom.parse("zad_3.xml")
books = document.getElementsByTagName("book")
for book in books:
	print(" Book ")
	if book.hasAttribute("title"):
		print("Title: " + str(book.getAttribute("title")))
	author = book.getElementsByTagName('author')[0]
	print("author: " + author.firstChild.data)
	changeText(author, "Good gopnik guy")
file = open("zad_3b_modified.xml","wb")
document.writexml(file)
file.close()

