import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
area_code, phone_number = mo.groups()
print('Phone number found: ' + phone_number)
print('Area code found:' + area_code)

a