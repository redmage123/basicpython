#!/usr/bin/env python


cart=[(1,1),(1,3),(2,5)]


def carttopolar(t):
    r = sqrt(t[0] **2 + t[1]**2)
    theta = atan(t[1]/t[0])
    return(r,theta)

polar = map(carttopolar,cart)

