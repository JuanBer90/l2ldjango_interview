from django.test import TestCase
from l2l.templatetags.l2l import format_datetime, DATETIME_FORMAT, DATETIME_PARSE_FORMAT
from datetime import datetime


class DateTimeTemplateFilterTest(TestCase):

    def setUp(self) -> None:
        self.iso_format = "2023-04-15T08:09:10"
        self.now = datetime(2023, 4, 15, 8, 9, 10)
        self.test_data = "2023-04-15 08:09:10"

    def test_str_format(self):
        self.assertEqual(self.test_data, format_datetime(self.iso_format))

    def test_datetime_format(self):
        self.assertEqual(self.test_data, format_datetime(self.now))

    def test_wrong_str_format(self):
        self.assertEqual("Invalid Datetime Format", format_datetime("hello world"))
