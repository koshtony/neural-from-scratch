#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 08:31:15 2021

@author: kosh
"""
def SSR(c,m,x,y):
    ssr=0
    for i in range(len(y)):
        ssr+=(y[i]-(c+x[i]*m))**2
    return ssr
def derive_ssr_c(c,m,x,y):
    der_ssr_c=0
    for i in range(len(y)):
        der_ssr_c+=-2*(y[i]-(c+x[i]*m))
    return der_ssr_c
def derive_ssr_m(c,m,x,y):
    der_ssr_m=0
    for i in range(len(y)):
        der_ssr_m+=(-2*x[i])*(y[i]-(c+x[i]*m))
        
    return der_ssr_m
def update_params(x,y,lrate):
    initial={"c":0,"m":1}
    all_used={"intercepts":[0],"slopes":[1]}
    n=0
    for i in range(100):
        dc=derive_ssr_c(initial["c"],initial["m"],x,y)
        steps_c=lrate*dc
        dm=derive_ssr_m(initial["c"],initial["m"], x, y)
        steps_m=lrate*dm
        initial["c"]=initial["c"]-steps_c
        initial["m"]=initial["m"]-steps_m
        all_used["intercepts"].append(initial["c"])
        all_used["slopes"].append(initial["m"])
        if SSR(initial["c"],initial["m"],x,y) > SSR(initial["c"],initial["m"],x,y):
            print(SSR(initial["c"],initial["m"],x,y))
            break
        #n+=1
    return all_used

x=[0.5,2.3,2.9]
y=[1.4,1.9,3.2]
print(update_params(x,y,0.01))

        