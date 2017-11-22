import re

regex_ip = re.compile(
    r'''(?P<adres>
        (?P<oktet1>(\d[01]\d[0-9]\d[0-9] | [2\d[0-4]\d[0-9]|25\d[0-5]))
        .
        (?P<oktet1>(\d[01]\d[0-9]\d[0-9] | [2\d[0-4]\d[0-9]|25\d[0-5]))
        .
        (?P<oktet1>(\d[01]\d[0-9]\d[0-9] | [2\d[0-4]\d[0-9]|25\d[0-5]))
        .
        (?P<oktet1>(\d[01]\d[0-9]\d[0-9] | [2\d[0-4]\d[0-9]|25\d[0-5]))

    )''',
    re.IGNORECASE | re.VERBOSE
)

adresy = "'1.2.4,2', '10.15.13.66', '162.442.125.155', '128.15.0.17', '123.15.44'"

for match_object in regex_ip.finditer(adresy):
    print match_object.groupdict()
