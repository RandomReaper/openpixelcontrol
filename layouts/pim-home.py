#!/usr/bin/env python
import math

# Led strip with
leds_per_meter = 30
spacing = 1.0/leds_per_meter  # m

a_size = 6.0
b_size = 3.0
c_size = 6.0

a = int(math.ceil(a_size * leds_per_meter))
b = int(math.ceil(b_size * leds_per_meter))
c = int(math.ceil(c_size * leds_per_meter))

lines = []

orig_x = 0
orig_y = 0
orig_z = 0
dir_x = 0
dir_y = -1
dir_z = 0
nr = a
for i in range(0, nr):
    lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                 (orig_x+i*dir_x*spacing, orig_y+i*dir_y*spacing, orig_z+i*dir_z*spacing))

orig_x = 0
orig_y = 0
orig_z = 0
dir_x = 1
dir_y = 0
dir_z = 0
nr = b
for i in range(0, nr):
    lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                 (orig_x+i*dir_x*spacing, orig_y+i*dir_y*spacing, orig_z+i*dir_z*spacing))

orig_x = orig_x+b*dir_x*spacing
orig_y = 0
orig_z = 0
dir_x = 0
dir_y = -1
dir_z = 0
nr = c
for i in range(0, nr):
    lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                 (orig_x+i*dir_x*spacing, orig_y+i*dir_y*spacing, orig_z+i*dir_z*spacing))

print '[\n' + ',\n'.join(lines) + '\n]'
