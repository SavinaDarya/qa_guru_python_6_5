import os

from selene import browser, have, be, by

def test_homework1 ():
    browser.open('/')

    #Заполняем форму

    browser.element('#firstName').type('Darya')
    browser.element('[placeholder="Last Name"]').type('Savina')
    browser.element('[id = "userEmail"]').type('DaryaSavina@mail.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').type('9270371323')

    browser.element(by.id('dateOfBirthInput')).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('December')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1995')).click()
    browser.element('.react-datepicker__day--007').click()
    browser.element('[id="subjectsInput"]').should(be.blank).type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#currentAddress').type('Tatarstan')
    browser.element('[id="state"]').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('.btn-primary').click()

    #Проверяем форму после заполнения
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody>tr')[0].should(have.text('Darya Savina'))
    browser.all('tbody>tr')[1].should(have.text('DaryaSavina@mail.ru'))
    browser.all('tbody>tr')[2].should(have.text('Female'))
    browser.all('tbody>tr')[3].should(have.text('9270371323'))
    browser.all('tbody>tr')[4].should(have.text('07 December,1995'))
    browser.all('tbody>tr')[5].should(have.text('Maths'))
    browser.all('tbody>tr')[6].should(have.text('Sports, Reading'))
    browser.all('tbody>tr')[8].should(have.text('Tatarstan'))
    browser.all('tbody>tr')[9].should(have.text('Uttar Pradesh Agra'))
