#!/bin/python3

import argparse
import lxml.etree as etree
from os import system as sh
import os

parser = argparse.ArgumentParser(description='Fortsetzung zu decode')
parser.add_argument('-f','--file',required=True, help='Gewählte "vuf" Datei (sollte existieren) ')
parser.add_argument('-d','--directory',required=True, help='Gewähltes Zielverzeichnis (sollte existieren und leer sein.) von <bash $2>')
#parser.add_argument('--value', required=True, default="[echo.v] Fehler: Argument --value erforderlich", help='Text in Anführungszeichen ("") angeben')
args = parser.parse_args()

doc=etree.parse(args.file)
for file in doc.xpath("//file"):
	path="/".join(file.xpath(".//ancestor-or-self::*[name()='file' or name()='dir']/@name"))
	text="\n".join(file.xpath(".//content/text()"))
	text= "\n".join([ zeile.lstrip() for zeile in text.split("\n")])
	print(path)
	print(f"vuf-Datei {args.file}:\n{text}")
	print()
	sh(f"""mkdir -p {args.directory}/`dirname {path}`""")
	with open(f"{args.directory}/{path}","wt") as datei:
		datei.write(text)
print("Fertig")