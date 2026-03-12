
read_count=0
valid_nums=[]
invalid_count=0

with open('scores.txt','r') as file:
    for line in file:
        print(line)
        read_count+=1
        try:
            valid_nums.append(float(line.strip()))
        except ValueError:
            invalid_count += 1
    

    

    print("read count",read_count)
    print("valid nums",valid_nums)
    print("avg score",sum(valid_nums)/len(valid_nums))
        