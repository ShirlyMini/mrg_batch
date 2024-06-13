*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/Keywords.robot
Variables       ../Data/data_variables.py
Variables       ../Data/xpaths.py
Library         ../Resources/LoadData.py
Library         DataDriver    file=../Data/LoginData.xlsx    sheet_name=Sheet2
Suite Setup     Nop Commerce Suite Setup
Test Setup      Nop Commerce Test Setup    chrome
Test Teardown   Close All Browsers
Test Template   Enter Username and password for nop commerce login - Test Template

*** Test Cases ***
Verify Dashboard Page title with username ${user} and password ${pass}

*** Keywords ***
Enter Username and password for nop commerce login - Test Template
    [Arguments]   ${user}   ${pass}   ${expected}
    Enter Username and password for nop commerce login   ${user}   ${pass}
    Run Keyword If   '${expected}'=='Pass'    Title Should Be    ${dashbord_page_title}
    ...   ELSE IF      '${expected}'=='Fail'   Title Should Be    ${login_page_title}
    ...   ELSE      Fail