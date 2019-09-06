@echo off
tasklist -v | findstr /i chrome.exe
if %ERRORLEVEL% == 0 (
   echo ok
) else (
   cd D:\workspace\web_at
   start python run.py product
   start python run.py bbs


   echo run run.py is success
)
