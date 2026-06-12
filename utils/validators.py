"""
utils/validators.py

Validation Functions
"""

import re


def validate_email(email):

    pattern = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )

    return bool(
        re.match(
            pattern,
            email
        )
    )


def validate_url(url):

    pattern = (
        r'^(http|https)://'
        r'([A-Za-z0-9.-]+)'
    )

    return bool(
        re.match(
            pattern,
            url
        )
    )


def validate_phone(phone):

    phone = str(phone)

    return (
        phone.isdigit()
        and len(phone) >= 10
    )


def validate_year(year):

    try:

        year = int(year)

        return (
            2000 <= year <= 2100
        )

    except:
        return False


def validate_dataframe(df):

    return (
        df is not None
        and len(df) > 0
    )


def validate_college_name(name):

    return (
        isinstance(name, str)
        and len(name.strip()) > 2
    )
