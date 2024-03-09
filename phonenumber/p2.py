# formating the phone number
import phonenumbers

from p1 import x

formate1=phonenumbers.format_number(x,phonenumbers.PhoneNumberFormat.NATIONAL)

formate2=phonenumbers.format_number(x,phonenumbers.PhoneNumberFormat.INTERNATIONAL)

print(formate1)
print(formate2)