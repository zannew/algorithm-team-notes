student_a = dict()
student_a['성별'] = '남자'
student_a['점수'] = 90

student_b = dict()
student_b['성별'] = '여자'
student_b['점수'] = 83

print(student_a['성별'] == '남자' and student_a['점수'] >= 95)
print(student_a['성별'] == '남자' or student_a['점수'] >= 90)
print(not student_a['성별'] == '남자')

print(student_b['성별'] == '여자' and student_b['점수'] >= 90)
print(student_b['성별'] == '여자' or student_b['점수'] >= 80)
print(not student_b['성별'] == '여자')