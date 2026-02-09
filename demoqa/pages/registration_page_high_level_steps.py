import os

from selene import browser as br, have, by, be

from demoqa.data.subjects import subject_english, subject_commerce, subject_arts
from demoqa.data.users import Users


class RegistrationPage:
    @staticmethod
    def fill_first_name(first_name):
        br.element('#firstName').type(first_name)

    @staticmethod
    def fill_last_name(last_name):
        br.element('#lastName').type(last_name)

    @staticmethod
    def fill_user_email(email):
        br.element('#userEmail').type(email)

    @staticmethod
    def fill_gender(gender):
        br.element(by.text(gender)).click().should(be.enabled)

    @staticmethod
    def fill_phone_number(phone):
        br.element('#userNumber').type(phone)

    @staticmethod
    def fill_date_of_birth(day, month, year):
        br.element("#dateOfBirthInput").click()
        br.element('.react-datepicker__month-select').element(by.text(month)).click()
        br.element('.react-datepicker__year-select').element(by.text(year)).click()
        br.element('.react-datepicker__month').element(f'.react-datepicker__day--0{day}').click()

    @staticmethod
    def select_subject_by_keys(keys, subject):
        br.element('#subjectsInput').send_keys(keys)
        br.element(by.text(subject)).click()

    @staticmethod
    def select_hobby(hobby):
        br.element(by.text(hobby)).click()
        br.element('#hobbies-checkbox-2').should(be.enabled)

    @staticmethod
    def upload_file(file_name):
        path_to_file: str = os.path.dirname(os.path.abspath(__file__))
        path_to_file_higher: str = os.path.dirname(os.path.dirname(path_to_file))
        abspath = os.path.join(path_to_file_higher, 'tests', 'resources', file_name)
        br.element("#uploadPicture").send_keys(abspath)

    @staticmethod
    def fill_address(address):
        br.element('#currentAddress').set_value(address)

    @staticmethod
    def select_state(state):
        br.element('#state').click()
        br.element(by.text(state)).click()

    @staticmethod
    def select_city(city):
        br.element('#city').click()
        br.element(by.text(city)).click()

    @staticmethod
    def submit_form():
        br.element('#submit').click()

    @staticmethod
    def should_have_submited_form_with_text(text):
        br.element('#example-modal-sizes-title-lg').should(have.text(text))

    @staticmethod
    def should_have_user_data(field, value):
        (br.element('.table-responsive').element(by.text(field)).element('..').
         should(have.text(value)))

    def open_page(self):
        br.open('/automation-practice-form')
        br.driver.execute_script("$('#fixedban').remove()")
        br.driver.execute_script("$('footer').remove()")
        br.element(".practice-form-wrapper").element('.text-center').should(have.text('Practice Form'))
        return self

    def register(self, user: Users):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_user_email(user.email)
        self.fill_gender(user.gender)
        self.fill_phone_number(user.phone)
        self.fill_date_of_birth(user.birth_day, user.birth_month, user.birth_year)
        for subject in user.subject:
            self.select_subject_by_keys(subject.keys, subject.subject)
        self.select_hobby(user.hobby)
        self.upload_file(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit_form()

    def should_have_been_registered(self, user: Users):
        self.should_have_submited_form_with_text('Thanks for submitting the form')
        self.should_have_user_data('Student Name', f'{user.first_name} {user.last_name}')
        self.should_have_user_data('Student Email', user.email)
        self.should_have_user_data('Gender', user.gender)
        self.should_have_user_data('Mobile', user.phone)
        self.should_have_user_data('Date of Birth',f'{user.birth_day} {user.birth_month},{user.birth_year}')
        self.should_have_user_data('Subjects',
                                                   f'{subject_english.subject}, {subject_commerce.subject}, {subject_arts.subject}')
        self.should_have_user_data('Hobbies', user.hobby)
        self.should_have_user_data('Picture', user.picture)
        self.should_have_user_data('Address', user.address)
        self.should_have_user_data('State and City', f'{user.state} {user.city}')