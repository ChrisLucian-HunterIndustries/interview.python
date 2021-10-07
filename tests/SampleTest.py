import unittest

from approvaltests.approvals import verify

from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory

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

        # @ Test
        # public void test3() {
        # PhoneNumber ph = new PhoneNumber("+598.123.4567x858");
        #
        # assertThat("+598.123.4567x858", is (ph.getOriginalText()));
        # assertThat("+5981234567x858", is (ph.getStrippedNumber()));
        # assertThat(null, is (ph.getValueAsNorthAmerican()));
        # assertThat("+598.123.456.7x858", is (ph.getValueAsInternational()));
        # }
        #
        # @ Test
        # public void test4() {
        # PhoneNumber ph = new PhoneNumber("+27 1234 5678 ext 4");
        #
        # assertThat("+27 1234 5678 ext 4", is (ph.getOriginalText()));
        # assertThat("+2712345678x4", is (ph.getStrippedNumber()));
        # assertThat(null, is (ph.getValueAsNorthAmerican()));
        # assertThat("+27 1234 5678 ext 4", is (ph.getValueAsInternational()));
        # }
        #
        # @ Test
        # public void test5() {
        # PhoneNumber ph = new PhoneNumber("858-775-2868");
        #
        # assertThat("858-775-2868", is (ph.getOriginalText()));
        # assertThat("+18587752868", is (ph.getStrippedNumber()));
        # assertThat("(858)775-2868", is (ph.getValueAsNorthAmerican()));
        # assertThat("+1.858.775.2868", is (ph.getValueAsInternational()));
        # }
        # }

