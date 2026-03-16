# vuf
Ein Universal-Format mit der Bezeichnung "Viktors Universal-Format"\
Lizensiert unter [GPL 3](/LICENSE)

# Herunterladen

    git clone https://github.com/viktor-chiarcos/vuf
    cd vuf

# Verpacken

    python3 ./encode.py -f <Zieldatei>.vuf -d <Ordner mit Dateien>

# Entpacken

    ./decode '<Dateienname>' '<Ordner>'

# Benutzern Informationen geben

Man kann auch Benutzerdefinierte Einstellungen anfügen. Weitere Information in der Datei [vuf.dtd](https://github.com/viktor-chiarcos/vuf/blob/main/vuf.dtd)

Ein Beispiel:

        <vuf version="0.1" name='Ein "vuf" Beispiel' labels="template;test">
        	<file name="test.txt" type="text/plain">
        		<content>
        				Ein Test
        			</content>
        		</file>
        		<dir name="test">
        			<file name="test.txt" type="text/plain">
        				<content>
        					Ein Test im Ordner "Test"
        				</content>
        			</file>
        		</dir>
        </vuf>


# Wichtige Info

Das Format **vuf** kann keine *Symbolische Links (Linux)* speichern und erzeugt stattdessen eine Datei mit dem gleichen Namen und dem gleichen Inhalt.
