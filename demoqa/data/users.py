from dataclasses import dataclass

from demoqa.data import subjects
from demoqa.data.subjects import Subject


@dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birth_day: str
    birth_month: str
    birth_year: str
    subject: list[Subject] | Subject
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = Users(
    first_name='Mirko',
    last_name='Stojanovic',
    email='mirko-stojanovic@srbijavoz.rs',
    gender='Male',
    phone='0682826586',
    birth_day='08',
    birth_month='October',
    birth_year='1979',
    hobby='Reading',
    subject=[subjects.subject_english, subjects.subject_commerce, subjects.subject_arts],
    picture='111.png',
    address='11545 Novi Sad, Srbija, ul. Cara Dusana, 9, sprat 2, stan 231',
    state='Haryana',
    city='Panipat'
)