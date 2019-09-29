@echo off
tasklist -v | findstr /i chrome.exe
if %ERRORLEVEL% == 0 (
   echo ok
) else (
   cd C:\Users\dellmn\Desktop\web_at
   start python run.py bbs

   start python run.py product

   echo run run.py is success
)
pause

