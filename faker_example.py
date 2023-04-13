import fake as fake
from faker import Faker

faker = Faker()
print(faker.name())
print(faker.address())
print(faker.zipcode())
print(faker.locale())
print(faker.phone_number())

print(fake.first_name())
print(fake.last_name())



for _ in range(10):
    print(faker.unique.random_int(min=1, max=10))

print(f'Date of birth: {faker.date_of_birth()}')
print(f'Century: {faker.century()}')
print(f'Year: {faker.year()}')
print(f'Month: {faker.month()}')
print(f'Month name: {faker.month_name()}')
print(f'Day of week: {faker.day_of_week()}')
print(f'Day of month: {faker.day_of_month()}')
print(f'Time zone: {faker.timezone()}')
print(f'AM/PM: {faker.am_pm()}')















