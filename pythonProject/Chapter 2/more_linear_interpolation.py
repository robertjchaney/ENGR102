import math

# By submitting this assignment, I agree to the following
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment"

# Name: Robert Chaney
# Section: 538
# Assignment: Lab 2, Activity 2
# Date: 2 September 2024

tStart = 12.0
t1 = 30.0
tEnd = 85.0

xStart = 8
x1 = None
xEnd = -5

yStart = 6
y1 = None
yEnd = 30

zStart = 7
z1 = None
zEnd = 9

# X interpolation
x1 = xStart + ((xEnd - xStart) / (tEnd - tStart)) * (t1 - tStart)
# Y interpolation
y1 = yStart + ((yEnd - yStart) / (tEnd - tStart)) * (t1 - tStart)
# Z interpolation
z1 = zStart + ((zEnd - zStart) / (tEnd - tStart)) * (t1 - tStart)

print(f'At time {t1} seconds:')
print(f'x1 = {x1} m')
print(f'y1 = {y1} m')
print(f'z1 = {z1} m')
print('-----------------------')

# PART 2 STARTS HERE

t2 = 37.5
t3 = 45.0
t4 = 52.5
t5 = 60.0

# t2 interpolation
x2 = xStart + ((xEnd - xStart) / (tEnd - tStart)) * (t2 - tStart)
y2 = yStart + ((yEnd - yStart) / (tEnd - tStart)) * (t2 - tStart)
z2 = zStart + ((zEnd - zStart) / (tEnd - tStart)) * (t2 - tStart)

print(f'At time {t2} seconds:')
print(f'x2 = {x2} m')
print(f'y2 = {y2} m')
print(f'z2 = {z2} m')
print('-----------------------')

# t3 interpolation
x3 = xStart + ((xEnd - xStart) / (tEnd - tStart)) * (t3 - tStart)
y3 = yStart + ((yEnd - yStart) / (tEnd - tStart)) * (t3 - tStart)
z3 = zStart + ((zEnd - zStart) / (tEnd - tStart)) * (t3 - tStart)

print(f'At time {t3} seconds:')
print(f'x3 = {x3} m')
print(f'y3 = {y3} m')
print(f'z3 = {z3} m')
print('-----------------------')

# t4 interpoaltion
x4 = xStart + ((xEnd - xStart) / (tEnd - tStart)) * (t4 - tStart)
y4 = yStart + ((yEnd - yStart) / (tEnd - tStart)) * (t4 - tStart)
z4 = zStart + ((zEnd - zStart) / (tEnd - tStart)) * (t4 - tStart)

print(f'At time {t4} seconds:')
print(f'x4 = {x4} m')
print(f'y4 = {y4} m')
print(f'z4 = {z4} m')
print('-----------------------')

# t5 interpolation
x5 = xStart + ((xEnd - xStart) / (tEnd - tStart)) * (t5 - tStart)
y5 = yStart + ((yEnd - yStart) / (tEnd - tStart)) * (t5 - tStart)
z5 = zStart + ((zEnd - zStart) / (tEnd - tStart)) * (t5 - tStart)

print(f'At time {t5} seconds:')
print(f'x5 = {x5} m')
print(f'y5 = {y5} m')
print(f'z5 = {z5} m')