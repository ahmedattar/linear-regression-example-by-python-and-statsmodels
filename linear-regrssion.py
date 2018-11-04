import numpy as np
import csv
import statsmodels.api as sm
# in the next 2 lines ,we initialize matrices for all records to add values in them
precent=[]
median=[]


file_path='boston.csv'
def find_coefficients():
    numerator = 0
    denominator = 0
    with open(file_path, newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        headers= next(file_reader)
        # in the next 2 lines , we put data in the initialized matrices above
        for column in file_reader:
            precent.append(float(column[12]))
            median.append(float(column[13]))
    median_avg=np.mean(median)
    precent_avg=np.mean(precent)
    for (a,b) in zip(precent,median):
	    numerator+=(a-precent_avg)*(b-median_avg)
	    denominator+=np.power((a-precent_avg),2)
    theta1= numerator/denominator
    theta0=precent_avg-theta1*median_avg
    print("theta0 : coefficient 0 for fitting the model=",theta0)
    print("theta1 : coefficient 1 for fitting the model=",theta1)
def statmodel_fit():
    modified_input = sm.add_constant(precent)
    model = sm.OLS(median,modified_input)
    results = model.fit()
    print("theta0 using statsmodels library : coefficient 0 for fitting the model=",results.params[0])
    print("theta1 using statsmodels library : coefficient 1 for fitting the model=",results.params[1])

if __name__ == '__main__':
    # calling the made function: responsible for finding the coefficients
    find_coefficients()
    # calling the statmodel function: responsible for finding the coefficients using statmodel library
    statmodel_fit()


	
	

