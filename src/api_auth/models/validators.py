from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"\+\d{1,3}\d{8,13}",
    "Phone number must not consist of space and requires country code. eg : +12312345678"
)
