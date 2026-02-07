import os

from selene import browser as br, by, be, have

from demoqa.pages.registration_page import RegistrationPage


def test_practice_form_filling_up():

    registration_page = RegistrationPage()

    registration_page.open_page()
    registration_page.should_be_open()

    registration_page.fill_first_name('Mirko')
    registration_page.fill_last_name('Stojanovic')
    registration_page.fill_user_email('mirko-stojanovic@srbijavoz.rs')
    registration_page.fill_gender('Male')
    registration_page.fill_phone_number('0682826586')

    # Ввод основных данных пользователя






    # Установка даты в календаре
    br.element("#dateOfBirthInput").click()
    br.element('.react-datepicker__month-select').element(by.text('October')).click()
    br.element('.react-datepicker__year-select').element(by.text('1979')).click()
    br.element('.react-datepicker__month').element('.react-datepicker__day--008').click()

    # Выбор предмета
    br.element('#subjectsInput').send_keys('e')
    br.element(by.text('English')).click()
    br.element('#subjectsInput').send_keys('erc')
    br.element(by.text('Commerce')).click()
    br.element('#subjectsInput').send_keys('a')
    br.element(by.text('Arts')).click()

    # Выбор хобби
    br.element(by.text('Reading')).click()
    br.element('#hobbies-checkbox-2').should(be.enabled)

    # Загрузка файла
    dirname: str = os.path.dirname(os.path.abspath(__file__))
    abspath = os.path.join(dirname, 'resources', '111.png')
    br.element("#uploadPicture").send_keys(abspath)

    # Выбор адреса
    br.element('#currentAddress').set_value('11545 Novi Sad, Srbija, ul. Cara Dusana, 9, sprat 2, stan 231')
    br.element('#state').click()
    br.element(by.text('Haryana')).click()
    br.element('#city').click()
    br.element(by.text('Panipat')).click()

    br.element('#submit').click()

    # Проверка формы
    br.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    (br.element('.table-responsive').element(by.text('Student Name')).element('..').
     should(have.text('Mirko Stojanovic')))
    (br.element('.table-responsive').element(by.text('Student Email')).element('..').
     should(have.text('mirko-stojanovic@srbijavoz.rs')))
    (br.element('.table-responsive').element(by.text('Gender')).element('..').
     should(have.text('Male')))
    (br.element('.table-responsive').element(by.text('Mobile')).element('..').
     should(have.text('0682826586')))
    (br.element('.table-responsive').element(by.text('Date of Birth')).element('..').
     should(have.text('08 October,1979')))
    (br.element('.table-responsive').element(by.text('Subjects')).element('..').
     should(have.text('English, Commerce, Arts')))
    (br.element('.table-responsive').element(by.text('Hobbies')).element('..').
     should(have.text('Reading')))
    (br.element('.table-responsive').element(by.text('Picture')).element('..').
     should(have.text('111.png')))
    (br.element('.table-responsive').element(by.text('Address')).element('..').
     should(have.text('11545 Novi Sad, Srbija, ul. Cara Dusana, 9, sprat 2, stan 231')))
    (br.element('.table-responsive').element(by.text('State and City')).element('..').
     should(have.text('Haryana Panipat')))