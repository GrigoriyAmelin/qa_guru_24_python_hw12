import os

import allure
from selene import browser as br, have, by, be
from selene import command


class RegistrationPage:
    def __init__(self, user_first_name, user_last_name, user_email, user_gender, user_phone_number, file_name_to_upload):
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.email = user_email
        self.gender = user_gender
        self.phone = user_phone_number
        self.file_name = file_name_to_upload

    @allure.step("Открыть страницу Practice Form")
    def open_page(self):
        br.open('/')
        br.element('a[href="/forms"]').click()
        br.element('a[href="/automation-practice-form"]').click()
        return self

    @allure.step("Проверить, что открыта страница Practice Form")
    def should_be_open(self):
        br.element(".practice-form-wrapper").element('.text-center').should(have.text('Practice Form'))
        return self

    @allure.step("Заполить Имя")
    def fill_first_name(self):
        br.element('#firstName').type(self.first_name)
        return self

    @allure.step("Заполнить Фамилию")
    def fill_last_name(self):
        br.element('#lastName').type(self.last_name)
        return self

    @allure.step("Заполнить email")
    def fill_user_email(self):
        br.element('#userEmail').type(self.email)
        return self

    @allure.step("Заполнить Пол")
    def fill_gender(self):
        br.element(by.text(self.gender)).click().should(be.enabled)
        return self

    @allure.step("Заполнить Номер телефона")
    def fill_phone_number(self):
        br.element('#userNumber').type(self.phone)
        return self

    @allure.step("Заполнить Дату рождения")
    def fill_date_of_birth(self, day, month, year):
        br.element("#dateOfBirthInput").click()
        br.element('.react-datepicker__month-select').element(by.text(month)).click()
        br.element('.react-datepicker__year-select').element(by.text(year)).click()
        br.element('.react-datepicker__month').element(f'.react-datepicker__day--0{day}').click()
        return self

    @allure.step("Указать Предметы интереса")
    def select_subject_by_keys(self, keys, subject):
        br.element('#subjectsInput').perform(command.js.scroll_into_view).send_keys(keys)
        br.element(by.text(subject)).perform(command.js.scroll_into_view).click()
        return self

    @allure.step("Указать Хобби")
    def select_hobby(self, hobby):
        br.element(by.text(hobby)).click()
        br.element('#hobbies-checkbox-2').should(be.enabled)
        return self

    @allure.step("Загрузить Картинку")
    def upload_file(self):
        path_to_file: str = os.path.dirname(os.path.abspath(__file__))
        path_to_file_higher: str = os.path.dirname(os.path.dirname(path_to_file))
        abspath = os.path.join(path_to_file_higher, 'tests', 'resources', self.file_name)
        br.element("#uploadPicture").send_keys(abspath)
        return self

    @allure.step("Заполнить Адрес проживания")
    def fill_address(self, address):
        br.element('#currentAddress').set_value(address)
        return self

    @allure.step("Выбрать Штат проживания")
    def select_state(self, state):
        br.element('#state').click()
        br.element(by.text(state)).click()
        return self

    @allure.step("Выбрать Город проживания")
    def select_city(self, city):
        br.element('#city').click()
        br.element(by.text(city)).click()
        return self

    @allure.step("Подтвердить введенные данные Пользователя")
    def submit_form(self):
        br.element('#submit').click()
        return self

    @allure.step("Проверка Открытия формы с введенными данными")
    def should_have_submited_form_with_text(self, text):
        br.element('#example-modal-sizes-title-lg').should(have.text(text))
        return self

    @allure.step("Проверка Корректности заполнения формы введенными данными")
    def should_have_registered_user_with_data(self, field, value):
        (br.element('.table-responsive').element(by.text(field)).element('..').
         should(have.text(value)))
        return self