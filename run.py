from subprocess import call, check_output
import matplotlib.pyplot as plt
import numpy as np

smallest = {
            'width':        '64',
            'height':       '64',
            'kernel_order': '3',
            'nchannels':    '64',
            'nkernels':     '64'
        }

small = {
            'width':        '64',
            'height':       '64',
            'kernel_order': '3',
            'nchannels':    '64',
            'nkernels':     '128'
        }

medium = {
            'width':        '64',
            'height':       '64',
            'kernel_order': '3',
            'nchannels':    '64',
            'nkernels':     '256'
        }

large = {
            'width':        '64',
            'height':       '64',
            'kernel_order': '3',
            'nchannels':    '64',
            'nkernels':     '512'
        }

largest = {
            'width':        '64',
            'height':       '64',
            'kernel_order': '3',
            'nchannels':    '64',
            'nkernels':     '1024'
        }

f = open("data.txt", "w")

print("Compiling...")
call(["gcc", "-O3", "-fopenmp", "-msse4", "conv-harness.c"])

print("Running...")

t_original = [0, 0, 0, 0, 0]
t_optimized = [0, 0, 0, 0, 0]

out = check_output(["./a.out", smallest['width'], smallest['height'], smallest['kernel_order'], smallest['nchannels'], smallest['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[0] = int(lines[0].split(': ')[1].split()[0])
t_optimized[0] = int(lines[1].split(': ')[1].split()[0])

print("1/5")

out = check_output(["./a.out", small['width'], small['height'], small['kernel_order'], small['nchannels'], small['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[1] = int(lines[0].split(': ')[1].split()[0])
t_optimized[1] = int(lines[1].split(': ')[1].split()[0])

print("2/5")

out = check_output(["./a.out", medium['width'], medium['height'], medium['kernel_order'], medium['nchannels'], medium['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[2] = int(lines[0].split(': ')[1].split()[0])
t_optimized[2] = int(lines[1].split(': ')[1].split()[0])

print("3/5")

out = check_output(["./a.out", large['width'], large['height'], large['kernel_order'], large['nchannels'], large['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[3] = int(lines[0].split(': ')[1].split()[0])
t_optimized[3] = int(lines[1].split(': ')[1].split()[0])

print("4/5")

out = check_output(["./a.out", largest['width'], largest['height'], largest['kernel_order'], largest['nchannels'], largest['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[4] = int(lines[0].split(': ')[1].split()[0])
t_optimized[4] = int(lines[1].split(': ')[1].split()[0])

print("5/5")

print("Done")
print("Showing graph...")

fig, ax = plt.subplots()
index = np.arange(5)
bw = 0.35

rect1 = plt.bar(index, t_original, bw, alpha=0.7, color='r', label='Original')
rect2 = plt.bar(index + bw, t_optimized, bw, alpha=0.7, color='y', label='Optimized')

plt.xlabel('Kernels')
plt.ylabel('Time (microseconds)')
plt.xticks(index, ('64', '128', '256', '512', '1024'))
plt.legend()
plt.tight_layout()
plt.show()
