#Q1
scores = [78, 85, 62, 90, 55, 88, 73]

print("Scores :",scores)

print("Highest score: ",max(scores))
print("Lowest score: ",min(scores))

AVG = round(sum(scores)/len(scores),2)
print("Average score: ", AVG)

greater_than_75_scores =[]
for score in scores:
    if score>75:
        greater_than_75_scores.append(score)

print("Score >75: ",greater_than_75_scores)

sortedDF= sorted(greater_than_75_scores,reverse=True)
print("Sorted as Desc: ",sortedDF)

sortedTuple = tuple(sortedDF)

print("First element: ",sortedTuple[0])
print("Last element: ",sortedTuple[-1])
print("Total number of elements: ",len(sortedTuple))

count=0
for score in scores:
    if score>AVG:
        count+=1

abv_avg_students=count
print("Number of Students who scored more than class avg: ", abv_avg_students)

print("-"*60) 
performance = {}
for score in scores:
    if score>=85:
        performance[score]="Excellent"
    elif score>=70 & score<=84:
        performance[score]="Good"
    elif score>=60 & score<=69:
        performance[score]="Average"
    else :
        performance[score]="Poor"

print("Score: ","Catergory: ")
for score, category in performance.items():
    print(f"{score} : {category}")

second_hscore = sortedTuple[1]
print("Second Highest Score: ", second_hscore)

abv_second_highscore = 0

for score in scores:
    if score>second_hscore:
        abv_second_highscore+=1

print("Students above second h score: ",abv_second_highscore)






