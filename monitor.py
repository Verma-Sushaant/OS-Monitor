import psutil
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from collections import deque

# Number of data points to display
style.use("dark_background")
max_points = 60
cpu_usage = deque([0] * max_points, maxlen=max_points)
mem_usage = deque([0] * max_points, maxlen=max_points)
disk_usage = deque([0] * max_points, maxlen=max_points)

def update(frame):

    cpu_percent = psutil.cpu_percent(interval=0.1) # Get CPU Usage
    memory_percent = psutil.virtual_memory().percent # Get Memory Usage
    disk_percent = psutil.disk_usage('/').percent #Get Disk Usage
    
    # CPU Usage graph
    cpu_usage.append(cpu_percent)
    ax[0].clear()
    ax[0].plot(range(60,0,-1),cpu_usage,color='#ffa500')
    ax[0].set_ylim(0, 60)
    ax[0].set_xlim(max_points,0)
    ax[0].set_ylabel("CPU Usage (%)")
    ax[0].grid(color='green')
    ax[0].text(2, cpu_percent + 2, f"{cpu_percent:.1f}%", color='white', fontsize=10)
    ax[0].set_xticks(np.arange(0, max_points + 1, 5))
    ax[0].set_yticks(np.arange(0, 101, 10))
    for spine in ax[0].spines.values():
        spine.set_color('#4169E1')
        spine.set_linewidth(1.5)
    
    # Memory Usage Graph
    mem_usage.append(memory_percent)
    ax[1].clear()
    ax[1].plot(range(60,0,-1),mem_usage, color='#ffa500')
    ax[1].set_ylim(0, 60)
    ax[1].set_xlim(max_points,0)
    ax[1].set_ylabel("Memory Usage (%)")
    ax[1].grid(color='green')
    ax[1].text(2, memory_percent + 2, f"{memory_percent:.1f}%", color='white', fontsize=10)
    ax[1].set_xticks(np.arange(0, max_points + 1, 5))
    ax[1].set_yticks(np.arange(0, 101, 10))
    for spine in ax[1].spines.values():
        spine.set_color('#4169E1')  
        spine.set_linewidth(1.5)
    
    # Disk Usage Graph
    disk_usage.append(disk_percent)
    ax[2].clear()
    ax[2].plot(range(60,0,-1),disk_usage, color='#ffa500')
    ax[2].set_ylim(0, 60)
    ax[2].set_xlim(max_points,0)
    ax[2].set_ylabel("Disk Usage (%)")
    ax[2].set_xlabel("Time (frames)")
    ax[2].grid(color='green')
    ax[2].text(2, disk_percent + 2, f"{disk_percent:.1f}%", color='white', fontsize=10)
    ax[2].set_xticks(np.arange(0, max_points + 1, 5))
    ax[2].set_yticks(np.arange(0, 101, 10))
    for spine in ax[2].spines.values():
        spine.set_color('#4169E1') 
        spine.set_linewidth(1.5)

fig, ax = plt.subplots(3,1, figsize = (8,12))
anim = animation.FuncAnimation(fig, update, interval=500,cache_frame_data = False)

plt.show()
