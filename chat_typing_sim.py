import time
import random

def sim_typing(s:str):
    for c in s:
        # print(c, end="", flush=False)
        print(c, end="", flush=True)
        delay=random.randrange(50, 200)/1000
        time.sleep(delay)

def sim_typing_word(s:str):
    words=s.split(" ")
    for w in words:
        # print(c, end="", flush=False)
        print(w, end=" ", flush=True)
        delay=random.randrange(50, 200)/1000
        time.sleep(delay)

if __name__ == '__main__':
    # s="Here are a few ideas for a 10 year old's birthday:"
    # s="ทดสอบภาษาไทย สวัสดีครับ"
    s="""A scavenger hunt with clues leading to a surprise party
A themed party such as a Harry Potter or a Minecraft party
A sleepover with friends, complete with movies, games, and a DIY spa station
A trip to an amusement park or a water park
A cooking or baking class"""
    # sim_typing(s)
    sim_typing_word(s)