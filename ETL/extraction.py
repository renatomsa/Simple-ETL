import pandas as pd
import xml.etree.ElementTree as ET

## Creating DataFrames from different FileTypes
class CDataFrame:
  def __init__(self, file) -> None:
    self.file = file

  def extract_csv(self):
    df = pd.read_csv(self.file)
    return df

  def extract_json(self):
    df = pd.read_json(self.file, lines=True)
    return df

  def extract_xml(self):
    df = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    tree = ET.parse(self.file)
    root = tree.getroot()
    for car in root:
      model = car.find("car_model").text
      year_manufact = car.find("year_of_manufacture").text
      price = float(car.find("price").text)
      fuel = car.find("fuel").text
    return df
