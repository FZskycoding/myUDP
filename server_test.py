import serial
import time

ser = serial.Serial("COM3", 1000000,timeout=2)
count = 0
count_ps = 0
s = 0
x_max = 0
y_max = 0
z_max = 0
with open("dataFile.txt", "w+") as f:
    t_end = time.time() + 10  # run 10 seconds
    per_s = time.time() + 1
    pre_data = ""
    
    while time.time() < t_end:
        data = ser.read(ser.in_waiting).decode()
        data_list = []
        
        if len(data) > 0:
            # print(data)
            # lines = ser.readline().decode()
            first_tag = data.find("#")
            last_tag = data.rfind("#")
            if first_tag == -1:
                pre_data = data
            else:
                if first_tag == 0:
                    data_list.append(pre_data)
                else:
                    data_list.append(pre_data + data[:first_tag])
                if last_tag == len(data)-1:
                    pre_data = ""
                else:
                    pre_data = data[last_tag+1:]
                
                if first_tag != last_tag:
                    data_list += data[first_tag+1:last_tag].split("#")
            
            # lines = lines.split("#")
            for data in data_list:
                data = data.split(",")
                if len(data) == 3:
                    x,y,z = data
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
            # print(len(data_list))
            count_ps = 0
            # data_list = []
        # f.write(line)
print("saved lines: %s" % count)
# t_end = time.time() + 10  # run 10 seconds
# while time.time() < t_end:
#     line = ser.readline()
#     # print(line)
#     count += 1
# print("saved lines: %s" % count)