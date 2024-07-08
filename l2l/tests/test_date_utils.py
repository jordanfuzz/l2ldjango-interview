from django.test import TestCase
from l2l.templatetags.date_utils import format_date
from datetime import datetime


class TestFormatDate(TestCase):
    def test_date_as_string(self):
        string_date = "2024-07-01T14:30:00"
        expected = "2024-07-01 14:30:00"
        actual = format_date(string_date)
        self.assertEqual(expected, actual)

    def test_date_as_datetime(self):
        date = datetime(2024, 7, 1, 14, 30)
        expected = "2024-07-01 14:30:00"
        actual = format_date(date)
        self.assertEqual(expected, actual)

    def test_date_as_string_invalid_format(self):
        string_date = "July 1, 2024"
        expected = "Invalid date format"
        actual = format_date(string_date)
        self.assertEqual(expected, actual)