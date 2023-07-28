@echo off

if exist html_report rmdir /S /Q  html_report
call ..\venv\Scripts\activate.bat
pytest  ^
--cov-config=.coveragerc ^
--cov-report term ^
--cov-report html:html_report ^
--cov=..\src\game ^
..\src\game\tests
del .coverage
call ..\venv\Scripts\deactivate.bat
:END