*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handling Mouse hover
    Open Browser   url=https://www.geeksforgeeks.org/    browser=chrome
    Maximize Browser Window

    Mouse Over   xpath://span[text()='Courses']
    sleep   2s
    Click Element   xpath://a[text()='Coding for Everyone']

    sleep   5s

    Close All Browsers