*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/Keywords.robot
Variables       ../Data/data_variables.py
Variables       ../Data/xpaths.py
Suite Setup     Nop Commerce Suite Setup
Test Setup      Nop Commerce Test Setup    chrome
Test Teardown   Close All Browsers

*** Test Cases ***
TC1 Search by Email
    Enter Username and password for nop commerce login   ${username}   ${password}
    Title Should Be    ${dashbord_page_title}
    Click Element   ${xpath_customers_menu}
    Click Element   ${xpath_customers_submenu}
    Title Should be    ${customer_page_title}

    Input Text   ${xpath_search_email}   ${email_search}
    Click Element    ${xpath_serach_button}
    Sleep    3s
#    ${table_data} =   Get Table Cell    ${xpath_email_column}   2   2
#    Log   ${table_data}    console=True
    Table Cell Should Contain   ${xpath_email_column}   2   2   ${email_search}


TC2 Search by First Name
    Enter Username and password for nop commerce login   ${username}   ${password}
    Title Should Be    ${dashbord_page_title}
    Click Element   ${xpath_customers_menu}
    Click Element   ${xpath_customers_submenu}
    Title Should be    ${customer_page_title}

    Input Text   ${xpath_search_fname}   ${fname_search}
    Click Element    ${xpath_serach_button}
    Table Cell Should Contain   ${xpath_email_column}   2   3   ${fname_search}

TC3 Search by Last Name
    Enter Username and password for nop commerce login   ${username}   ${password}
    Title Should Be    ${dashbord_page_title}
    Click Element   ${xpath_customers_menu}
    Click Element   ${xpath_customers_submenu}
    Title Should be    ${customer_page_title}

    Input Text   ${xpath_search_lname}   ${lname_search}
    Click Element    ${xpath_serach_button}
    Table Cell Should Contain   ${xpath_email_column}   2   3   ${lname_search}

TC4 Search By role
    [Tags]    TC4
    Enter Username and password for nop commerce login   ${username}   ${password}
    Title Should Be    ${dashbord_page_title}
    Click Element   ${xpath_customers_menu}
    Click Element   ${xpath_customers_submenu}
    Title Should be    ${customer_page_title}

    Click Element   ${xpath_role_remove_regsiter}
    Select From List By Label    ${xpath_select_role}    ${role_search}
    Click Element    ${xpath_serach_button}
    Scroll Element Into View   ${xpath_email_column}

    Table Column Should Contain    ${xpath_email_column}   4   ${role_search}



