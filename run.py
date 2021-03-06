from subprocess import call, check_output
import matplotlib.pyplot as plt
import numpy as np

smallest = {'width': '32', 'height': '32', 'kernel_order': '3', 'nchannels': '32', 'nkernels': '64'}
small = {'width': '64', 'height': '64', 'kernel_order': '3', 'nchannels': '64', 'nkernels': '64'}
medium = {'width': '128', 'height': '128', 'kernel_order': '3', 'nchannels': '64', 'nkernels': '64'}
large = {'width': '256', 'height': '256', 'kernel_order': '3', 'nchannels': '64', 'nkernels':  '64'}
largest = {'width': '512', 'height': '512', 'kernel_order': '3', 'nchannels': '64', 'nkernels': '64'}


input_list = [smallest, small, medium, large, largest]

print("Compiling...")
call(["gcc", "-O3", "-fopenmp", "-msse4", "conv-harness.c"])

print("Running...")

t_original = []
t_optimized = []
for s in range(0, len(input_list)):
#for s in range(0, 20):
    out = check_output(["./a.out", input_list[s]['width'], input_list[s]['height'], input_list[s]['kernel_order'], input_list[s]['nchannels'], input_list[s]['nkernels']]).decode()
    print(out)
    lines = out.split('\n')[0:2]
    t_original.append(int(lines[0].split(': ')[1].split()[0]))
    t_optimized.append(int(lines[1].split(': ')[1].split()[0]))
    print("{}x faster than original\n".format(t_original[s]/t_optimized[s]))

print("Done")

print("Showing graph...")

fig, ax = plt.subplots()
index = np.arange(5)
bw = 0.35

rect1 = plt.bar(index, t_original, bw, alpha=0.7, color='r', label='Original')
rect2 = plt.bar(index + bw, t_optimized, bw, alpha=0.7, color='y', label='Optimized')

plt.xlabel('Image size')
plt.ylabel('Time (microseconds)')
plt.xticks(index, ('32*32', '64*64', '128*128', '256*256', '512*512'))
plt.legend()
plt.tight_layout()
plt.show()
