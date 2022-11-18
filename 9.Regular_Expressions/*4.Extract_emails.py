import re

pattern = r"(?P<user>(?<=\s)[a-zA-Z0-9]+[.,_-]?[a-zA-Z0-9]+)\@(?P<host>[a-zA-Z]+[a-zA-Z\-\.]*\.[a-zA-Z]+)"
mails = input()

valid_mails = re.finditer(pattern, mails)

for mail in valid_mails:
    group = mail.groupdict()
    print(f"{group['user']}@{group['host']}")
