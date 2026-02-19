import os

from selene import browser as br, have, by, be


class RegistrationPage:
    def __init__(self, user_first_name, user_last_name, user_email, user_gender, user_phone_number, file_name_to_upload):
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.email = user_email
        self.gender = user_gender
        self.phone = user_phone_number
        self.file_name = file_name_to_upload

    def open_page(self):
        br.open('/automation-practice-form')
        br.driver.execute_script("$('#fixedban').remove()")
        br.driver.execute_script("$('footer').remove()")
        return self

    def should_be_open(self):
        br.element(".practice-form-wrapper").element('.text-center').should(have.text('Practice Form'))
        return self

    def fill_first_name(self):
        br.element('#firstName').type(self.first_name)
        return self

    def fill_last_name(self):
        br.element('#lastName').type(self.last_name)
        return self

    def fill_user_email(self):
        br.element('#userEmail').type(self.email)
        return self

    def fill_gender(self):
        br.element(by.text(self.gender)).click().should(be.enabled)
        return self

    def fill_phone_number(self):
        br.element('#userNumber').type(self.phone)
        return self

    def fill_date_of_birth(self, day, month, year):
        br.element("#dateOfBirthInput").click()
        br.element('.react-datepicker__month-select').element(by.text(month)).click()
        br.element('.react-datepicker__year-select').element(by.text(year)).click()
        br.element('.react-datepicker__month').element(f'.react-datepicker__day--0{day}').click()
        return self

    def select_subject_by_keys(self, keys, subject):
        br.element('#subjectsInput').send_keys(keys)
        br.element(by.text(subject)).click()
        return self

    def select_hobby(self, hobby):
        br.element(by.text(hobby)).click()
        br.element('#hobbies-checkbox-2').should(be.enabled)
        return self

    def upload_file(self):
        path_to_file: str = os.path.dirname(os.path.abspath(__file__))
        path_to_file_higher: str = os.path.dirname(os.path.dirname(path_to_file))
        abspath = os.path.join(path_to_file_higher, 'tests', 'resources', self.file_name)
        br.element("#uploadPicture").send_keys(abspath)
        return self

    def fill_address(self, address):
        br.element('#currentAddress').set_value(address)
        return self

    def select_state(self, state):
        br.element('#state').click()
        br.element(by.text(state)).click()
        return self

    def select_city(self, city):
        br.element('#city').click()
        br.element(by.text(city)).click()
        return self

    def submit_form(self):
        br.element('#submit').click()
        return self

    def should_have_submited_form_with_text(self, text):
        br.element('#example-modal-sizes-title-lg').should(have.text(text))
        return self

    def should_have_registered_user_with_data(self, field, value):
        (br.element('.table-responsive').element(by.text(field)).element('..').
         should(have.text(value)))
        return self