*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}   https://admin-demo.nopcommerce.com/
&{cred_dict}    user=admin@yourstore.com   pass=admin


*** Test Cases ***
TestCase1: Verify Dashbord page
    Open Browser   url=${url}    browser=chrome    #executable_path=E:/selenium/drivers/chromedriver.exe
    Maximize Browser Window
#    Input Text   id:Email    ${cred_dict['user']}    clear=True
#    Input Text   id:Password    ${cred_dict['pass']}    clear=True
#    Click Element   xpath://button[@type="submit"]
    Login with Username and Password-basic
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser

TestCase2: Verify Dashbord page with parameter
    Open Browser   url=${url}    browser=chrome
    Maximize Browser Window
    Login with Username and Password-with parameter   ${cred_dict['user']}   ${cred_dict['pass']}
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser

TestCase3: Verify Dashbord page with return
    Open Browser   url=${url}    browser=chrome
    Maximize Browser Window
    ${verify_title}   Login with Username and Password-with return   ${cred_dict['user']}   ${cred_dict['pass']}
    Run Keyword If    '${verify_title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser

*** Keywords ***
Login with Username and Password-basic
    Input Text   id:Email    ${cred_dict['user']}    clear=True
    Input Text   id:Password    ${cred_dict['pass']}    clear=True
    Click Element   xpath://button[@type="submit"]

Login with Username and Password-with parameter
    [Arguments]    ${username}   ${password}
    Input Text   id:Email    ${username}    clear=True
    Input Text   id:Password    ${password}    clear=True
    Click Element   xpath://button[@type="submit"]


Login with Username and Password-with return
    [Arguments]    ${username}   ${password}
    Input Text   id:Email    ${username}    clear=True
    Input Text   id:Password    ${password}    clear=True
    Click Element   xpath://button[@type="submit"]
    ${title}    Log Title
    Log   ${title}    console=True
#    [Return]   ${title}
    RETURN   ${title}