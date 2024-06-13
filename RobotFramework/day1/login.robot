*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TestCase1: Verify Login page title
    Open Browser   url=https://admin-demo.nopcommerce.com/    browser=chrome   #executable_path=E:\selenium\drivers\
    Maximize Browser Window
#    ${title}    Get Title
#    Log   ${title}    console=True
    ${title}    Log Title
    Log   ${title}    console=True
    Close Browser

TestCase2: Verify Dashbord page
    Open Browser   url=https://admin-demo.nopcommerce.com/    browser=chrome
    Maximize Browser Window
    Input Text   id:Email    admin@yourstore.com    clear=True
    Input Text   id:Password    admin    clear=True
    Click Element   xpath://button[@type="submit"]
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser


#python -m robot.rebot output.xml