import sys

sys.stdin = open("_조교의성적매기기.txt")
T = int(input())
for C in range(1 ,T+1):
    matrix_ = []
    N, M = map(int, input().split())
    rank = []
    sep_ = N // 10
    for i in range(N):
        point = 0
        matrix_.append(input().split())
        point += float(matrix_[i][0])*0.35
        point += float(matrix_[i][1])*0.45
        point += float(matrix_[i][2])*0.20
        rank.append(point)
    answer = sorted(rank)[::-1]
    Two = sorted(rank)[::-1]
    count = 0
    for index in range(10):
        for idx in range(sep_):
            if index == 0:
                answer[count] = 'A+'
            elif index == 1:
                answer[count] = 'A0'
            elif index == 2:
                answer[count] = 'A-'
            elif index == 3:
                answer[count] = 'B+'
            elif index == 4:
                answer[count] = 'B0'
            elif index == 5:
                answer[count] = 'B-'
            elif index == 6:
                answer[count] = 'C+'
            elif index == 7:
                answer[count] = 'C0'
            elif index == 8:
                answer[count] = 'C-'
            elif index == 9:
                answer[count] = 'D0'
            count += 1
    for search in range(N):
        if rank[M-1] == Two[search]:
            print(f'#{C}', answer[search])  


T = int(input())
for C in range(1 ,T+1):
    matrix_ = []
    N, M = map(int, input().split())
    rank = []
    sep_ = N // 10
    for i in range(N):
        point = 0
        matrix_.append(input().split())
        point += float(matrix_[i][0])*0.35
        point += float(matrix_[i][1])*0.45
        point += float(matrix_[i][2])*0.20
        rank.append(point)
    answer = sorted(rank)[::-1]
    Two = sorted(rank)[::-1]
    count = 0
    Plus_ = 0
    my_dic = {0: 'A+', 1: 'A0', 2: 'A-', 3: 'B+', 4: 'B0', 5: 'B-', 6: 'C+', 7: 'C0', 8: 'C-', 9: 'D0'}
    for index in range(10):
        for idx in range(sep_):
            if index == Plus_:
                answer[count] = my_dic[index]
            count += 1
        Plus_ += 1
    for search in range(N):
        if rank[M-1] == Two[search]:
            print(f'#{C}', answer[search])  

#3회차 알고리즘 테스트 2번 4번 피드백을 생각하며 풀어보았습니다.