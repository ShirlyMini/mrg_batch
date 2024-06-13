

*** Keywords ***
NopCommerce Test Setup
    Open Browser   url=${url}    browser=chrome    #options=add_argument("--no-sandbox")     #executable_path=E:/selenium/drivers/chromedriver.exe
    Maximize Browser Window

NopCommerce Test teardown
    Run Keyword If Test Failed    Capture Page Screenshot   test1.png
    Close Browser

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