from faker import Faker
import random

fake = Faker('en_US')

def generate_phone_number():
    return fake.phone_number()

def generate_name_surname():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name

def generate_email_with_number(first_name, last_name):
    email_provider = random.choice(["gmail.com", "yahoo.com", "outlook.com", "example.com"])
    random_number = random.randint(100, 999)
    email = f"{first_name.lower()}.{last_name.lower()}{random_number}@{email_provider}"
    return email

def generate_usa_address():
    return fake.street_address() + ", " + fake.city() + ", " + fake.state_abbr() + " " + fake.zipcode()

for _ in range(1):
    first_name, last_name = generate_name_surname()
    email = generate_email_with_number(first_name, last_name)
    phone_number = generate_phone_number()
    address = generate_usa_address()

    print(f"Name: {first_name} {last_name}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")
    print(f"Address: {address}")
    print("=" * 30)
