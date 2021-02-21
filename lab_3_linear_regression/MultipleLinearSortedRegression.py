import numpy as np
from sklearn.linear_model import LinearRegression

#   init empty arrays for taking data from file
data = []
answers = []
primary_data_from_file = []

with open("apartmentComplexData.txt") as file_db:
    for line in file_db:
        row = line.split(",")

        current_row_usable_data = [float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]),
                                   float(row[8])]

        primary_data_from_file.append(current_row_usable_data)

primary_data_from_file.sort(key=lambda x: x[0])

for i in range(len(primary_data_from_file)):
    current_record = [primary_data_from_file[i][0], primary_data_from_file[i][1], primary_data_from_file[i][2],
                      primary_data_from_file[i][3], primary_data_from_file[i][4]]

    data.append(current_record)
    answers.append(primary_data_from_file[i][5])

#   transform standard arrays into numpy arrays
data, answers = np.array(data), np.array(answers)

#   for showing how system works, print first 5 elements of original table
for i in range(5):
    print("before analysis :" + str(data[i]) + " have answer " + str(answers[i]))

#   fit data with answers to the LinearRegression module for analysis
model = LinearRegression().fit(data, answers)

#   try to analyze data and get scores
r_sq = model.score(data, answers)

#   show variables that are inner part of linear regression module
print("\n\n\n\n\t\tcoefficient of determination: " + str(r_sq))
print("\t\tintercept: " + str(model.intercept_))
print("\t\tslope: " + str(model.coef_))

#   generate possible answers using the same data as was provided to compare solutions
answers_predicted = model.predict(data)

#   show another answers to the first five inputs from the original table basing on finished regression
for i in range(5):
    print("for data " + str(data[i]) + " the answer is " + str(answers_predicted[i]))
