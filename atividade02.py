import numpy as np
#1-csv
#2-,

#3 - Questão
iris_data1 = np.genfromtxt('iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('iris_data_2.csv', delimiter=',')

#-4 - Questão
print(iris_data1.shape)
print(iris_data2.shape)


#5- Questão
iris_data = np.vstack((iris_data1,iris_data2))

# 6- Questão
print(iris_data.shape)

#7 - Questão
new_data = iris_data[~np.isnan(iris_data).any(axis=1)]

#8 - Questão
print(iris_data.shape)
print(new_data.shape)
print(iris_data)
print(new_data)

# 9- Questão
nodes, counts = np.unique(new_data[:,-1], return_counts=True)
print(nodes)
print(counts)

#10 - Questão

new_data[:,0][new_data[:,-1] == 2] = 3
new_data[:,0][new_data[:,-1] == 1] = 2
new_data[:,0][new_data[:,-1] == 0] = 1
data = new_data
print(data)

# 11 -questão
caracteristicas = data[:,-2]
classes = data[:,-1]
print(caracteristicas)
print(classes)
print(caracteristicas.shape)
print(classes.shape)

np.savetxt('data.csv', data, delimiter=',')