import re

regex_pesel = re.compile(
    r'''(?P<pesel>
        (?P<rok>\d[0-9]\d[0-9])
        (?P<miesiac>\d[0]\d[1-9] | \d[1]\d[1-2])
        (?P<dzien>\d[0]\d[1-9] | \d[1-2]\d[0-9] | \d[3]\d[0-1])
        (?P<numerserii>\d[0-9]\d[0-9]\d[0-9])
        (?P<plec>\d[0-9])
        (?P<cyfrakontrolna>d[0-9])
    )''',
    re.IGNORECASE | re.VERBOSE
)

pesele = "85102412362, 88142412362, 92105412362, 95090312352, 93002412361"

for match_object in regex_pesel.finditer(pesele):
    print match_object.groupdict()
