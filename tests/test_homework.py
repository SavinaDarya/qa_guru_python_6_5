import os

from selene import browser, have, be, by

def test_homework1 ():
    browser.open('/')

    browser.element('#firstName').type('Darya')
    browser.element('[placeholder="Last Name"]').type('Savina')
    browser.element('[id = "userEmail"]').type('DaryaSavina@mail.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').type('79270371323')

    browser.element(by.id('dateOfBirthInput')).click()




