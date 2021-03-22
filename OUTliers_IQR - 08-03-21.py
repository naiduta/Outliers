# import pickle
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pprint
import json

class Outliers:
    def __init__(self, dfA: pd.DataFrame) -> pd.DataFrame:
        self.dfA = dfA

    def device_outliers(self, dfA):
        dev = dfA['device'].unique()
        # out_lie = str(dev) + ".jason"
        # out_lie2 = str(dev) + ".txt"
        parameters = ['temperature', 'humidity', 'voc', 'pm10', 'pm25', 'pm100', 'pm10_env', 'pm25_env', 'pm100_env',
                      'particles_03',
                      'particles_05', 'particles_10', 'particles_25', 'particles_50', 'particles_100', 'co2']
        df_outl = pd.DataFrame()
        for sensor in parameters:
            Q1, Q3 = dfA[sensor].quantile([0.25, 0.75])
            IQR = Q3 - Q1
            low_lim = Q1 - 1.5 * IQR
            up_lim = Q3 + 1.5 * IQR
            df_min = dfA[dfA[sensor] < low_lim]
            df_max = dfA[dfA[sensor] > up_lim]
            df_outl = df_outl.append(df_max, ignore_index=True)
            df_outl = df_outl.append(df_min, ignore_index=True)
            #print(sensor)
        df_outl = df_outl.drop_duplicates(subset=['timestamp'])
        json_str = df_outl.set_index("timestamp").to_json(orient="index", date_format='iso')
        pprint.pprint(json.loads(json_str))
        # df_outl.to_json(out_lie)
        # print(df_outl, file=open(out_lie2, "wt"))
        return

    def plot(sensor_data: pd.DataFrame, val: str) -> plt.plot:
        #ax = df1.plot(x='timestamp', y=["co2", "temperature", "humidity", "voc"])
        #ax = df1.plot(x='timestamp', y=['pm10', 'pm25', 'pm100', 'pm10_env', 'pm25_env', 'pm100_env'])
        ax = df1.plot(x='timestamp', y=['particles_03',
                      'particles_05', 'particles_10', 'particles_25', 'particles_50', 'particles_100'])
        ax.set_xlim(pd.Timestamp('2021-01-21 10:48:07'), pd.Timestamp('2021-01-21 15:48:07'))
        ax.set_ylim(-100, 1000)
        plt.title(device)
        plt.show()
        return

if __name__ == "__main__":
    # Loading the pickled data
    df = pd.read_pickle('D:/EnvIOT/Sensor data processing/sample_data.pkl')
    custom_date_parser = lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    #df = pd.DataFrame(df)
    df = df.drop(columns=['fw_version', 'pid'])
    # Data from the pickle is not clean and can't be read directly into a data frame, thats why I have created csv file
    df.to_csv('D:/EnvIOT/Sensor data processing/sample_data_19col.csv')
    # timestamp in the data frame is object and I have tried several options to convert before I choose parse_dates
    df = pd.read_csv('D:/EnvIOT/Sensor data processing/sample_data_19col.csv', parse_dates=['timestamp'],
                     date_parser=custom_date_parser)
    pd.set_option('display.max_columns', None)
    out = Outliers(df)
    for device in df['device'].unique():
        df1 = df[df['device'] == device]
        out.device_outliers(df1)
        out.plot(df1)

