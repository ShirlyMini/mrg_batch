*** Settings ***
Library  SeleniumLibrary
Variables  ../Data/data_variables.py

*** Keywords ***
Nop Commerce Suite Setup
    Set Log Level   TRACE
    ${speed} =    Get Selenium Speed
    Log    ${speed}    console=True
    Set Selenium Speed	  0.5 seconds
    ${speed} =    Get Selenium Speed
    Log    ${speed}    console=True


Nop Commerce Test Setup
    [Arguments]    ${web_browser}
    Open Browser   url=${url}    browser=${web_browser}
    Maximize Browser Window

Demo_windows Test Setup
    [Arguments]    ${web_browser}
    Open Browser   url=${demo_url}    browser=${web_browser}
    Maximize Browser Window

Demo_Frames Test Setup
    [Arguments]    ${web_browser}
    Open Browser   url=${demo_url2}    browser=${web_browser}
    Maximize Browser Window


Enter Username and password for nop commerce login
    [Arguments]   ${user}   ${pass}
    Input Text   ${xpath_user_input}     ${user}    #clear=True
    Input Password    ${xpath_pswd_input}   ${pass}
    Click Element   ${xpath_login_button}

Enter Username and password for nop commerce login DDT
   [Arguments]    ${user}   ${pass}   ${expected}
    Nop Commerce Test Setup    Chrome
   Enter Username and password for nop commerce login   ${user}   ${pass}
   Run Keyword If   '${expected}'=='Pass'    Title Should Be    ${dashbord_page_title}
   ...   ELSE IF      '${expected}'=='Fail'   Title Should Be    ${login_page_title}
   ...   ELSE      Fail
   Close All Browsers


