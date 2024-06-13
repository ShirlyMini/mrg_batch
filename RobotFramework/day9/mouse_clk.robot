*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handling Mouse right clk and double clk
    Open Browser   url=https://demo.guru99.com/test/simple_context_menu.html    browser=chrome
    Maximize Browser Window
    # right click
#    Open Context Menu   xpath://span[text()='right click me']
#    Click Element    xpath://span[text()='Delete']
#
#    sleep   2s
#    ${msg} =   Handle Alert   ACCEPT
#    Log    ${msg}   console=True

    # double click

    Double Click Element   xpath://button[text()='Double-Click Me To See Alert']
    sleep   2s
    ${msg} =   Handle Alert   ACCEPT
    Log    ${msg}   console=True

    sleep   5s
