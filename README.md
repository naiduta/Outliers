# Outlier
# This is the code to pick out the outliers from a big sensor data. Sensor data is needed to run this code. Sensor data belongs to the company I worked for and not sharing that info.
Extracting outliers from a dataset of sensor data
The newly developed sensors show outliers in the data. The reason why the outliers are reported is not fully clear, but it is important to have tools that can tell us if any changes applied actually improve the output.
Task: Outlier Detection
Sample data will be made available in the form of a pickled pandas DataFrame. The task is to output an outlier frequency per sensor type and sensor unit, e.g.:
SensorA:
CO2: x outliers/h
PM1.0: y outliers/h
The output should be put in a JSON structure (nested dictionaries), e.g.:

{<sensor_id>:
	{‘CO2’: x,
	‘PM1.0’: y,
	}
}

The script needs to run as a standalone script (run on the command line).
