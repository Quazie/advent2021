with open('input1.txt') as f:
    lines = f.readlines()


single_inc = 0
rolling_inc = 0
last = ""
last3 = []
for line in lines:
    cur = int(line)

    # compare single increment
    if last != "":
        if cur > last:
            single_inc = single_inc + 1
    if len(last3) == 3:
        old = sum(last3)
        last3.pop(0)
        last3.append(cur)
        new = sum(last3)
        if new > old:
            rolling_inc = rolling_inc + 1

    else:
        last3.append(cur)
    last = cur

print "Single increment is " + str(single_inc)
print "Rolling increment is " + str(rolling_inc)