import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    emails = re.compile(r"[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}")
    def parse(self):
        strings = re.split(r',|\s', self.addresses)

        parsed_emails = set()
        for string in strings:
            if self.emails.fullmatch(string):
                parsed_emails.add(string)

        return sorted(list(parsed_emails))
