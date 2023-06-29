from selene import browser, have, be

def test_homework1 ():
    browser.open('/')

    browser.element('#firstName').type('Darya')
    browser.element('[placeholder="Last Name"]').type('Savina')
    browser.element('[id = "userEmail"]').type('DaryaSavina@mail.ru')



