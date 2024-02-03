#Forbes 2022 Dataset

import pandas as pd 

df=pd.read_csv("forbes_2022_billionaires.csv")
print(df.head())

#Harf ve işaretleri kaldırmalıyız. Sayısal olması gereken sütunlara dönüşüm uygulamalıyız.

print(df.columns)
#Bazı sütun isimlerinde boşluklar var, _ ile o boşlukları doldurmalıyız.
#df.columns=df.columns.str.replace(" ","_")
print(df.columns)

print(df.shape)
#Satır --> Örneklem
#Sütun --> Öznitelik
#print(df.dtypes)
#Object veri tipi --> sayısal veri tipine dönüştürülmelidir.

#print(df.isnull().sum())
#Rating sütununda çok fazla eksik veri var.

import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

sns.set_theme()
sns.set(rc={"figure.dpi":90,"figure.figsize":(12,9)})
#sns.heatmap(df.isnull(),cbar=False)
#print(plt.show())

#Eksik verileri kaldırmak, bilgi kaybına yol açacağı için yerlerini veri setinin medyanlarıyla dolduracağız.

#rating_median=df["Rating"].median()
#print(rating_median)
#df["Rating"].fillna(rating_median,inplace=True)
#Diğer eksik veri sayısı az olduğu için direkt kaldırdık.
#df.dropna(inplace=True)
#print(df.isnull().sum().sum())
#print(df.info)

#Şimdi object --> int64
#df["Reviews"].describe()
#df["Reviews"]=df["Reviews"].astype("int64")
#df["Reviews"].describe().round()
#Yuvarlama işlemi yaptık.

#Şimdi M ve k harflerini kaldıracağız.
#df["Size"].replace("M","",regex=True,inplace=True)
#df["Size"].replace("k","",regex=True,inplace=True)
#df["Size"].unique()
#Bir tane metin içeren sütun var.
#size_median=df[df["Size"]!="Varies with device"]["Size"].astype(float).median()
#df["Size"].replace("Varies with device",size_median,inplace=True)
#df.Size=pd.to_numeric(df.Size)
#print(df.Size.head())
#df.Size.describe().round()

#Şimdi + ve , işaretlerini kaldıralım. Sonra int değerine dönüştürelim.
#df.Installs=df.Installs.apply(lambda x:x.replace("+",""))
#df.Installs=df.Installs.apply(lambda x:x.replace(",",""))
#df.Installs=df.Installs.apply(lambda x:int(x))
#df.Installs.unique()

#Şimdi $ sembolünü kaldıralım.
#df.Price=df.Price.apply(lambda x:x.replace("$",""))
#df.Price=df.Price.apply(lambda x:float(x))
#df.Price.unique()

#Şimdi ; işaretini kaldıralım. Sonra Tür ve Alan olmak üzere öznitelikleri ayıralım.
#df.Genres=df.Genres.str.split(";").str[0]
#df.Genres.unique()
#Music ve Music&Audio türlerini birleştirelim.
#df.Genres.replace("Music & Audio","Music",inplace=True)

#df.Last_Updated=pd.to_datetime(df.Last_Updated)

#Şimdi veri görselleştirme aşamasına geçiyoruz.
#df["Type"].value_counts().plot(kind="bar",color="blue")
#print(plt.show())
#Free uygulama sayısının paid uygulama sayısından çok olduğunu gördük.
#sns.boxplot(x="Type",y="Rating",data=df)
#print(plt.show())

#sns.countplot(y="Content_Rating",data=df)
#plt.title("Content rating with their counts")
#print(plt.show())

#sns.boxplot(x="Content_Rating",y="Rating",data=df)
#print(plt.show())

#cat_num=df["Category"].value_counts()
#sns.barplot(x=cat_num,y=cat_num.index,data=df)
#plt.title("The number of categories")
#print(plt.show())

#sns.scatterplot(data=df,y="Category",x="Price")
#print(plt.show())

#sns.histplot(df["Rating"],kde=True)
#print(plt.show())

#########################################

#Üzerinde çalışacağımız sütunları seçiyoruz.

df=df.loc[:,["rank","personName","age","finalWorth","category","country","gender"]]
print(df.head())

df=df.rename(columns={"rank":"Rank","personName":"Name","age":"Age","finalWorth":"TotalWorth","category":"Category","country":"Country","gender":"Gender"})
print(df.head())

#Rank sütunu 1'den başlayıp artarak ilerlediği için onu index sütunu olarak kabul edebiliriz.
df=df.set_index("Rank")
print(df.head())

print(df.dtypes)
print(df.isnull().sum())
df.dropna(inplace=True)

#Veri ön işleme bitti. Şimdi bilgileri çıkaracağız.
print(df["Gender"].value_counts(normalize=True))
print(df[df["Country"]=="Turkey"].Gender.value_counts())

df_gender=df.groupby(["Gender"])
df_gender.Age.mean()

df_gender.size().plot(kind="bar")
sns.barplot(x=df.TotalWorth[:10],y=df.Name[:10])

df_country=df.groupby("Country")
df_country_count=pd.DataFrame(df._country.size().sort_values(ascending=False),columns=["Counts"])
sns.barplot(x=df_country_count["Counts"][:10],y=df_country_count.index[:10])
