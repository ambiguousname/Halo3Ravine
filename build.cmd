@echo off
for /f ^"usebackq^ eol^=^

^ delims^=^" %%a in (config.ini) do (
    for /f "tokens=1,2 delims==" %%b in ("%%a") do (
        set %%b=%%c
    )
)

REM You have to edit tags in the editing kit directory, so we copy those over to here.
xcopy /s /y "%h3ek%\tags\*" .\tags\
xcopy /s /y .\data\* "%h3ek%\data\"