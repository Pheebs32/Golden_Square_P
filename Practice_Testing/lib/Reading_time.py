import math

def reading_time(text: str):
    reading_speed = 200
    # text / readingspeed = length of time (as an int)
    length = len(text.split(" "))
    count = 0
    
    if length == 1:
        if text == "":
            return 0
        return 1
    
    # now that edge cases have been handled,
    # remove one from length
    length -= 1

    while length > 0:
        count += 1
        length -= reading_speed

    return count
