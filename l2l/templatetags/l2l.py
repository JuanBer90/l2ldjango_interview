from django import template
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

register = template.Library()

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATETIME_PARSE_FORMAT = "%Y-%m-%dT%H:%M:%S"


@register.filter(name="l2l_dt")
def format_datetime(value):
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, DATETIME_PARSE_FORMAT)
        except Exception as e:
            logger.error(e.__str__())
            return "Invalid Datetime Format"
    return datetime.strftime(value, DATETIME_FORMAT)

