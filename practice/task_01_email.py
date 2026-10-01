from email_validator import validate_email, EmailNotValidError


def is_valid_email(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


assert is_valid_email("test@gmail.com") is True
assert is_valid_email("test@mail.co.uk") is True
assert is_valid_email("testgmail.com") is False
assert is_valid_email("@gmail.com") is False
assert is_valid_email("test@@gmail.com") is False
assert is_valid_email("test@gmail") is False
assert is_valid_email("test@.com") is False
assert is_valid_email("te st@gmail.com") is False
assert is_valid_email("") is False