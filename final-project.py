# Name: Prof Martinez
# Date: 2024-10-20
# Purpose: Final Project - CEIS110 - Prof Martinez

from noaa_sdk import noaa
import matplotlib.pyplot as plt

name = "Prof Martinez"
startDate = "2024-10-09"  # These dates will give me Hurricane Helene data
endDate = "2024-10-19"
zipCode = "32820"

print('Final Project - CEIS110 -', name)
print('Weather data for', zipCode, 'from', startDate, 'to', endDate)


temps = []
humidities = []
windSpeeds = []


def get_observation_value(observation, key, ndigits=None):
    return round(observation[key]['value'], ndigits) if observation[key]['value'] else '???'


def append_observation_value(observation, key, list):
    if (observation[key]['value']):
        list.append(observation[key]['value'])


n = noaa.NOAA()
observations = n.get_observations(zipCode, 'US', start=startDate, end=endDate)
print('Timestamp\t\t\t Temp\t Humidity\t Wind\t Description')
for observation in observations:
    append_observation_value(observation, 'temperature', temps)
    append_observation_value(observation, 'relativeHumidity', humidities)
    append_observation_value(observation, 'windSpeed', windSpeeds)
    print(observation['timestamp'], '\t',
          get_observation_value(observation, 'temperature'), '\t',
          get_observation_value(observation, 'relativeHumidity', 1), '\t\t',
          get_observation_value(observation, 'windSpeed'), '\t',
          observation['textDescription'])

farenheight_temps = list(map(lambda temp: temp * 1.8 + 32, temps))

# line chart
plt.figure()
plt.plot(farenheight_temps, label='Temperature F°')
plt.plot(humidities, label='Humidity %')
plt.plot(windSpeeds, label='Wind Speed Km/h')
plt.legend()
plt.suptitle('Temperature vs Humidity vs Wind Speed')
plt.savefig('temp-humidity-windSpeed-line.png')

# box plot
plt.figure()
box_plot_data = [farenheight_temps, humidities, windSpeeds]
plt.boxplot(box_plot_data)
plt.boxplot(box_plot_data, tick_labels=[
            'Temperature F°', 'Humidity %', 'Wind Speed Km/h'])
plt.suptitle('Temperature vs Humidity vs Wind Speed')
plt.savefig('temp-humidity-windSpeed-boxplot.png')

# Statistics
avg_temp = round(sum(farenheight_temps) / len(farenheight_temps), 1)
low_temp = round(min(farenheight_temps))
high_temp = round(max(farenheight_temps))

avg_humidity = round(sum(humidities) / len(humidities), 1)
low_humidity = round(min(humidities), 1)
high_humidity = round(max(humidities), 1)

avg_wind_speed = round(sum(windSpeeds) / len(windSpeeds), 1)
low_wind_speed = min(windSpeeds)
high_wind_speed = max(windSpeeds)

print('Weather statistics for', zipCode, 'from', startDate, 'to', endDate)

print('Avg Temperature: ', avg_temp, '°F')
print('Low Temperature: ', low_temp, '°F')
print('High Temperature: ', high_temp, '°F')

print('Avg Humidity: ', avg_humidity, '%')
print('Low Humidity: ', low_humidity, '%')
print('High Humidity: ', high_humidity, '%')

print('Avg Wind Speed: ', avg_wind_speed, 'Km/h')
print('Low Wind Speed: ', low_wind_speed, 'Km/h')
print('High Wind Speed: ', high_wind_speed, 'Km/h')
