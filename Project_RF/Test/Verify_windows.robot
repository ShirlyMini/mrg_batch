*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/Keywords.robot
Variables       ../Data/data_variables.py
Variables       ../Data/xpaths.py
Suite Setup     Nop Commerce Suite Setup
Test Setup      Demo_windows Test Setup    chrome
Test Teardown   Close All Browsers

*** Test Cases ***
TC1 Verify Tabbed Windows
    Click Element    ${xpath_click_windows}
    ${handles} =    Get Window Handles
    Log   ${handles}   console=True
    Switch Window    ${handles[1]}
    Title Should Be   Selenium

#    Switch Window    ${handles[2]}
#    Title Should Be   Selenium
