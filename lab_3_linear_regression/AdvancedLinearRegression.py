import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#   init empty arrays for taking data from file
data = []
answers = []
primary_data_from_file = []

with open("apartmentComplexData.txt") as file_db:
    for line in file_db:
        row = line.split(",")

        current_row_usable_data = [float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]),
                                   int(float(row[8]))]

        primary_data_from_file.append(current_row_usable_data)

for i in range(len(primary_data_from_file)):
    current_record = [primary_data_from_file[i][0], primary_data_from_file[i][1], primary_data_from_file[i][2],
                      primary_data_from_file[i][3], primary_data_from_file[i][4]]

    data.append(current_record)
    answers.append(primary_data_from_file[i][5])

#   transform standard arrays into numpy arrays
data, answers = np.array(data), np.array(answers)

#   add column of ones for calculating b0
data = sm.add_constant(data)

#   setting regression basing on ordinary least squares
model = sm.OLS(answers, data)

#   after setting model fit all answers for processing (they're already should be placed in)
results = model.fit()

print(results.summary())

#   show variables that are inner part of linear regression module
print("\n\n\n\n\t\tcoefficient of determination: " + str(results.rsquared))
print("\t\tregression coefficients: " + str(results.params))

#   generate possible answers using the same data as was provided to compare solutions
answers_predicted = results.predict(data)

#   for showing how system works, print first 5 elements of original table
for i in range(5):
    print("before analysis :" + str(data[i]) + " have answer " + str(answers[i]))

#   show another answers to the first five inputs from the original table basing on finished regression
for i in range(5):
    print("for data " + str(data[i]) + " the answer is " + str(answers_predicted[i]))

representable_plot_size = len(data)

#   graphical representation of the data for making visual analysis of the results
plt.scatter(range(0, representable_plot_size), answers[:representable_plot_size], color="red")
plt.plot(range(0, representable_plot_size), answers_predicted[:representable_plot_size], color="blue")
plt.title("first 100 original results and predictions (originals - red, predicted - blue")
plt.xlabel("record ID")
plt.ylabel("Answer value")
plt.grid(color="black")
plt.show()