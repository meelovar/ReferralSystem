import random
import string
import time


def generate_otp() -> str:
    otp_length = 4

    return "".join(random.choice(string.digits) for _ in range(otp_length))


def send_otp() -> None:
    sleep_time = random.uniform(1, 2)

    time.sleep(sleep_time)
