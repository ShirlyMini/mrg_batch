*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handling tabbed windows
    Open Browser   url=https://demo.automationtesting.in/Windows.html    browser=chrome
    Maximize Browser Window
    # tabbed window
    Click Element    xpath://button[@class='btn btn-info']
    Switch Window   Selenium
    Click Element    xpath://span[contains(text(),'Downloads')]
    #Close Window

    # seperate window
    Switch Window   MAIN
    Click Element   xpath://a[contains(text(),'Open New Seperate Windows')]
    Click Element    xpath://button[@class='btn btn-primary']

    Switch Window   NEW
    Sleep   2s
    Click Element    xpath://span[contains(text(),'Downloads')]
    ${handles} =    Get Window Handles
    Log to Console   ${handles}
    Switch Window    ${handles[2]}
    Close Browser

#    Close All Browsers

#    Close Window

    Sleep   5s