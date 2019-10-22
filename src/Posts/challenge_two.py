# Created by Albus Wulfric Brain Dumbledore
# Date: 8/23/2019
# Time: 20:14


def check_flag(flag_guess):
    actual_flag = "S1i2!Fs9pl"
    if flag_guess.lower() == actual_flag.lower():
        return "You have gotten the correct flag. Please move onto the next challenge. " \
               "www.hogwartslibrary.com:777/iUhS5m1Nap7vU"
    else:
        return "This flag is incorrect. Please try again."
