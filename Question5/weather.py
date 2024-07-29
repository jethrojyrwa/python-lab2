def highest_lowestTemp(weather):
    max_temps = []
    min_temps = []
    for i in range(len(weather)):
        max_temps.append(weather[i]['MaxTemp'])

    for i in range(len(weather)):
        min_temps.append(weather[i]['MinTemp'])
        
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)

    return highest_temp, lowest_temp

def aboveTemp(weather):
    temps=[]
    count=0
    for i in range(len(weather)):
        temps.append(weather[i]['MaxTemp'])
    for i in range(len(temps)):
        if temps[i]>30:
            count+=1
    return count

def avgHumidity(weather):
    hu = []
    huSum = 0
    for i in range(len(weather)):
        hu.append(weather[i]['Humidity'])
    for i in range(len(hu)):
        huSum += hu[i]
        
    return huSum/len(hu)
weather = [
            {'date': '2024-07-10', 'MaxTemp': 29, 'MinTemp': 22, 'Humidity': 72},
            {'date': '2024-07-11', 'MaxTemp': 35, 'MinTemp': 23, 'Humidity': 58},
            {'date': '2024-07-12', 'MaxTemp': 35, 'MinTemp': 19, 'Humidity': 46},
            {'date': '2024-07-13', 'MaxTemp': 25, 'MinTemp': 15, 'Humidity': 51},
            {'date': '2024-07-14', 'MaxTemp': 28, 'MinTemp': 21, 'Humidity': 65},
            {'date': '2024-07-15', 'MaxTemp': 28, 'MinTemp': 20, 'Humidity': 46},
            {'date': '2024-07-16', 'MaxTemp': 31, 'MinTemp': 22, 'Humidity': 65},
            {'date': '2024-07-17', 'MaxTemp': 27, 'MinTemp': 18, 'Humidity': 60},
            {'date': '2024-07-18', 'MaxTemp': 34, 'MinTemp': 23, 'Humidity': 64},
            {'date': '2024-07-19', 'MaxTemp': 28, 'MinTemp': 25, 'Humidity': 67},
            {'date': '2024-07-20', 'MaxTemp': 30, 'MinTemp': 20, 'Humidity': 77},
            {'date': '2024-07-21', 'MaxTemp': 32, 'MinTemp': 21, 'Humidity': 47},
            {'date': '2024-07-22', 'MaxTemp': 32, 'MinTemp': 21, 'Humidity': 79},
            {'date': '2024-07-23', 'MaxTemp': 25, 'MinTemp': 23, 'Humidity': 68},
            {'date': '2024-07-24', 'MaxTemp': 28, 'MinTemp': 22, 'Humidity': 64},
            {'date': '2024-07-25', 'MaxTemp': 31, 'MinTemp': 24, 'Humidity': 62},
            {'date': '2024-07-26', 'MaxTemp': 25, 'MinTemp': 20, 'Humidity': 53},
            {'date': '2024-07-27', 'MaxTemp': 30, 'MinTemp': 20, 'Humidity': 69},
            {'date': '2024-07-28', 'MaxTemp': 28, 'MinTemp': 18, 'Humidity': 70},
            {'date': '2024-07-29', 'MaxTemp': 30, 'MinTemp': 19, 'Humidity': 43},
            {'date': '2024-07-30', 'MaxTemp': 25, 'MinTemp': 19, 'Humidity': 71},
            {'date': '2024-07-31', 'MaxTemp': 31, 'MinTemp': 19, 'Humidity': 63},
            {'date': '2024-08-01', 'MaxTemp': 28, 'MinTemp': 24, 'Humidity': 40}
            ]

print("Weather over the specified period:\n")
for i in range(len(weather)):
    d = weather[i]
    print("Date:",d['date'])
    print("MaxTemp:",d['MaxTemp'])
    print("MinTemp:",d['MinTemp'])
    print("Humidity:",d['Humidity'])
    print("-----------------")

print()
high,low = highest_lowestTemp(weather)
print("Higest Temperature during the week: ",high,"°C")
print("Lowest Temperature during the week: ",low,"°C")

above_30 = aboveTemp(weather)
print("Number of days with above 30°C: ",above_30)

humd = avgHumidity(weather)
print("Average Humidity over the specified period: ",humd) 
