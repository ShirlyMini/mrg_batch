*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handling Mouse drag and drop
    Open Browser   url=http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html    browser=chrome
    Maximize Browser Window

    Drag And Drop   id:box5   id:box105

    sleep 5s


Handling Mouse drag and drop offset
    [Tags]   offset
    Open Browser   url=https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/    browser=chrome
    Maximize Browser Window

    Drag And Drop By Offset    xpath://div[@id='slider-range']/span[1]    200    0
    Drag And Drop By Offset    xpath://div[@id='slider-range']/span[2]    -100    0

    sleep   5s