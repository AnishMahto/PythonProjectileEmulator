#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:57:38 2018

@author: anishmahto
"""
from vpython import *

scene = canvas (title='Projectile Emulator', width=1500, height=600)
dt = 0.01
time = 0
PI = 3.14159265358979323
initX = -20
initY = -10
xAxis = []
yAxis = []


for i in range (initX, 100):
    if (i%10==0):
        xAxis.append(text(text=("%sm" % (i-initX)), pos=vec(i,initY,0), height=1))
        
for i in range (initY, 50):
    if (i%10==0):
        yAxis.append(text(text=("%sm" % (i-initY)), pos=vec(initX,i,0), height=1))

#scene.autoscale = False

force_of_gravity = 9.8

vscale = 0.1

def singleProjectile():
    ball = sphere (pos=vec(initX,initY,0), radius = 1, color=color.red, make_trail=True)
    
    force_of_gravity = 9.8
    ball.angle = 45
    ball.speed = 30
    #ball.speed = 5.4
    #ball.mass = 0.0005669905
    ball.mass = 15
    
    ball.velocity = vec(ball.speed*cos(radians(ball.angle)), ball.speed*sin(radians(ball.angle)), 0)
    
    varr = arrow(pos=ball.pos, axis=ball.velocity*vscale, color=color.yellow)
    
    
    time = 0
    dt = 0.01 
    while (time < 5):
        rate (100)
        time += dt
        
    time = 0

    while (ball.pos.y >= initY):
        rate (10)
        
        #downwards vector, w = mg
        weight_vector = vec (0, ball.mass*-force_of_gravity, 0)
        net_force = weight_vector
        acceleration = net_force/ball.mass
    
        ball.velocity = ball.velocity + acceleration * dt
        ball.pos = ball.pos + ball.velocity*dt
        
        varr.pos = ball.pos
        varr.axis = ball.velocity*vscale
    
        time = time + dt
        print (" (%sm, %sm)" % (ball.pos.x - initX, ball.pos.y - initY))            

singleProjectile()
#multipleProjectiles()
