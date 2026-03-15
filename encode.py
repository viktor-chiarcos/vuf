#!/bin/python3

import argparse
import lxml.etree as etree
from os import system as sh
import os,base64

def view(content):
	print(content)

parser = argparse.ArgumentParser(description='Encoder-Skript für "vuf"-Dateien')
parser.add_argument('-f','--file',required=True, help='Gewählte "vuf" Datei (sollte nicht existieren) ')
parser.add_argument("-d","--directory",required=True, help='Gewähltes Zielverzeichnis (sollte existieren und nicht leer sein.) von <bash $2>')
args = parser.parse_args()

doc=etree.XML(f'''<?xml version="1.0"?>
	<!DOCTYPE vuf SYSTEM "vuf.dtd">
	<vuf version="0.1"/>
	''')
vuf=doc.xpath("/vuf")[0]

#vuf.append(etree.Element("file",name="test.txt"))

mein_inhalt=[ f"{args.directory}/{file}" for file in os.listdir(args.directory) ]
nr=0
while nr<len(mein_inhalt):
	if os.path.isdir(mein_inhalt[nr]):
		dirname=mein_inhalt[nr]
		mein_inhalt=mein_inhalt+[ f"{dirname}/{file}" for file in os.listdir(dirname)]
		#vuf.append(etree.Element("dir",name=dirname))
	nr=nr+1
mein_inhalt.sort()
#print(mein_inhalt)
"""
vor
"""
for i in mein_inhalt:
	path=i.split(f"/")
	# view(path)
	node=vuf
	while(len(path)>1 or (len(path)>0 and os.path.isdir(path[0]))):
		next_nodes=node.xpath(f"dir[@name='{path[0]}']")
		if len(next_nodes)==0:
			node.append(etree.Element("dir",name=path[0]))
		next_nodes=node.xpath(f"dir[@name='{path[0]}']")
		node=next_nodes[0]
		path=path[1:]
	if len(path)==1 and os.path.isfile(i):
		node.append(etree.Element("file",name=path[0]))
		node=node.xpath(f"file[@name='{path[0]}']")[0]
		node.append(etree.Element("content"))
		
		node=node.xpath(f"content")[-1]		
		try: 
			with open(i,"rt") as inhalt:
				text=inhalt.read()
				node.text=text
		except UnicodeDecodeError:
			with open(i,"rb") as inhalt:
				zeichen=inhalt.read()
				text=base64.b64encode(zeichen)
				node.text=text
				parent=node.xpath("..")[0]
				parent.attrib["type"]=f"application/octet-stream"

			
with open(args.file,"wt") as datei:
	datei.write(f'<?xml version="1.0"?>\n{etree.tostring(doc).decode("utf-8")}')


