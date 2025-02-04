list_students = []
list_scores = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_students.append([name, score])
        list_scores.append(score)
        
        
minimum = min(list_scores);

while minimum in list_scores:
    list_scores.remove(minimum)

# now the lowest has been removed, let's find min again.
minimum = min(list_scores)

stu_min = [student[0] for student in list_students if student[1] == minimum]

stu_min.sort()

for stu in stu_min:
    print(stu)
