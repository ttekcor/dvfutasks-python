students_dict = {}
f = open("/home/rockett/Desktop/input.txt" ) 
a, *data = f
for st1 in data:
    st1.split('\t')
    group_id,student_name = st1.split('\t')
    group_data = students_dict.get(group_id)
    if group_data:
        group_data.append(student_name)
    else:
        group_data = [student_name]
    students_dict[group_id]=group_data 
with open ('/home/rockett/Desktop/output.txt' , 'w') as fout:
    sorted_dict=sorted(students_dict.items(), key=lambda x: x[0])
    sorted_dict=dict(sorted_dict)
    for group_id, students_data in sorted_dict.items():
        print(group_id, file=fout)
        group_id = sorted(group_id)
        for student in students_data:
            student=[i.rstrip()for i in students_data]
            student.sort()
            student = "\n".join(student)
        print(student,file=fout)