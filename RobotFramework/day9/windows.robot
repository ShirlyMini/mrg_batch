*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handling multiple windows
    Open Browser   url=https://www.facebook.com/    browser=chrome
    Maximize Browser Window

    sleep   2s

    Open Browser   url=https://www.geeksforgeeks.org/    browser=chrome
    Maximize Browser Window

    sleep   2s

    Close Browser

    sleep   5s