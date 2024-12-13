#Flask, Python ile web uygulamaları ve RESTful API'ler geliştirmek için kullanılan popüler ve hafif bir web çerçevesidir.
#Flask, basit ve genişletilebilir bir yapıya sahip, Python tabanlı bir web framework'tür. 
#Flask, "mikro çerçeve" olarak adlandırılır çünkü temel özelliklerle başlar ve kullanıcı ihtiyaçlarına göre genişletilebilir.

#Flask'ı indir ve kur:

pip install flask

#############################################################################################################

#Basit Flask Uygulaması Oluşturma:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba, Flask ile web uygulamanız çalışıyor!"

if __name__ == "__main__":
    app.run(debug=True)

#Flask importu: Flask sınıfını içe aktarır ve uygulamanızı başlatır.
#app.route('/'): Ana sayfa (/) için bir URL rotası tanımlar.
#app.run(debug=True): Uygulamanın hata ayıklama modunda çalışmasını sağlar.
#Bu, kodda bir değişiklik olduğunda uygulamanın otomatik olarak yeniden başlatılmasını sağlar.

#############################################################################################################