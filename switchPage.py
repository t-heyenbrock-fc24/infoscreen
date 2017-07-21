import math

def get_speed(current, goal, width = 1280, speed = 20):
    if current < goal:
        return math.ceil(speed * (- (current - goal) * (current - goal + width + 1)) * 4 / pow(width, 2)), 0
    else:
        return math.floor(speed * ((current - goal) * (current - goal - width - 1)) * 4 / pow(width, 2)), 0
