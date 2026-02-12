from decimal import Decimal, ROUND_HALF_UP
from django import template

register = template.Library()


@register.filter
def display_price(value):
    """Format price without thousands separator and without unnecessary decimals.

    Examples:
    - 120.00 -> '120'
    - 89.99  -> '89.99'
    - 1000.5 -> '1000.5'
    """
    if value is None:
        return ''
    try:
        d = Decimal(value)
    except Exception:
        try:
            d = Decimal(str(value))
        except Exception:
            return value

    # If whole number, return integer form
    if d == d.quantize(Decimal('1')):
        return str(d.quantize(Decimal('1')))

    # Otherwise keep up to 2 decimal places, trim trailing zeros
    q = d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    # normalize then format without scientific notation
    s = format(q.normalize(), 'f')
    return s
