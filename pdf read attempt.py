import pandas
import numpy as np


frames = pandas.DataFrame({'a':[],'b':[],'c':[]})
import tabula

dfList = tabula.read_pdf('C:/users/DX/Desktop/021.pdf', multiple_tables=True, pages='all')
#print(dfList)

frames=pandas.concat(dfList, axis=1)

print(frames)
#pandas.
    #print(df['Βαθμός'])