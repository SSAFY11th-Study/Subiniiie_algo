switches_num = int(input())
switches = list(map(int, input().split()))
students_num = int(input())
# 성별, 학생이 받은 수
students = [list(map(int, input().split())) for _ in range(students_num)]

switches.insert(0, 0)

for i in range(students_num) :
    if students[i][0] == 1 :
        k = students[i][1]
        s = students[i][1]
        while k <= switches_num :
            if switches[k] == 0 :
                switches[k] = 1
            else :
                switches[k] = 0
            k += s
    else :
        if switches[students[i][1]] == 0 :
            switches[students[i][1]] = 1
        else :
            switches[students[i][1]] = 0
        for l in range(1, students[i][1]) :
            if switches[students[i][1]-l] == switches[students[i][1]+l] :
                if switches[students[i][1]-l] == 0 :
                    switches[students[i][1] - l] = 1
                    switches[students[i][1] + l] = 1
                else :
                    switches[students[i][1] - l] = 0
                    switches[students[i][1] + l] = 0
            else :
                break

        print(*switches[1:])

