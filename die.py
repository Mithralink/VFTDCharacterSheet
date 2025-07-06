"""Dice rolls"""
import random
from random import randint

def rolld(die):
    """Rolls dice of chosen side count"""
    return randint(1, die)


def roll_deight(numsides = 8):
    """Rolls 1d8"""
    return random.randint(1, numsides)

def roll_dsix(num_sides = 6):
    """Rolls 1d6"""
    return random.randint(1, num_sides)

def roll_dfour(num_sides = 4):
    """Rolls 1d4"""
    return random.randint(1, num_sides)
