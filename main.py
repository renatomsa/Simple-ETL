import glob
import pandas as pd
import ETL.extraction as EX

target_file = "transformed_data/data.csv"

# Processing data

def extracting():
  extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

  for csvfile in glob.glob("raw_data/*.csv"):
    extracted_data = pd.concat([extracted_data, pd.DataFrame(EX.CDataFrame(csvfile).extract_csv())], ignore_index=True)

  for jsonfile in glob.glob("raw_data/*.json"):
    extracted_data = pd.concat([extracted_data, pd.DataFrame(EX.CDataFrame(jsonfile).extract_json())], ignore_index=True)

  for xmlfile in glob.glob("raw_data/*.xml"):
    extracted_data = pd.concat([extracted_data, pd.DataFrame(EX.CDataFrame(xmlfile).extract_xml())], ignore_index=True)

  return extracted_data

#
# Transforming Data
#

def transform(data):
  data['price'] = round(data.price)
  return data

#
# Loading Data
#

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)


## ETL!!

extracted_data = extracting()
transformed_data = transform(extracted_data)

load_data(target_file, transformed_data)
