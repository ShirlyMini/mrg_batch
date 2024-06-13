*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
TestCase1: Verify alert
    Open Browser   url=https://demo.automationtesting.in/Frames.html    browser=chrome
    Maximize Browser Window

#    Select Frame    id:singleframe
#    Input Text   xpath://input[@type='text']    Welcome
#    Sleep    5s

    Click Element   xpath://a[text()="Iframe with in an Iframe"]

    Select Frame   xpath://div[@id="Multiple"]/iframe
    Select Frame   xpath://div[@class="iframe-container"]/iframe
    Input Text   xpath://input[@type='text']    Welcome
    Unselect Frame   #move to main frame
    Click Element   xpath://a[text()="Single Iframe "]
    Sleep    5s
