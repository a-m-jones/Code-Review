import numpy as np
import matplotlib.pyplot as plt
import glob

def read_data(file_type, month):
	files_in = glob.glob('./data/{}_*-{}-*.txt'.format(file_type, month))
	file_1 = np.genfromtxt(files_in[0])
	file_2 = np.genfromtxt(files_in[1])
	file_3 = np.genfromtxt(files_in[2])
	averages = (file_1 + file_2 + file_3) / 3.0
	return averages
	# an_array = np.array([ [files_1], [files_2], [files_3] ])
	# return np.nanmean(an_array, axis=0)

def plot(month):
	# plt.pcolormesh(read_data('xcoordinates', month), read_data('ycoordinates', month),
	# read_data('airtemp', month))
	plt.imshow(read_data('airtemp', month))
	plt.colorbar()
	plt.show()

plot('08')

# print np.genfromtxt('./data/xcoordinates_1981-01-17T00:00:00.000000000.txt')
# print ""
# print read_data('airtemp', '01')

# data1 = np.genfromtxt('./data/xcoordinates_1980-09-16T12:00:00.000000000.txt')
# data2 = np.genfromtxt('./data/xcoordinates_1981-09-16T12:00:00.000000000.txt')
# data3 = np.genfromtxt('./data/xcoordinates_1982-09-16T12:00:00.000000000.txt')

# print data1[12][0]
# print data2[12][0]
# print data3[12][0]

# for i in range(0,len(data)):
# 	print data[i][0]

# print read_data('xcoordinates', '01').shape

# x = np.array([[0,1], [2,3]])
# y = np.array([[3,5], [2,6]])

# print np.nanmean()






# air_temp = np.genfromtxt('./data/airtemp_1980-09-16T12:00:00.000000000.txt')
# x_coords = np.genfromtxt('./data/xcoordinates_1980-09-16T12:00:00.000000000.txt')
# y_coords = np.genfromtxt('./data/ycoordinates_1980-09-16T12:00:00.000000000.txt')

# average_air_temp = np.nanmean(air_temp, axis=1)
# average_x_coords = np.nanmean(x_coords, axis=1)
# average_y_coords = np.nanmean(y_coords, axis=1)

# # for i in range(0, len(average_y_coords)):
# # 	print average_x_coords[i], average_y_coords[i], average_air_temp[i]

# plt.pcolormesh(x_coords, y_coords, air_temp)
# plt.show()

# print x_coords[100][100]
# print y_coords[100][100]

# x = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
# y = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
# data = np.array([ [1,1,1], [2,2,2], [3,3,3] ])

# combined = np.array([x,y,data])
# print combined
# # plt.imshow(combined)
# # plt.show()

# data = np.array([[1,2],[3,4]])
# plt.imshow(data)
# plt.show()