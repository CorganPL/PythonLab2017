import liczby

class Testy(object):
    def test_answer_type(self):
        assert isinstance(liczby.num2text(1),basestring)
    def test_zero(self):
        assert (liczby.num2text(0) == "zero" or liczby.num2text(0) == "Zero")
    def test_jeden(self):
        assert (liczby.num2text(1) == "jeden" or liczby.num2text(1) == "Jeden")
    def test_dwa(self):
        assert (liczby.num2text(2) == "dwa" or  liczby.num2text(2) == "Dwa")
    def test_trzy(self):
        assert (liczby.num2text(3) == "trzy" or liczby.num2text(3) == "Trzy")
    def test_trzy(self):
        assert (liczby.num2text(3) == "trzy" or liczby.num2text(3) == "Trzy")
