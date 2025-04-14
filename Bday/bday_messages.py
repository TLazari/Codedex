import random


def get_msg () :
    messages = ['Hope you have a very Happy Birthday! 🎈',
    'Its your special day  get out there and celebrate! 🎉',
    'You were born and the world got better – everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞']
    r_message = random.choice(messages)
    return r_message


