list = ['banana', '1', '2', 'class', 'string', 'bool', '313', '12', '404', 'git']

def IsItNumberAndAverage(a):
    total = 0
    count = 0
    for i in a:
        if i.isdigit():
            total += int(i)
            count += 1
    avg = total/count
    print(f"Average is {avg} and total is {total}")

IsItNumberAndAverage(list)
