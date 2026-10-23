'''filter'''
import json
data_str = input()
min_score = float(input())

students = json.loads(data_str)

passed_students = []

student_ids = sorted(students.keys())

for student_id in student_ids:
    score = students[student_id]
    if score >= min_score:
        passed_students.append((student_id, score))

if not passed_students:
    print("Nope")
else:
    for student_id, score in passed_students:
        print(f"{student_id}\t{score:.2f}")
