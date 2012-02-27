#!/usr/bin/python env

def point_in_box(pt, box):
    x,y = pt
    bx,by,w,h = box
    return (x >= bx) and (x < bx+w) and (y >= by) and (y < by+h)


