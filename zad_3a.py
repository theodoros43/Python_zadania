#!/usr/bin/python3

# parser SAX

import xml.sax as sax
import xml.sax.saxutils as saxutils

class ContentHandler(sax.ContentHandler):
	def __init__(self):
	#	xml.sax.ContentHandler.__init__(self)
		self.data =""
		self.type = ""
		self.author = ""
	
	def startElement(self, name, attrs):
	#	print("startElement: " + name)
		self.data = name
		if name == "book":
			print("book")
			title = attrs["title"]
			print("Title: " + title)
	
	def endElement(self, name):
	#	print("endElement: " + name)
		if self.data =="type":
			print("Type: " + self.type)
		elif self.data == "author":
			print("Author: " + self.author)
			self.data = ""

	def characters(self, content):
		if self.data =="type":
			self.type = content
		elif self.data =="author":
			self.author = content

class TextChange(saxutils.XMLGenerator):
	def startElement(self, name, attrs):
		self.currentdata = name
		saxutils.XMLGenerator.startElement(self, name, attrs)
	def endElement(self, name):
		self.currentdata = ""
		saxutils.XMLGenerator.endElement(self, name)
	def characters(self, content):
		if(self.currentdata == "author"):
			saxutils.XMLGenerator.characters(self, 'niktnic')
		else:
			saxutils.XMLGenerator.characters(self, content)


parser = sax.make_parser()
parser.setContentHandler(ContentHandler())
parser.parse("zad_3.xml")

destination = open("zad_3a_modified.xml","w")
source = open("zad_3.xml","r")
sax.parse(source, TextChange(destination))
