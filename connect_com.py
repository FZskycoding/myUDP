import serial
import time

ser = serial.Serial("COM3", 2000000,timeout=2)
count = 0
count_ps = 0
s = 0
x_max = 0
y_max = 0
z_max = 0
with open("dataFile.txt", "w+") as f:
    t_end = time.time() + 10  # run 10 seconds
    per_s = time.time() + 1
    while time.time() < t_end:
        lines = ser.readline().decode()
        lines = lines.split("#")
        for line in lines:
            line = line.split(",")
            if len(line) == 3:
                x,y,z = line
                if len(x) > 0 and len(y) > 0 and len(z) > 0:
                    x = float(x) / 1000
                    y = float(y) / 1000
                    z = float(z) / 1000
                    # if abs(z) > z_max:
                    #     z_max = z
                    print(f"{x},{y},{z}",file=f)
                    count += 1
                    count_ps += 1
        if time.time() > per_s:
            per_s = time.time() + 1
            print(count_ps)
            count_ps = 0
        # f.write(line)
print("saved lines: %s" % count)
# t_end = time.time() + 10  # run 10 seconds
# while time.time() < t_end:
#     line = ser.readline()
#     # print(line)
#     count += 1
# print("saved lines: %s" % count)