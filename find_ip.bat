@echo off
setlocal enabledelayedexpansion

rem Get the IP addresses
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr "IPv4"') do (
    set ip=%%a
    set ip=!ip:~1!
    
    rem Check if the IP address starts with 192, 10, or 172
    if "!ip:~0,4!"=="192." (
        set local_ip=!ip!
    ) else if "!ip:~0,3!"=="10." (
        set local_ip=!ip!
    ) else if "!ip:~0,6!"=="172.16" (
        set local_ip=!ip!
    )
)

if defined local_ip (
    echo Access the Flask app at: http://%local_ip%:5000/
) else (
    echo Could not find a valid local IPv4 address.
)

pause
endlocal
