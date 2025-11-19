import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
area_code, phone_number = mo.groups()
print('Phone number found: ' + phone_number)
print('Area code found:' + area_code)

question_mark = re.compile(r'Bat(wo)?man')
mo1 = question_mark.search('The adventures of Batman')

# Greedy and Non-Greedy

greedyharegex = re.compile(r'(Ha){3,5}')
mo1 = greedyharegex.search('HaHaHaHaHa')
print(mo1.group())

mo2 = nongreedyharegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyharegex.search("HaHaHaHaHa")
print(mo2.group())

vowelregex = re.compile(r'[aeiouAEIOU]')
print(vowelregex.findall('RoboCop eats baby food. BABY FOOD.'))

constantRegex = re.compile(r'[^aeiouAEIOU]')
print(constantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

robocop = re.compile(r'robocop', re.IGNORECASE)
print(robocop.findall('RoboCop is part man, part machine, all cop.'))

namesregex = re.compile(r'Agent \w+')
print(namesregex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
