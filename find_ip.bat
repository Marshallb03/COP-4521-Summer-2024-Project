@echo off
setlocal enabledelayedexpansion

for /f "tokens=14 delims= " %%A in ('ipconfig ^| findstr /C:"IPv4 Address"') do (
    set ipAddress=%%A
    echo Local IP Address: !ipAddress!
)

endlocal
pause
