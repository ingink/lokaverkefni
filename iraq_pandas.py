import pandas as pd
import csv as csv

#færa inn hrá gögn
csv_file_object = csv.reader(open('iraq-war-diary-redacted.csv'),delimiter=",")
haus = next(csv_file_object)
iraq_diary = pd.read_csv('iraq-war-diary-redacted.csv',sep=",",names=haus,skiprows=1)
df = iraq_diary[["date","type","title","summary","attackon","friendlywia","friendlykia","hostnationwia","hostnationkia","civilianwia","civiliankia","enemywia","enemykia","enemydetained","latitude","longitude"]]

#taka út allar villur í kia data:
df.ix[0:,5:]=df.ix[0:,5:].convert_objects(convert_numeric=True)
df=df.dropna(subset = ["friendlywia","friendlykia","hostnationwia","hostnationkia","civilianwia","civiliankia","enemywia","enemykia","enemydetained","latitude", "longitude"])
df=df.reset_index(drop=True)

#breyta dagsetningum i datetime og raða eftir dags.:
df.date=pd.to_datetime(df.date,errors="coerce")
df=df.dropna(subset = ["date"])
df.date=pd.to_datetime(df.date)
df=df.sort('date')
df=df.reset_index(drop=True)

tmp = df.iloc[:,[0,1,4,5,6,7,8,9,10,11,12,13,14,15]]
tmp = tmp[8:]

#print(tmp)
tmp.to_csv('data.csv', sep=',')



#print(df.head())
#print(type(df.date[0]))
#print(len(df.date))
#print("The data is from {} to {}".format(df.date.min(),df.date.max()))
#print("It takes place on the area bound between latitude {} and {}\nand longitude {} and {}".format(df.latitude.min(),df.latitude.max(),df.longitude.min(),df.longitude.max()))
#df["date"]=df["date"].astype('datetime64[ns]')
#df = df.groupby(df.date).sum()
#print("The total number of americans killed was: {}".format(df["friendlykia"].astype(int).sum()))
#print("The total number of americans wounded was: {}".format(df["friendlywia"].astype(int).sum()))
#print("The total number of civilians killed was: {}".format(df["civiliankia"].astype(int).sum()))
#print("The total number of civilians wounded was: {}".format(df["civilianwia"].astype(int).sum()))
#print("The total number of 'friendly iraqis' killed was: {}".format(df["hostnationkia"].astype(int).sum()))
#print("The total number of 'friendly iraqis' wounded was: {}".format(df["hostnationwia"].astype(int).sum()))
#print("The total number of enemies killed was: {}".format(df["enemykia"].astype(int).sum()))
#print("The total number of enemies wounded was: {}".format(df["enemywia"].astype(int).sum()))
#print("The total number of enemies detained was: {}".format(df["enemydetained"].astype(int).sum()))
#print("This adds up to a total of {} wounded and {} killed".format(   df["enemywia"].astype(int).sum()+df["hostnationwia"].astype(int).sum()+df["civilianwia"].astype(int).sum()+df["friendlywia"].astype(int).sum()   ,   df["enemykia"].astype(int).sum()+df["hostnationkia"].astype(int).sum()+df["civiliankia"].astype(int).sum()+df["friendlykia"].astype(int).sum()   ))
#print("There of, only {0:.1f}% those killed were americans".format(100*df["friendlykia"].astype(int).sum()/( df["enemykia"].astype(int).sum()+df["hostnationkia"].astype(int).sum()+df["civiliankia"].astype(int).sum()+df["friendlykia"].astype(int).sum() )))
#print("{} civilians were killed with improvised explosive devices".format(df[df['title'].str.contains("IED")].civiliankia.astype(int).sum()))
#print("{} civilians were killed with improvised explosive devices".format(df[df['title'].str.contains(" IED EXPLOSION")].civiliankia.astype(int).sum()))


