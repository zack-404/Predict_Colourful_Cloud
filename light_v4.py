from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import csv


def x_y(theta, height):

    x = 0.02/np.tan(theta)
    y = height

    P = [x, y]

    return P


def refract(x0, y0, index):

    sin0 = np.abs(x0)/np.sqrt(x0**2+y0**2)
    sin1 = (refrac[index])/(refrac[index+1])*sin0

    thet = np.arcsin(sin1)

    P = x_y(thet, height[index])
    x_route.append(P[0]+x_route[-1])
    y_route.append(P[1]+y_route[-1])
    
    x = np.cos(thet)
    y = np.sin(thet)

    return [x, y, thet]


x_route = []
y_route = []


refrac = []
height = [3899*0.02]

with open('csv_file/refractivity2.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    print(csv_reader)

    for line in csv_reader:

        for i in line:
            refrac.append(float(i))
        
        height.append(height[-1]+0.02)


x0 = 0.0
y0 = 0.0

with open('csv_file/cloud.csv', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        x = line['x0']
        y = line['y0']

        x0=(float(x))
        y0=(float(y))


observer = [0, 0]


vector0 = np.array([ x0, y0, 0])
vector1 = np.array([-x0, y0, 0])

x_route.append(x0)
y_route.append(y0)

refrac.reverse()

for i in range(int(y0/50), 3899-1001):

    vector1 = refract(vector1[0], vector1[1], i)


plt.plot(x_route,y_route,color='red')
plt.title('Light route')

plt.xlabel('incident route')
plt.ylabel('altitude ( 20 m )')

plt.show()


def delta(d):
    
    return (-0.40928)*np.cos(np.pi*2/365*(d+10))

def omega(t):

    return np.pi/12*(t-12)

def get_time(arr,angle):
    
    min=5
    index=-1

    for i in range(30):

        if np.abs(arr[i]-angle)<=min:
            min=np.abs(arr[i]-angle)
            index=i

    return index

fai=np.deg2rad(23.5)

print(fai)
print((360-23.5)/180*np.pi)

ti=[0 for x in range(100)]

for t in range(0,96):

    theta=np.arccos(np.sin(delta(234))*np.sin(fai)+np.cos(delta(234))*np.cos(fai)*np.cos(omega(t/4)))

    ti[t]=(theta)


for i in range(96):

    t=0
    x=str(i%4)

    match x:
        case '0':
            t=0
        case '1':
            t=15
        case '2':
            t=30
        case '3':
            t=45

print(vector1[2],get_time(ti,vector1[2]))