pyinstaller -F -n fileCollector __main__.py
mkdir "exe"
mv ./dist/fileCollector.exe ./exe/
rm -r dist
rm -r build
rm fileCollector.spec
