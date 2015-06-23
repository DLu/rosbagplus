from rosbagplus import *
import sys
from matplotlib.pyplot import *
import collections

bag = SuperBag(sys.argv[1])

T = collections.defaultdict(list)
DATA = collections.defaultdict(list)

def put(key, t, d):
    T[key].append(t)
    DATA[key].append(d)

for topic,msg,stamp in bag:
    stamp = stamp.to_sec()
    if topic == '/cmd_vel':
        put('cmd_x', stamp, msg.linear.x)
        put('cmd_z', stamp, msg.angular.z)
    elif topic == '/odom':
        put('odom_x', stamp, msg.twist.twist.linear.x)
        put('odom_z', stamp, msg.twist.twist.angular.z)
    if len(T.get('cmd_x', []))>150:
        break    

for key in T:
    plot(T[key], DATA[key], label=key)
legend()
show()        
