class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())

    
# ------------------------------------- Problem to resolve ------------------------------
#
# Create class Email. The __init__ method should receive sender, receiver and a content. It should also have
# a default set to False attribute called is_sent. The class should have two additional methods:
# ⦁	send() - sets the is_sent attribute to True
# ⦁	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver, and the third one – the content.
# On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
# Call the send() method for the given indices of emails. For each email, call the get_info() method.
# Note: submit all of your code, including the class
# Input	                            Output
# Peter John Hi,John                Peter says to John: Hi,John. Sent: True
# John Peter Hi,Peter!              John says to Peter: Hi,Peter!. Sent: False
# Katy Lilly Hello,Lilly            Katy says to Lilly: Hello,Lilly. Sent: True
# Stop
# 0, 2
# --------------------------------------------------------------------------------
# Anna, Bella, Hi                   Anna, says to Bella,: Hi. Sent: True
# Sam, Dany, Okey                   Sam, says to Dany,: Okey. Sent: False
# Felix, Mery, Bye                  Felix, says to Mery,: Bye. Sent: False
# Stop
# 0
