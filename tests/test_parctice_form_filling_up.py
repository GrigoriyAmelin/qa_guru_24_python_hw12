import allure
from allure_commons.types import Severity

from demoqa.pages.registration_page import RegistrationPage


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'gamelin')
@allure.feature('Страница Practice Form')
@allure.story('Пользователь может ввести свои учетные данные и зарегистрироваться')
@allure.link('https://demoqa.com/automation-practice-form', name='Practice Form page')
@allure.title('Заполнить форму и зарегистрироваться')
def test_practice_form_filling_up():
    registration_page = RegistrationPage('Mirko',
                                         'Stojanovic',
                                         'mirko-stojanovic@srbijavoz.rs',
                                         'Male',
                                         '0682826586',
                                         '111.png')

    (
        registration_page
        .open_page()
        .should_be_open()
        .fill_first_name()
        .fill_last_name()
        .fill_user_email()
        .fill_gender()
        .fill_phone_number()
        .fill_date_of_birth('08', 'October', '1979')
        .select_subject_by_keys('e', 'English')
        .select_subject_by_keys('erc', 'Commerce')
        .select_subject_by_keys('a', 'Arts')
        .select_hobby('Reading')
        .upload_file()
        .fill_address('11545 Novi Sad, Srbija, ul. Cara Dusana, 9, sprat 2, stan 231')
        .select_state('Haryana')
        .select_city('Panipat')
    )

    (
        registration_page
        .submit_form()
        .should_have_submited_form_with_text('Thanks for submitting the form')
        .should_have_registered_user_with_data('Student Name', 'Mirko Stojanovic')
        .should_have_registered_user_with_data('Student Email', 'mirko-stojanovic@srbijavoz.rs')
        .should_have_registered_user_with_data('Gender', 'Male')
        .should_have_registered_user_with_data('Mobile', '0682826586')
        .should_have_registered_user_with_data('Date of Birth', '08 October,1979')
        .should_have_registered_user_with_data('Subjects', 'English, Commerce, Arts')
        .should_have_registered_user_with_data('Hobbies', 'Reading')
        .should_have_registered_user_with_data('Picture', '111.png')
        .should_have_registered_user_with_data('Address',
                                               '11545 Novi Sad, Srbija, ul. Cara Dusana, 9, sprat 2, stan 231')
        .should_have_registered_user_with_data('State and City', 'Haryana Panipat')
    )