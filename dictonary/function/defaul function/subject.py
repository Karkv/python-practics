subject_marks=[("English ",88),("Hindi",90),("Science",98),("Maths",87),("Social science",87)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x:x[1])
print("\nSorting the list of Tuples")
print(subject_marks)