import numpy as np
import matplotlib.pyplot as plt
import time


n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

nh=len(h)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)

y = np.zeros(nx+nh-1)
start = time.time()
for k in range(0,nx+nh-1):
	for n in range(0,nx):
		if k-n >= 0 and k-n < nh:
			y[k]+=x[n]*h[k-n]
end=time.time()
print(end-start)
