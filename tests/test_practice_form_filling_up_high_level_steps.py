from demoqa.data.users import user
from demoqa.pages.registration_page_high_level_steps import RegistrationPage


def test_practice_form_filling_up_high_level_steps():
    registration_page = RegistrationPage()
    registration_page.open_page()
    registration_page.register(user)
    registration_page.should_have_been_registered(user)