import pandas as pd 
import matplotlib.pyplot as plt
Iris = pd.read_csv("Iris.csv")
SepalLengthCm = Iris["SepalLengthCm"] 
SepalWidthCm = Iris["SepalWidthCm"]
PetalLengthCm = Iris["PetalLengthCm"]
PetalWidthCm=Iris["PetalWidthCm"]
#calculating the statistical information of the data
print("--SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm --")
print("mean: [", SepalLengthCm.mean(),"," ,SepalWidthCm.mean(),",",PetalLengthCm.mean() ,",",PetalWidthCm.mean(),"]")
print("median: [", SepalLengthCm.median(),",",SepalWidthCm.median(),",",PetalLengthCm.median(),",",PetalWidthCm.median(),"]")
print("mode: [", float(SepalLengthCm.mode()),",",float(SepalWidthCm.mode()),",",float(PetalLengthCm.mode()),",",float(PetalWidthCm.mode()),"]")
print("variance: [", SepalLengthCm.var(ddof=0),",",SepalWidthCm.var(ddof=0),",",PetalLengthCm.var(ddof=0),",",PetalWidthCm.var(ddof=0),"]") 
print("standard deviation: [", SepalLengthCm.std(ddof=0),",",SepalWidthCm.std(ddof=0),",",PetalLengthCm.std(ddof=0),",",PetalWidthCm.std(ddof=0),"]")
#verilerin range hesaplaması
min_val_SepalLengthCm = min(SepalLengthCm)
max_val_SepalLengthCm = max (SepalLengthCm)
range_data_SepalLengthCm =  max_val_SepalLengthCm- min_val_SepalLengthCm
min_val_SepalWidthCm = min(SepalWidthCm)
max_val_SepalWidthCm = max (SepalWidthCm)
range_data_SepalWidthCm = max_val_SepalWidthCm - min_val_SepalWidthCm
min_val_PetalLengthCm = min(PetalLengthCm)
max_val_PetalLengthCm = max (PetalLengthCm)
range_data_PetalLengthCm = max_val_PetalLengthCm - min_val_PetalLengthCm
min_val_PetalWidthCm = min(PetalWidthCm)
max_val_PetalWidthCm = max (PetalWidthCm)
range_data_PetalWidthCm = max_val_PetalWidthCm - min_val_PetalWidthCm
print("Range: [" , range_data_SepalLengthCm ,",",range_data_SepalWidthCm,",",range_data_PetalLengthCm,",",range_data_PetalWidthCm,"]")

# Plotting
x1=[0,1,2,3]
y1=[SepalLengthCm.mean(),SepalWidthCm.mean(),PetalLengthCm.mean() ,PetalWidthCm.mean()]
y2=[SepalLengthCm.median(),SepalWidthCm.median(),PetalLengthCm.median() ,PetalWidthCm.median()]
y3=[SepalLengthCm.mode(),SepalWidthCm.mode(),PetalLengthCm.mode() ,PetalWidthCm.mode()]
y4=[SepalLengthCm.var(ddof=0),SepalWidthCm.var(ddof=0),PetalLengthCm.var(ddof=0) ,PetalWidthCm.var(ddof=0)]
y5=[SepalLengthCm.std(ddof=0),SepalWidthCm.std(ddof=0),PetalLengthCm.std(ddof=0) ,PetalWidthCm.std(ddof=0)]
y6=[range_data_SepalLengthCm,range_data_SepalWidthCm,range_data_PetalLengthCm ,range_data_PetalWidthCm]

#mean plot
plt.plot(x1,y1,c="red")
plt.scatter(x1,y1,c="red")
plt.title("Mean Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()
#median plot
plt.plot(x1,y2,c="orange")
plt.scatter(x1,y2,c="orange")
plt.title("Median Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()
#mode plot
plt.plot(x1,y3,c="yellow")
plt.scatter(x1,y3,c="yellow")
plt.title("Mode Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()
#variance plot
plt.plot(x1,y4,c="green")
plt.scatter(x1,y4,c="green")
plt.title("Variance Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()
#standart deviation plot
plt.plot(x1,y5,c="blue")
plt.scatter(x1,y5,c="blue")
plt.title("Standard Deviation Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()
#range plot
plt.plot(x1,y6,c="indigo")
plt.scatter(x1,y6,c="indigo")
plt.title("Range Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()

#Point representation of all values
plt.scatter(x1,y1,c="red",label="Mean")
plt.scatter(x1,y2,c="orange",label="Median")
plt.scatter(x1,y3,c="yellow",label="Mode")
plt.scatter(x1,y4,c="green",label="Variance")
plt.scatter(x1,y5,c="blue",label="Standart Dev.")
plt.scatter(x1,y6,c="indigo",label="Range")
plt.title("İstatistik Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.legend()
plt.show()

#Point and linear view of all values
plt.plot(x1,y1,c="red")
plt.plot(x1,y2,c="orange")
plt.plot(x1,y3,c="yellow")
plt.plot(x1,y4,c="green")
plt.plot(x1,y5,c="blue")
plt.plot(x1,y6,c="indigo")
plt.scatter(x1,y1,c="red",label="Mean")
plt.scatter(x1,y2,c="orange",label="Median")
plt.scatter(x1,y3,c="yellow",label="Mode")
plt.scatter(x1,y4,c="green",label="Variance")
plt.scatter(x1,y5,c="blue",label="Standart Dev.")
plt.scatter(x1,y6,c="indigo",label="Range")
plt.title("İstatistik Değerleri")
plt.xticks([0,1,2,3],["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.legend(loc='best') 
plt.show()
