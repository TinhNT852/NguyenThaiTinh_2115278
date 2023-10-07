import pandas as pd

df  = pd.read_csv("D:\\DaiHocDaLat\\HocTAP\\Python\\Automobile_data.csv")

# print(df)
# print(df.head(6))
# print(df.tail(7))



df = df [['company', 'price']][df.price == df['price'].max()]
print(df)

# car_Manufacturers = df.groupby('company')
# toyotaDf = car_Manufacturers.get_group('toyota')
# print(toyotaDf)
# print(df['company'].value_counts())



# car_Manufacturers = df.groupby('company')
# priceDf = car_Manufacturers[['company', 'price']].mean('price')
# print(priceDf)