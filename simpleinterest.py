import sys

if len(sys.argv) == 4:
    script_name = sys.argv[0]
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
else:
    script_name = sys.argv[0]
    p, t, r = 10000, 2, 10
    print("No input given - using default values:")

# Calculate simple interest
si = (p * t * r) / 100

print("Script Name:", script_name)
print("Priniciple amount",p)
print("Rate",r)
print("Time",t)
print("Simple Interest:", si)