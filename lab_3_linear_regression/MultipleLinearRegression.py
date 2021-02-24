import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#   init empty arrays for taking data from file
data = []
answers = []

#   open file with table of required for analysis data and process row-by-row
with open("apartmentComplexData.txt") as file_db:
    for line in file_db:
        #   separate all elements in row by comma
        row = line.split(",")

        #   append elements of the row into an inner array that will represent variables of polynomial
        current_row_usable_data = [float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6])]

        #   append those variables into the list of polynomial inputs, transforming string to float
        data.append(current_row_usable_data)

        #   append current row's answer to the polynomial, transforming string to float
        answers.append(float(row[8]))

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

#   graphical representation of the data for making visual analysis of the results
plt.scatter(range(0, 100), answers[:100], color="red")
plt.plot(range(0, 100), answers_predicted[:100], color="blue")
plt.title("first 100 original results and predictions (originals - red, predicted - blue")
plt.xlabel("record ID")
plt.ylabel("Answer value")
plt.grid(color="black")
plt.show()