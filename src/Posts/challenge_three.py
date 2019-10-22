# Created by Albus Wulfric Brain Dumbledore
# Date: 8/23/2019
# Time: 20:14


def check_flag(flag_guess):
    actual_flag = "535353535353535353262618221822182226262653"
    if flag_guess.lower() == actual_flag.lower():
        return "You have gotten the correct flag. Please send a text to (785) 813-1143 to inform us that you are done."
    else:
        return "This flag is incorrect. Please try again."
