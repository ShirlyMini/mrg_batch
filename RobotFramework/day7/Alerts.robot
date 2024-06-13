*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
TestCase1: Verify alert
    Open Browser   url=https://the-internet.herokuapp.com/javascript_alerts    browser=chrome
    Maximize Browser Window

    # only accept the alert
#    Click Element   xpath://button[contains(text(),'Click for JS Alert')]
##    Alert Should Be Present    I am a JS Alert
#    ${msg} =   Handle Alert   ACCEPT
#    Log    ${msg}   console=True

    ##confirmation alert
#    Click Element   //button[contains(text(),'Click for JS Confirm')]
#    ${msg} =   Handle Alert   LEAVE
##    ${msg} =   Handle Alert   DISMISS
##    ${msg} =   Handle Alert   ACCEPT
#    Log    ${msg}   console=True

    ## prompt alert
    Click Element   //button[contains(text(),'Click for JS Prompt')]
    Input Text Into Alert    Welcome   action=DISMISS
    Sleep    5s

