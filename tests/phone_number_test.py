import unittest

from phone_number import PhoneNumber


class PhoneNumberTest(unittest.TestCase):
    def test_1(self):
        ph = PhoneNumber("+1(858)775-2868")

        self.assertEquals("+1(858)775-2868", ph.getOriginalText())
        self.assertEquals("+18587752868",  ph.getStrippedNumber())
        self.assertEquals("(858)775-2868",  ph.getValueAsNorthAmerican())
        self.assertEquals("+1.858.775.2868",  ph.getValueAsInternational())

    def test_2(self):
        ph = PhoneNumber("+1(858)775-2868x123")

        self.assertEquals("+1(858)775-2868x123", ph.getOriginalText())
        self.assertEquals("+18587752868x123", ph.getStrippedNumber())
        self.assertEquals("(858)775-2868x123", ph.getValueAsNorthAmerican())
        self.assertEquals("+1.858.775.2868x123", ph.getValueAsInternational())

    def test_3(self):
        ph = PhoneNumber("+598.123.4567x858")

        self.assertEquals("+598.123.4567x858",ph.getOriginalText())
        self.assertEquals("+5981234567x858",ph.getStrippedNumber())
        self.assertEquals(None,ph.getValueAsNorthAmerican())
        self.assertEquals("+598.123.456.7x858",ph.getValueAsInternational())


    def test_4(self):
        ph = PhoneNumber("+27 1234 5678 ext 4")

        self.assertEquals("+27 1234 5678 ext 4",ph.getOriginalText())
        self.assertEquals("+2712345678x4",ph.getStrippedNumber())
        self.assertEquals(None,ph.getValueAsNorthAmerican())
        self.assertEquals("+27 1234 5678 ext 4",ph.getValueAsInternational())


    def test_5(self):
        ph = PhoneNumber("858-775-2868")

        self.assertEquals("858-775-2868",ph.getOriginalText())
        self.assertEquals("+18587752868",ph.getStrippedNumber())
        self.assertEquals("(858)775-2868",ph.getValueAsNorthAmerican())
        self.assertEquals("+1.858.775.2868",ph.getValueAsInternational())


