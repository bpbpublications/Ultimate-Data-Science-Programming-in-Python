import numpy as mynp

# print(help(mynp.sort))
myarr1 = mynp.array([45,34,68,34,67,26,9,98,35])
print(f"Original array is: {myarr1}")
print(f"sorted 1-D array in ascending order is {mynp.sort(myarr1)}") # default sorting is ascending
print(f"sorted 1-D array in descending order is {-mynp.sort(-myarr1)}") # default sorting is ascending
print('-'*50)
myarr2 = mynp.array(['mat','hat','rat','bat','cat'])
print(f"String sorted 1-D array in ascending order is {mynp.sort(myarr2)}") # default sorting is ascending
print(f"String sorted 1-D array in descending order is {mynp.sort(myarr2)[::-1]}")
print('-'*50)
myarr3 = mynp.array([[78,35,98],[21,11,9],[87,35,65]])
print(f"Sorted 2-D array in ascending order is {mynp.sort(myarr3)}")
print(f"Sorted 2-D array in descending order is {-mynp.sort(-myarr3)}")
print('-'*50)
print("Sorting based on same marks of Students and correct questions attempted in ascendong order")
mydata = [('name', 'S10'), ('marks', float), ('correct_questions', int)]
myvalues = [('Saurabh', 89.5, 52), ('Pallavi', 67, 38),('Priyanka', 89.5, 53),('Yathartha', 88, 51)]
mydatatype = mynp.array(myvalues, dtype=mydata)
mysort_marks_correct = mynp.sort(mydatatype, order=['marks', 'correct_questions'])
print(f"Original Array is :\n {mydata}")
print(f"Sorting carried out based on correct_questions :\n {mysort_marks_correct}")