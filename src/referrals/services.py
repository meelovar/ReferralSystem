import random
import string


def generate_invite_code():
    choice_seq = string.digits + string.ascii_letters
    code_length = 6

    return "".join(random.choice(choice_seq) for _ in range(code_length))
