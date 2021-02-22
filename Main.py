import json
import pygame as pg
import keyboard as key
import random

pg.init()
size = (700,700)
screen = pg.display.set_mode((size))
surface = pg.Surface((size))
file = open('coordinate.txt','r')
points = json.load(file)
file = open('coordinate.txt','r')
coords = json.load(file)

def NearstPoints(points):
    for i in range(1,len(points)):
        distance = (points[0][0] - points[i][0])**2 + (points[0][1] - points[i][1])**2
        if i == 1:
            short_dis = distance
            index = i
        elif short_dis > distance:
            short_dis = distance
            index = i
    return index
def Connect(points):
    temp = points
    result = []
    for i in range(len(points)-1):
        index = NearstPoints(temp)
        result.append(temp[0])
        temp[0] = temp[index]
        temp.pop(index)
    result.append(temp[0])
    return result

sorted_list = Connect(points)
print(coords)
print(sorted_list)

clock = 0
pointer = 0
point = sorted_list
while True:
    if key.is_pressed("q"):
        break
    elif key.is_pressed("w"):
        surface.fill((0,0,0))
        screen.blit(surface,(0,0))
        pg.display.flip()
        point = coords
    elif key.is_pressed('e'):
        surface.fill((0, 0, 0))
        screen.blit(surface,(0,0))
        pg.display.flip()
        point = sorted_list
    screen.fill((0,0,0))
    pg.draw.line(surface, (random.randrange(50,250,20),random.randrange(50,250,20),random.randrange(50,250,20)), point[pointer-1], point[pointer])
    screen.blit(surface,(0,0))
    pg.display.flip()
    clock += 1
    clock %= 10
    if clock == 0:
        pointer += 1
        pointer %= len(sorted_list)
