*** Settings ***
Library    SeleniumLibrary
Resource    ./resource.robot    #current folder
#Resource    ../../day2/
#Resource    ./keyword/resource1.robot


*** Variables ***
${url}   https://admin-demo.nopcommerce.com/
${user}    admin@yourstore.com
${pass}    admin


*** Test Cases ***
TestCase1: Verify Dashbord page
    [tags]   tc1   sanity
    #Set Log Level   Trace
    Open Browser   url=${url}    browser=chrome    #executable_path=E:/selenium/drivers/chromedriver.exe
    Maximize Browser Window
    Login with Username and Password-with parameter   ${user}   ${pass}
    ${title}    Log Title
    Log   ${title}    console=True
    Run Keyword If    '${title}'=='Dashboard / nopCommerce administration'    Log   Dashboard page verified successful
    ...    ELSE   Fail
    Close Browser
