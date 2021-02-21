import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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

#   init polynomial features object
transformer = PolynomialFeatures(degree=5, include_bias=True)

#   fit input for polynomial analysis
transformer.fit(data)

#   polynomial variables values generation out of input
polynomial_data = transformer.transform(data)

#   fit data with answers to the LinearRegression module for analysis
model = LinearRegression().fit(polynomial_data, answers)

#   try to analyze data and get scores
r_sq = model.score(polynomial_data, answers)

#   show variables that are inner part of linear regression module
print("\n\n\n\n\t\tcoefficient of determination: " + str(r_sq))
print("\t\tintercept: " + str(model.intercept_))
print("\t\tslope: " + str(model.coef_))

#   generate possible answers using the same data as was provided to compare solutions
answers_predicted = model.predict(polynomial_data)

#   for showing how system works, print first 5 elements of original table
for i in range(5):
    print("before analysis :" + str(data[i]) + " have answer " + str(answers[i]))

#   show another answers to the first five inputs from the original table basing on finished regression
for i in range(5):
    print("for data " + str(data[i]) + " the answer is " + str(answers_predicted[i]))