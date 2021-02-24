import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sklearn.preprocessing as preprop
import matplotlib.pyplot as plt

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

# scaler = preprop.StandardScaler()
# primary_data_from_file = scaler.fit_transform(primary_data_from_file)

# pt = preprop.PowerTransformer(method="box-cox", standardize=True)
# primary_data_from_file = pt.fit_transform(primary_data_from_file)

# quantile_transformer = preprop.QuantileTransformer(output_distribution="normal", random_state=0)
# primary_data_from_file = quantile_transformer.fit_transform(primary_data_from_file)

# primary_data_from_file = preprop.normalize(primary_data_from_file, norm="l2")
for i in range(len(primary_data_from_file)):
    current_record = [primary_data_from_file[i][0], primary_data_from_file[i][1], primary_data_from_file[i][2],
                      primary_data_from_file[i][3], primary_data_from_file[i][4]]

    data.append(current_record)
    answers.append(primary_data_from_file[i][5])

# data = preprop.normalize(data)
# scaler = preprop.StandardScaler()
# primary_data_from_file = scaler.fit_transform(primary_data_from_file)

data = preprop.normalize(data)

#   transform standard arrays into numpy arrays
data, answers = np.array(data), np.array(answers)

#   init polynomial features object
transformer = PolynomialFeatures(degree=5, include_bias=False)

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

#   graphical representation of the data for making visual analysis of the results
plt.scatter(range(0, 100), answers[:100], color="red")
plt.plot(range(0, 100), answers_predicted[:100], color="blue")
plt.title("first 100 original results and predictions (originals - red, predicted - blue")
plt.xlabel("record ID")
plt.ylabel("Answer value")
plt.grid(color="black")
plt.show()