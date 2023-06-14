import random
data = []
coef = []
temp_point = []
with open("in.txt") as f:
    count_task = int(f.readline())
    category_task = list(map(int,f.readline().split()))
    time = list(map(float,f.readline().split()))
    count_dev = int(f.readline())
    for i in range(0,int(count_dev)):
        coef.append(list(map(float,f.readline().split())))

rand_list = []
temp_lst = []
best_list =[]
time_residents = [0] * (count_task-1)
temp = 0
score = 0
best_score = 0
best_time = 999999999
for y in range (0,random.randint(5,100)):
    for i in range(0,count_task):
        tmp_r = random.randint(0,count_dev-1)
        rand_list.append(tmp_r)
        temp = time[i]*coef[tmp_r][category_task[i]-1]
        score += (10**6)/(temp)
        time_residents[tmp_r] += temp
        temp = 0
    temp_time = max(time_residents)
    if temp_time<best_time:
        if best_score < score: 
            best_score = score
            best_list = rand_list
            best_time = temp_time
            temp_res1 = time_residents
    score = 0
    time_residents = [0] * (count_task-1)
    temp_lst.append(rand_list)
    rand_list = []

print([x+1 for x in best_list])






         