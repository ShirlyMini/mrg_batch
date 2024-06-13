*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/Keywords.robot
Variables       ../Data/data_variables.py
Variables       ../Data/xpaths.py
Suite Setup     Nop Commerce Suite Setup
Test Setup      Nop Commerce Test Setup    chrome
#Test Setup      Nop Commerce Test Setup    ff
Test Teardown   Close All Browsers

*** Test Cases ***
TC1 Verify nopcommerce login page title
    Title Should Be   ${login_page_title}

TC2 Verify nopcommerce Dashboard page title
#    Input Text   ${xpath_user_input}     ${username}    #clear=True
#    Input Password    ${xpath_pswd_input}   ${password}
#    Click Element   ${xpath_login_button}
    Enter Username and password for nop commerce login   ${username}   ${password}
    Title Should Be    ${dashbord_page_title}

TC3 Verify nop commerce product page title
#    Input Text   ${xpath_user_input}     ${username}    #clear=True
#    Input Password    ${xpath_pswd_input}   ${password}
#    Click Element   ${xpath_login_button}
    Enter Username and password for nop commerce login   ${username}   ${password}
    Click Element   ${xpath_catalog_menu}
    Click Element   ${xpath_product_submenu}
    Title Should Be    ${product_page_title}