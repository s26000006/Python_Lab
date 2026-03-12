import math
clean_data=[]
invalid_data=0
Total_records=0

with open("data.txt","r") as file:
    for line in file:
        Total_records+=1
        try:
            clean_data.append(float(line.strip()))
        except ValueError:
            invalid_data+=1
            

        

print("clean data from file: ",clean_data)
print("invalid count ",invalid_data)

print("-"*60)
print("statistics")
print("-"*60)

mean = sum(clean_data)/len(clean_data)
print("mean of data: ",round(mean,2))

n=len(clean_data)

var =sum((x - mean)**2 for x in clean_data) / n

sigma =math.sqrt(var)
print("sigma ",round(sigma,2))

#z = (x - mu) / sigma

outliers = []
for x in clean_data:
    z = (x - mean) / sigma
    if abs(z) > 2:
        outliers.append(x)

print("Outliers: ",outliers)


with open("data_report.txt","w") as file:
    print("Data Quality Report\n")
    print("Total Records",Total_records)
    print("Invalid Records",invalid_data)
    print("mean of data: ",round(mean,2))
    print("sigma ",round(sigma,2))
    print("Outliers: ",outliers)
    





