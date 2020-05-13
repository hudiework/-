REM @echo off
@echo off
set str=hudie.jpg 
for /f %%i in (a.txt) do (echo F|(xcopy %str% %%i))
