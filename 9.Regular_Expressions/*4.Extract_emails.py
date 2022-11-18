import re

pattern = r"(?P<user>(?<=\s)[a-zA-Z0-9]+[.,_-]?[a-zA-Z0-9]+)\@(?P<host>[a-zA-Z]+[a-zA-Z\-\.]*\.[a-zA-Z]+)"
mails = input()

valid_mails = re.finditer(pattern, mails)

for mail in valid_mails:
    group = mail.groupdict()
    print(f"{group['user']}@{group['host']}")

    
# ------------------------------------- Another Solution -----------------------------
#
# import re
#
# pattern = r"\s(([a-z0-9\.\-\_]+)@([a-z\-]+(\.[a-z]+)+)\b"
# mails = input()
#
# valid_mails = re.findall(pattern, mails)
# for email in emails:
#     print(email[0])


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives a single string and extracts all email addresses from it. Print the
# extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:
# {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
# Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
# Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"
# {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".".
# Each word consists of only letters and can have hyphens "-" between the letters.
# Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
# Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"
# Examples
# Input
#   Please contact us at: support@github.com.
# Output
# support@github.com
#   Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.
# Output
# s.miller@mit.edu
# j.hopking@york.ac.uk
# Input
#   Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home
#   or @ class. –- steve.parker@softuni.de.
# Output
# steve.parker@softuni.de
