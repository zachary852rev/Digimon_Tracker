def staircase(n):
    for i in range(1, n+1):
        print(("#"* i).rjust(n))



def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score = a_score + 1
        elif a[i] < b[i]:
            b_score = b_score + 1
        else:
            continue
    return (a_score, b_score)



def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38:
            continue
        else:
            x = grades[i]
            y = x % 5
            if y == 3:
                x = x + 2
                grades[i] = x
            elif y == 4:
                x = x + 1
                grades[i] = x
            else:
                continue
    return grades