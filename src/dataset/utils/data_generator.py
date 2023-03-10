from datetime import date
from random import randint

from faker import Faker


class FakeDataGenerator:
    def __init__(self):
        self.faker = Faker()

    def get_fullname(self):
        return " ".join((self.faker.first_name(), self.faker.last_name()))

    def get_text(self, min_limit_sents, max_limit_sents):
        sentences_qty = randint(min_limit_sents, max_limit_sents)
        return self.faker.paragraph(sentences_qty)

    def get_birthday_date(self, min_year_limit, max_year_limit):
        min_age = date.today().year - max_year_limit
        max_age = date.today().year - min_year_limit
        return self.faker.date_of_birth(minimum_age=min_age, maximum_age=max_age)

    def get_email(self):
        return self.faker.email()

    def get_address(self):
        return self.faker.address()

    # street_address()

    def get_phone_number(self):
        return self.faker.phone_number()

    def get_full_domain(self):
        return self.faker.domain_name()

    def get_age(self, range_from, range_to):
        return randint(range_from, range_to)


# key_func_dict = {
#     'FN': FakeDataGenerator().get_fullname(),
#     ('EM', 'Email'),
#     ('BR', 'Birthdate'),
#     ('DM', 'Domain'),
#     ('AD', 'Address'),
#     ('PN', 'Phone number'),
#     ('AG', 'Age'),
#     ('TX', 'Text'),
# }
