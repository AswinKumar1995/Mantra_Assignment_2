#program is complete


import pandas as pd # pyarrow package had to be pre installed(pip install pyarrow)
from pathlib import Path # pip install pathlib
def changeCSVtoParquet(fileLocation):
    df = pd.read_csv(fileLocation)
    df.to_parquet('output.parquet')
    mypath = Path().absolute() # hass current working directory
    print(f"File is stored in below location : \n {mypath} ")
fileLocation = input("Please provide the file location : ") #http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv 
changeCSVtoParquet(fileLocation)
