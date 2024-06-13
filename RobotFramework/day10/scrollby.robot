*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handling Mouse events- scroll by
    Open Browser   url=https://www.myntra.com/tops    browser=chrome
    Maximize Browser Window

    #Scroll Element Into View    xpath=//a[contains(text(), "A Flipkart company")]

    Execute Javascript   window.scrollBy(0, document.body.scrollHeight);
    sleep    5s
    Execute Javascript   window.scrollBy(0, -document.body.scrollHeight);

    sleep    10s


