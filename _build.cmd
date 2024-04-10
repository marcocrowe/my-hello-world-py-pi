REM Delete the old build folder
rmdir /s /q dist
REM Build the package
python -m build
