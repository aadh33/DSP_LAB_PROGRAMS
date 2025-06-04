import numpy as np
import matplotlib.pyplot as plt

def cosine(f,over,nCyc,phase):
    fs=over*f
    ts=np.arange(0,nCyc*(1/f),1/fs)
    g=np.cos(2*np.pi*f*ts+phase)
    return list(g)


fm=10
fc=30
over=20
fs=over*fc

bcd=2021
x=''.join(format(int(digit),'04b') for digit in str(bcd))

print(x)

message=[x[i:i+2] for i in range(0,len(x),2)]

mod_00=cosine(fc,over,fc/fm,np.pi/4)
mod_01=cosine(fc,over,fc/fm,3*np.pi/4)
mod_10=cosine(fc,over,fc/fm,-np.pi/4)
mod_11=cosine(fc,over,fc/fm,-3*np.pi/4)

mod=[]

for i in message:
    if i == '00':
        mod.extend(mod_00)
    elif i == '01':
        mod.extend(mod_01)
    elif i == '10':
        mod.extend(mod_10)
    elif i == '11':
        mod.extend(mod_11)
        
        
t=np.arange(0,(len(x)/2)*(1/fm),1/fs)

plt.plot(t[:len(mod)],mod)
plt.title("QPSK")
plt.grid('true')
plt.show()

       

