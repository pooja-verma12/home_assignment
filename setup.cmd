@echo off
setlocal ENABLEDELAYEDEXPANSION
PATH=C:\Python27

echo.
rem echo Miniconda-64bit Py2.7 Console
echo.
echo.
cd C:\

rem echo Miniconda-64bit Py2.7 setup......


python -m pip install –upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python -m pip install -U pytest


cmd
