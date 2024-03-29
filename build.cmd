@echo off
for /f ^"usebackq^ eol^=^

^ delims^=^" %%a in (config.ini) do (
    for /f "tokens=1,2 delims==" %%b in ("%%a") do (
        set %%b=%%c
    )
)

REM You have to edit tags in the editing kit directory, so we copy from those tags to here.

echo -----------------
echo Copying from H3EK tags...
echo -----------------

for %%a in (%tag_directories%) do (
    xcopy /s /y "%h3ek%\tags\%%a\*" ".\tags\%%a\"
)

echo -----------------
echo Copying from H3EK fragments
echo -----------------

for %%a in (%structures%) do (
    xcopy /s /y "%h3ek%\data\%structures%\*_fragments.hsc" .\data\
)

echo -----------------
echo Copying to H3EK data...
echo -----------------

REM conversely, we move our data over to the editing kit directory.
xcopy /s /y .\data\* "%h3ek%\data\"