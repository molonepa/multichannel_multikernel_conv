from subprocess import call, check_output
import matplotlib.pyplot as plt
import numpy as np

smallest = {
            'width':        '16',
            'height':       '16',
            'kernel_order': '1',
            'nchannels':    '32',
            'nkernels':     '32'
        }

small = {
            'width':        '64',
            'height':       '64',
            'kernel_order': '3',
            'nchannels':    '256',
            'nkernels':     '256'
        }

medium = {
            'width':        '128',
            'height':       '128',
            'kernel_order': '5',
            'nchannels':    '256',
            'nkernels':     '256'
        }

large = {
            'width':        '256',
            'height':       '256',
            'kernel_order': '5',
            'nchannels':    '256',
            'nkernels':     '256'
        }

largest = {
            'width':        '512',
            'height':       '512',
            'kernel_order': '5',
            'nchannels':    '256',
            'nkernels':     '256'
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

out = check_output(["./a.out", small['width'], small['height'], small['kernel_order'], small['nchannels'], small['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[1] = int(lines[0].split(': ')[1].split()[0])
t_optimized[1] = int(lines[1].split(': ')[1].split()[0])

out = check_output(["./a.out", medium['width'], medium['height'], medium['kernel_order'], medium['nchannels'], medium['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[2] = int(lines[0].split(': ')[1].split()[0])
t_optimized[2] = int(lines[1].split(': ')[1].split()[0])

out = check_output(["./a.out", large['width'], large['height'], large['kernel_order'], large['nchannels'], large['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[3] = int(lines[0].split(': ')[1].split()[0])
t_optimized[3] = int(lines[1].split(': ')[1].split()[0])

out = check_output(["./a.out", largest['width'], largest['height'], largest['kernel_order'], largest['nchannels'], largest['nkernels']]).decode()
lines = out.split('\n')[0:2]
t_original[4] = int(lines[0].split(': ')[1].split()[0])
t_optimized[4] = int(lines[1].split(': ')[1].split()[0])

print("Done")
print("Showing graph...")

fig, ax = plt.subplots()
index = np.arange(5)
bw = 0.35

rect1 = plt.bar(index, t_original, bw, alpha=0.7, color='r', label='Original')
rect2 = plt.bar(index + bw, t_optimized, bw, alpha=0.7, color='y', label='Optimized')

plt.xlabel('Input size')
plt.ylabel('Time (ns)')
plt.xticks(index, ('Smallest', 'Small', 'Medium', 'Large', 'Largest'))
plt.legend()
plt.tight_layout()
plt.show()
