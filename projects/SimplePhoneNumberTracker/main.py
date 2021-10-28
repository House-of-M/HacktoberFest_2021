import phonenumbers

from yourNumber import number

from phonenumbers import geocoder

country_num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(country_num, "en"))

from phonenumbers import carrier
service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))



