# CollectingFilesDataApp
A small python app that search all files by extension and writes to result file

| Args | Default value | Description |
| --- | --- | --- |
| -dir | ./ | Describe the root directory where to start searching |
| -fileExt | *.java | File extension which will used in searching |
| -clean | True | Perform clean files to delete comments(java/kotlin style), packages, imports |

To build project run compile.sh 
For additional info see ``pyinstaller`` documentation here https://pyinstaller.readthedocs.io/en/stable/index.html 

# Warning!!! The executable file generates depending on the platform where you are running ``pyInstaller`` 