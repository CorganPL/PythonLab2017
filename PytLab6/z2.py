import re

class EmailException(Exception):
    regex_email = re.compile(
      r'''(?P<adres>
        (?P<login>[\w+.]+)
        @
        (?P<domena>\w+(\.\w+)+)
      )''',
  re.IGNORECASE | re.VERBOSE)

    def verifyMail(self, mail):
        for match_object in self.regex_email.finditer(mail):
            print match_object.groupdict()


try:
    return EmailException
except EmailException as w:
    print w

class EmailList:
    emails = []
    def __init__(self, mail):
        try:
            self.emails.append(mail)
            print "Dodano " + mail
        except EmailException as ex:
            print ex
