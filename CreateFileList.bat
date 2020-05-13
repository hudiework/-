REM @echo off
@echo off

set name=a.txt
set time=ÕÅÐ¡Ò»
set number=_1383977
set exc=.jpg
for /l %%i in (10000,1,4000) do (
echo %time%%%i%number%%%i%exc% >>%name%
)
