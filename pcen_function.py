#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:28:23 2017

@author: Miranda
"""
import math
import matplotlib.pyplot as plt


def func(Pcen):
    
    p = 10**Pcen
    M = 2*10**33
    G = 6.67*10**(-8)
    R = int(6.957*10**100)
    dr = 10**7
    m = 0
    
    T = 16*10**6
    L = 0
    mbar = .92*(8.3*10**(-25)) + .8*((6.64*10**(-24))/3)
    k = 1.38*10**(-16)
    
    rho = mbar*p/(k*T)
    kappa = 3*10**(-2)
    sigma = 5.67*10**(-5)
    epp = 1.08*10**(-5)
    chih = .749
    
    

    for r in range(10**5, R, dr):
    #print("T = ", T)
    #print(p, rho)
    #print(pr)
        mr = rho*4*math.pi*(r**2) #dM/dr
        pr = (-rho*G*m)/(r**2) #dp/dr
        Lr = 4*math.pi*(r**2)*epp*(chih**2)*(rho**2)*((T/(10**6))**4) #dL/dr
        Trr = -3*kappa*rho*L/(16*math.pi*sigma*4*(T**3)*(r**2)) #dT/dr
        Trc = (2/5)*(T/p)*pr
        m = m + (dr)*mr
        p = p + (dr)*pr
        if p < 1 or T < 1 or rho < 10**(-3):
            return((m/M) - 1)
            break
        rho = mbar*p/(k*T)
        if abs(Trr) > abs(Trc):
            T = T + (dr)*Trc
            #print("Tc = ", T)
        else:
            T = T + (dr)*Trr
            #print("Tr = ", T)
        L = L + (dr)*Lr

def find(xlow, xhigh, tol):

    xCHECK = func(xlow)*func(xhigh)
    
    if xCHECK < 0:
        print("range is good!")
        fhigh = func(xhigh)
        flow = func(xlow)
        for i in range (0, 10000):
            xmid = (xhigh + xlow)/2
            fmid = func(xmid)
            if fmid*flow > 0:
                xlow = xmid
                flow = fmid
            if fmid*fhigh > 0:
                xhigh = xmid
                fhigh = fmid
            print("test", xmid, func(xmid))
            if func(xmid) > -tol and func(xmid) < tol:
                print("done! Pcen is:", 10**xmid)
                return(xmid)
    
    if xCHECK > 0:
        print("range is bad")
    if xCHECK == 0:
        print("???")
        
Pcen = find(15, 20, 1.5*10**-5)

Pcen

#p = 8.431884690934281e+17

ra = []
pa = []
Ta = []
LLa = []
mMa = []
rhoa = []

con = []
rad = []

Lsol = 3.839*10**33

p = 10**Pcen
#p = 1.4748450693917164e+18
M = 2*10**33
G = 6.67*10**(-8)
R = int(6.957*10**100)
dr = 10**7
m = 0

T = 16*10**6
L = 0
mbar = .92*(8.3*10**(-25)) + .8*((6.64*10**(-24))/3)
k = 1.38*10**(-16)

rho = mbar*p/(k*T)
kappa = 3*10**(-2)
sigma = 5.67*10**(-5)
epp = 1.08*10**(-5)
chih = .75

for r in range(10**7, R, dr):
    ra.extend([r])
    pa.extend([math.log(p)])
    Ta.extend([math.log(T)])
    LLa.extend([L/Lsol])
    mMa.extend([m/M])
    rhoa.extend([math.log(rho)])
    mr = rho*4*math.pi*(r**2) #dM/dr
    pr = (-rho*G*m)/(r**2) #dp/dr
    Lr = 4*math.pi*(r**2)*epp*(chih**2)*(rho**2)*((T/(10**6))**4) #dL/dr
    Trr = -3*kappa*rho*L/(16*math.pi*sigma*4*(T**3)*(r**2)) #dT/dr radiative
    Trc = (2/5)*(T/p)*pr #dT/dr adiabatic
    m = m + (dr)*mr
    p = p + (dr)*pr
    if p < 1 or T < 1 or rho < 10**(-3):
        print("done at radius", r)
        break
    rho = mbar*p/(k*T)
    if abs(Trr) > abs(Trc):
        T = T + (dr)*Trc
        con.extend([r])
    else:
        T = T + (dr)*Trr
        rad.extend([r])
    L = L + (dr)*Lr

constart = con[0]
confin = con[-1]
radstart = rad[0]
radfin = rad[-1]

#print(con)
#print(rad)
print("Convenctive zone starting radius is:", constart, "cm and ending radius is:", confin, "cm.")

plt.plot(ra, mMa, label = "m/M vs. r")
plt.legend()
plt.show()
plt.plot(ra, pa, label = "log(P) vs. r")
plt.legend()
plt.show()
plt.plot(ra, rhoa, label = "log(rho) vs. r")
plt.legend()
plt.show()
plt.plot(ra, LLa, label = "L/Lsol vs. r")
plt.legend()
plt.show()
plt.plot(ra, Ta, label = "log(T) vs. r")
plt.legend()
plt.show()
