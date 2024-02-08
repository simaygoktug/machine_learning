#pandas küçük veya orta boyutlu verilerle çalışmak için uygun bir kütüphanedir.

#BigQuery bulut serivisi ise büyük verilerle çalışmak için çok iyidir.

#Amazon karşılığı --> Amazon Athena&Redshift
#Azure karşılığı --> Azure Synapse Analytics

#Google Cloud sol üstteki 3 çizgiden BigQuery tıkla.
#Create dataset
#Add Data
#Pin a project --> Enter project name 
#bigquery-public-data --> PIN
#Aşağıya in --> ml_datasets
#penguins

#Sekme tarafından +'ya bas ve yeni editör aç.
#CREATE OR REPLACE MODEL "projenin_adı.dataset_adı.penguins_model"
#OPTIONS (model_type="linear_reg",input_label_cols=["body_mass_g"]) AS 
#SELECT * (MySQL dili gibi)
#FROM "bigquery-public-data.ml_datasets.penguins"
#WHERE body_mass_g IS NOT NULL

#RUN tuşuna bas.
#Sol taraftan Models --> penguins_model --> TRAINING --> Table (hatamıza baktık.)

#Sekme tarafından +'ya bas ve yeni editör aç.
#SELECT * FROM ML.EVALUATE(MODEL "projenin_adı.dataset_adı.penguins_model",(SELECT * FROM "bigquery-public-data.ml_datasets.penguins" WHERE body_mass_g IS NOT NULL))
#Query Results --> Results --> r^2 değeri 1'e ne kadar yakınsa o kadar iyi.
