from django.test import TestCase
from l2l.templatetags.date_utils import format_date


class TestFormatDate(TestCase):
    def test_date_as_string(self):
        string_date = "2024-07-01T14:30:00"
        expected = "2024-07-01 14:30:00"
        actual = format_date(string_date)
        self.assertEqual(expected, actual)
