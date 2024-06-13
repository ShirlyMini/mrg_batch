# waits
# selenium Speed
#selenium timeout--explicit wait
# selenium implicit wait

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://admin-demo.nopcommerce.com/
&{cred_dict}    user=admin@yourstore.com   pass=admin

*** Test Cases ***
TestCase1: Select unordered list
    Open Browser   url=${url}    browser=chrome    #executable_path=E:/selenium/drivers/chromedriver.exe
    Maximize Browser Window
    ${timeout1} =    Get Selenium Implicit Wait
    Log    ${timeout1}   console=True
    Set Selenium Implicit Wait   10s
    ${timeout2} =    Get Selenium Implicit Wait
    Log    ${timeout2}   console=True

    Input Text   id:Email    ${cred_dict['user']}    clear=True
    Input Text   id:Password    ${cred_dict['pass']}    clear=True
    Click Element   xpath://button[@type="submit"]
    Title Should Be    Dashboard / nopCommerce administration
    # unordered list
#    Sleep   5s
    Click Element   xpath://ul[@role='menu']/li/a/p[contains(text(),'Sales')]
#    Sleep   5s
    Click Element   xpath://p[contains(text(),'Orders')]
    Title Should Be    Orders / nopCommerce administration

    # list with select tag
    Select From List By Label    id:WarehouseId    Warehouse 2 (Los Angeles)
    List Selection Should Be    id:WarehouseId    Warehouse 2 (Los Angeles)



    Select from List By Value    id:PaymentMethodSystemName    Payments.PayPalCommerce
    List Selection Should Be    id:PaymentMethodSystemName    PayPal Commerce

    Select from List By Index    id:BillingCountryId    1    # 0 to n-1
#    Page Should Contain List    id:BillingCountryId
    List Selection Should Be    id:BillingCountryId    United States