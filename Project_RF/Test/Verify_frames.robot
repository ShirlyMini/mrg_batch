*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/Keywords.robot
Variables       ../Data/data_variables.py
Variables       ../Data/xpaths.py
Suite Setup     Nop Commerce Suite Setup
Test Setup      Demo_Frames Test Setup    chrome
Test Teardown   Close All Browsers

*** Test Cases ***
TC1 Verify Frames
    Select Frame   ${xpath_frame}
    Input Text    ${xpath_frame_input}   ${input_text}
    Sleep   5s