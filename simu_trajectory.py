import numpy as np
import matplotlib.pyplot as plt
import auxiliary as aux
from matplotlib import animation, rc
#plt.style.use('ggplot')

#Problem parameters
q  = 1.6e-19
dV = 150
m  = 100*1.66e-27
dE = 0.05
L  = 0.5

dt = 10e-9
tf = 35e-6
time = [dt, tf]

x0 = np.random.normal(0.025,0.001,500)
v0 = 0
t0 = 0

masa    = np.array([12, 32, 40])*1.66e-27
ion_tr = []
ta = []
for ii in masa:
    a = q*dV/ii/dE
    tr_part = []
    t_ion = []
    for jj in x0:
        cond = [jj,v0,t0]
        pos = aux.evolve(cond,time,a,dE,L)
        tr_part.append(pos)
        pos = np.array(pos)
        ka = np.where(pos[0]<L)[0][-1]
        t_ion.append(pos[2][ka])
    ion_tr.append(tr_part)
    ta.append(t_ion)

ion_tr = np.array(ion_tr)
ta     = np.array(ta)
posy   = np.random.normal(0.5,0.02,len(x0))

# Animation 1
FRAMES = 100
N,B = np.histogram(ta[0,:]*1e6,bins=np.linspace(0,tf*1e6,FRAMES))
for ii in range(2):
    n,b = np.histogram(ta[ii+1,:]*1e6,bins=np.linspace(0,tf*1e6,FRAMES))
    N = N+n

B = B[0:-1]

fig = plt.figure(2,figsize=(10,6))
ax = plt.subplot2grid((3,1), (0,0), rowspan=2)
#ax.set(xlim=(-0.1, 0.6), ylim=(-0.1, 1.1))
part0 = ax.plot(ion_tr[0,:,0,0],posy,'o',markersize=4,color='C0')[0]
part1 = ax.plot(ion_tr[1,:,0,0],posy,'o',markersize=12,color='C1')[0]
part2 = ax.plot(ion_tr[2,:,0,0],posy,'o',markersize=20,color='C2')[0]
ax.plot([0,0],[0,1],'--',linewidth=2,color='k')
ax.plot([dE,dE],[0,1],'--',linewidth=2,color='k')
ax.plot([L,L],[0,1],'--',linewidth=2,color='k')
ax.set_xlabel('x (m)')
ax1 = plt.subplot2grid((3,1), (2,0))
line = ax1.plot(B[0],N[0],color='C0')[0]
ax1.set(xlim=(-2,tf*1e6+2),ylim=(-2,len(x0)*0.75))
ax1.set_xlabel(r'tiempo ($\mu$s)')
fig.tight_layout()

# animation function.  This is called sequentially
def animate(i):
    current_index = int(len(pos[0]) / FRAMES * i)
    part0.set_xdata(ion_tr[0,:,0,current_index])
    part1.set_xdata(ion_tr[1,:,0,current_index])
    part2.set_xdata(ion_tr[2,:,0,current_index])
    ax1.plot(B[:i],N[:i],color='C0')

# call the animator.
anim = animation.FuncAnimation(fig, animate,frames=FRAMES, interval=50)

# call our new function to display the animation
anim.save('animation.gif', writer='imagemagick')
