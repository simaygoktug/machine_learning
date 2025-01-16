#Transformers, NLP alanında devrim yaratan bir model mimarisidir. 
#BERT (Bidirectional Encoder Representations from Transformers), metin verilerini bağlam içinde anlamlandırmak için güçlü bir tekniktir. 
#Bu uygulamada, önceden eğitilmiş bir BERT modelini kullanarak metinlerin duygu analizi yapılacaktır.

pip install transformers torch datasets

data = [
    {"text": "I love this product!", "label": 1},  # Pozitif
    {"text": "This is the worst experience ever.", "label": 0},  # Negatif
    {"text": "It is okay, not great but not bad.", "label": 1}  # Pozitif
]

# Veriyi Pandas DataFrame'e dönüştürme
import pandas as pd
df = pd.DataFrame(data)
print(df)

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# BERT modelini ve tokenizer'ı yükle
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Tokenize et ve modelden tahmin al
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1)
    return "Positive" if prediction.item() == 1 else "Negative"

# Örnek metinlerin tahminini al
df['sentiment'] = df['text'].apply(analyze_sentiment)
print(df)

