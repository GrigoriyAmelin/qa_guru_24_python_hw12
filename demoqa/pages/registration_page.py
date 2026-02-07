from selene import browser as br, have, by, be


class RegistrationPage:

    def open_page(self):
        br.open('/automation-practice-form')
        br.driver.execute_script("$('#fixedban').remove()")
        br.driver.execute_script("$('footer').remove()")

    def should_be_open(self):
        br.element(".practice-form-wrapper").element('.text-center').should(have.text('Practice Form'))

    def fill_first_name(self, first_name: str):
        br.element('#firstName').type(first_name)

    def fill_last_name(self, last_name: str):
        br.element('#lastName').type(last_name)

    def fill_user_email(self, user_email: str):
        br.element('#userEmail').type(user_email)

    def fill_gender(self, gender):
        br.element(by.text(gender)).click().should(be.enabled)

    def fill_phone_number(self, phone_number: str):
        br.element('#userNumber').type(phone_number)

