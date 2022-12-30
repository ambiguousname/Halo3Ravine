@echo off
for /f ^"usebackq^ eol^=^

^ delims^=^" %%a in (config.ini) do (
    for /f "tokens=1,2 delims==" %%b in ("%%a") do (
        set %%b=%%c
    )
)

xcopy /s /y .\tags\* "%h3ek%\tags\"
xcopy /s /y .\data\* "%h3ek%\data\"