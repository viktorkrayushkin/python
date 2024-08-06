import numpy as np
import matplotlib.pyplot as plt

#Input voltage amplitude
AMP = 21.0

#Active components
r1 = 2000.0; r2 = 10.0; r3 = 10.0; r4 =2000.0;

#Reactive components
c=0.0001; l=0.06;

#Time components
T=0.01; t0=0.0; step=T/1000;
tf=T*10

steps=int(tf/step);

#Input voltage
def E(t):
    n=int(t/T)
    if ((t >= n*T )and(t <= n*T + T/2)):
        return AMP
    else:
        return 0.0


time = np.arange(t0, tf, step)

ul = []; il = []; uc = []; ic = []; y = [];

for i in range(0, steps, 1):
    y.append(E(time[i]))

def dIl_dt(t):
    return float((1.0/l)*(E(t) - (r1/((r1+r2)*(r3+r4)+r3*r4) * (il[int(t/step)]*(r2*(r3+r4)+r3) - uc[int(t/step)]*r3))))

def dUc_dt(t):
    return float((1.0/c)* (r3/(r3+r4)) * (il[int(t/step)]-(E(t)-ul[int(t/step)])/r1 - uc[int(t/step)]/r3))

#Start condition
ul.append(E(0)); il.append(0.0); uc.append(0.0); ic.append(0.0);

#Euler method
for i in range(1, steps, 1):
    il.append(il[i-1] + step*dIl_dt(time[i-1]))
    uc.append(uc[i-1] + step*dUc_dt(time[i-1]))
    ul.append(l*dIl_dt(time[i]))
    ic.append(c*dUc_dt(time[i]))

plt.figure("charts")
e = plt.subplot(311)
e.plot(time, y)
e.set_xlabel('time (s)')
e.set_ylabel('E(t), (V)', color='b')
plt.grid(True)

UL = plt.subplot(312)
UL.plot(time, ul)
UL.set_xlabel('time (s)')
UL.set_ylabel('Ul(t), (V)', color = 'b')

IL = UL.twinx()
IL.plot(time, il, 'r')
IL.set_ylabel('Il(t), (A)', color = 'r')
plt.grid(True)

UC = plt.subplot(313)
UC.plot(time, uc)
UC.set_xlabel('time (s)')
UC.set_ylabel('Uc(t), (V)', color = 'b')

IC = UC.twinx()
IC.plot(time, ic, color = 'r')
IC.set_ylabel('Ic(t), (A)', color = 'r')
plt.grid(True)

plt.show()
