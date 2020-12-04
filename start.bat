IF NOT EXIST appJar\NUL GOTO NOAPPJAR
python main.py
pause
GOTO ENDOFSCRIPT
:NOAPPJAR
ECHO the folder appJar does not exist
tar.exe -x -f appJar.zip
echo uncompressing folder...
python main.py
del "appJar.zip"  /s /f /q
pause

:ENDOFSCRIPT
