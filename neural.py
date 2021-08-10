#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:26:35 2021

@author: kosh
"""
from random import *
import math
def initialize(n_inputs,n_hidden,n_outputs):
    network=[]
    hidden_layer=[{'weight':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer=[{'weight':[random() for i in range(n_hidden+1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network
network=initialize(2,1,2)
#calculating activation of a neuron.
def activate(weight,inputs):
    activation=weight[-1]
    for i in range(len(weight)-1):
        activation+=weight[i]*inputs[i]
    return activation
def transfer(activation):
    return 1.0/(1.0+math.exp(-activation))
def forward_propagate(network,row):
    inputs=row
    for layers in network:
        new_inputs=[]
        for neuron in layers:
            activation=activate(neuron['weight'],inputs)
           # print(activation)
            neuron["output"]=transfer(activation)
            #print(neuron["output"])
            new_inputs.append(neuron["output"])
        inputs=new_inputs
    return inputs
row=[1,0,None]
output=forward_propagate(network, row)
print(output)
#back propagating
def transfer_derivative(output):
    return output*(1-output)
def back_propagate(network,expected):
    for i in range(reversed(network)):
        layer=network[i]
        errors=[]
        if i !=len(network)-1:
            for j in range(len(len(layer))):
                error=0.0
                for neuron in network[i+1]:
                    error+=(neuron['weight'][j]*neuron["delta"])
                errors.append(error)
                
    
