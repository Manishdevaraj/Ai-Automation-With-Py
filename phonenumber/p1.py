import phonenumbers

number ="+918248431135"

x=phonenumbers.parse(number)
print(x)

if phonenumbers.is_valid_number(x):
    print("the number is valid")

else:
    print("the number is not valid")