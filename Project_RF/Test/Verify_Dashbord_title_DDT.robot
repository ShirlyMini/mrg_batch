*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/Keywords.robot
Variables       ../Data/data_variables.py
Variables       ../Data/xpaths.py
Library         ../Resources/LoadData.py
Suite Setup     Nop Commerce Suite Setup
#Test Setup      Nop Commerce Test Setup    chrome
#Test Teardown   Close All Browsers
#Test Template    Enter Username and password for nop commerce login DDT

*** Test Cases ***
TC1 Verify nopcommerce Dashboard page title DDT
    [Tags]   TC1
    ${data} =   fetch_data_xl   ../Data/LoginData.xlsx
    Log    ${data}   console=True
    FOR    ${d}   IN   @{data}
        Log    ${d}   console=True
        Log    ${d[0]}   console=True   # user
        Log    ${d[1]}   console=True   # paswd
        Log    ${d[2]}   console=True   # expected
        Nop Commerce Test Setup    chrome
        Enter Username and password for nop commerce login   ${d[0]}   ${d[1]}
        Run Keyword If   '${d[2]}'=='Pass'    Title Should Be    ${dashbord_page_title}
        ...   ELSE IF      '${d[2]}'=='Fail'   Title Should Be    ${login_page_title}
        ...   ELSE      Fail
        Close All Browsers
    END

TC2 Verify nopcommerce Dashboard page title DDT-JSON
    [Tags]   TC2
    ${data} =   fetch_data_json   ../Data/logindata_json.json
    Log    ${data}   console=True
    FOR    ${d}   IN   @{data}
        Log    ${d}   console=True
        Log    ${d['user']}   console=True   # user
        Log    ${d["password"]}   console=True   # paswd
        Log    ${d["expected"]}   console=True   # expected
        Nop Commerce Test Setup    chrome
        Enter Username and password for nop commerce login   ${d["user"]}   ${d["password"]}
        Run Keyword If   '${d["expected"]}'=='Pass'    Title Should Be    ${dashbord_page_title}
        ...   ELSE IF      '${d["expected"]}'=='Fail'   Title Should Be    ${login_page_title}
        ...   ELSE      Fail
        Close All Browsers
    END

TC3 Verify nopcommerce Dashboard page title DDT-YML
    [Tags]   TC3
    ${data} =   fetch_data_yaml   ../Data/test_data_yaml.yml
    Log    ${data}   console=True
    FOR    ${d}   IN   @{data}
        Log    ${d}   console=True
        Log    ${d['user']}   console=True   # user
        Log    ${d["password"]}   console=True   # paswd
        Log    ${d["expected"]}   console=True   # expected
        Nop Commerce Test Setup    chrome
        Enter Username and password for nop commerce login   ${d["user"]}   ${d["password"]}
        Run Keyword If   '${d["expected"]}'=='Pass'    Title Should Be    ${dashbord_page_title}
        ...   ELSE IF      '${d["expected"]}'=='Fail'   Title Should Be    ${login_page_title}
        ...   ELSE      Fail
        Close All Browsers
    END