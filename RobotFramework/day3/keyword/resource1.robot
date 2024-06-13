

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