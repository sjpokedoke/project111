import csv
import pandas as pd
import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

#population mean and stdev
print("Population mean is: " + str(mean))
print("Standard deviation of the population is: " + str(stdev))

def randomsetofmean(count):
    dataset = []
    for i in range(0, count):
        randomindex = random.randint(0, len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0, 100):
    setofmeans = randomsetofmean(30)
    meanlist.append(setofmeans)

samplemean = statistics.mean(meanlist)
samplestdev = statistics.stdev(meanlist)

#sample mean and stdev
print("Sample mean is: " + str(samplemean))
print("Standard deviation of the sample is: " + str(samplestdev))

firststdevstart, firststdevend = samplemean-samplestdev, samplemean+samplestdev
twostdevstart, twostdevend = samplemean-(2*samplestdev), samplemean+(2*samplestdev)
threestdevstart, threestdevend = samplemean-(3*samplestdev), samplemean+(3*samplestdev)

#1, 2, 3 stdev
print("STDEV 1", firststdevstart, firststdevend)
print("STDEV 2", twostdevstart, twostdevend)
print("STDEV 3", threestdevstart, threestdevend)

fig = ff.create_distplot([meanlist], ["Reading time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="mean"))

fig.add_trace(go.Scatter(x=[firststdevstart, firststdevstart], y=[0, 0.17], mode="lines", name="First STDEV start"))
fig.add_trace(go.Scatter(x=[firststdevend, firststdevend], y=[0, 0.17], mode="lines", name="First STDEV end"))

fig.add_trace(go.Scatter(x=[twostdevstart, twostdevstart], y=[0, 0.17], mode="lines", name="Two STDEV start"))
fig.add_trace(go.Scatter(x=[twostdevend, twostdevend], y=[0, 0.17], mode="lines", name="Two STDEV end"))

fig.add_trace(go.Scatter(x=[threestdevstart, threestdevstart], y=[0, 0.17], mode="lines", name="Three STDEV start"))
fig.add_trace(go.Scatter(x=[threestdevend, threestdevend], y=[0, 0.17], mode="lines", name="Three STDEV end"))

#show graph
fig.show()

zscore = (samplemean-mean)/samplestdev

#print z score
print("Z Score is: " + str(zscore))