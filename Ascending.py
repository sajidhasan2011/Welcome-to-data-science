import numpy as np

data_type = [
    ('name','S15'),
    ('class',int),
    ('height',float)

]

students_details = [
    ('Safwan',5,48.5),
    ('Afnan',6,52.5),
    ('Sajid',5,42.1),
    ('Nahian',5,40.11)
]
students = np.array(students_details,dtype=data_type)

print("Orginal array:")
print(students)

print()

print("Sort by height")
print(np.sort(students,order='height'))