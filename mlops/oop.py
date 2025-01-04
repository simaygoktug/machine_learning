#OOP, nesnelerle çalışan programlama paradigmasıdır. OOP’nin temel taşları:

#Encapsulation (Kapsülleme): Veriyi gizleme ve koruma.
#Inheritance (Kalıtım): Kod tekrarını azaltma ve yeniden kullanılabilirlik.
#Polymorphism (Çok Biçimlilik): Aynı yöntem farklı nesnelerde farklı davranabilir.
#Abstraction (Soyutlama): Gereksiz detayları gizleyerek önemli olan kısımları vurgulama.

#SOLID Prensipleri: OOP'yi daha sağlam ve sürdürülebilir yapmak için geliştirilmiştir.

#S: Single Responsibility Principle (SRP) - Her sınıf yalnızca bir sorumluluğa sahip olmalıdır.
#O: Open/Closed Principle (OCP) - Bir sınıf genişletilmeye açık, değiştirilmeye kapalı olmalıdır.
#L: Liskov Substitution Principle (LSP) - Alt sınıflar, üst sınıfların yerini alabilmelidir.
#I: Interface Segregation Principle (ISP) - İstemciler kullanmadıkları arayüzlere bağımlı olmamalıdır.
#D: Dependency Inversion Principle (DIP) - Üst seviyeli modüller alt seviyelilere bağımlı olmamalıdır.

#Pratik Örnek:
# Single Responsibility Principle
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount * 1.18  # 18% VAT


class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice Total: {invoice.calculate_total()}")

invoice = Invoice(100)
printer = InvoicePrinter()
printer.print_invoice(invoice)

#Recursion (Özyineleme)

#Recursion, bir fonksiyonun kendisini çağırdığı durumdur. Çoğunlukla böl ve yönet algoritmalarında kullanılır. Temel olarak:
#Base Case: Fonksiyonun durması gereken koşul.
#Recursive Case: Fonksiyonun kendisini çağırdığı durum.

#Pratik Örnek:
# Divide & Conquer uygulamalarında da yani QuickSort applicationda da kullanılır.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 55

#Polymorphism (Çok Biçimlilik)

#Polymorphism, aynı isimli bir yöntemin farklı sınıflar tarafından farklı şekillerde uygulanabilmesidir. İki türde görülebilir:
#Method Overriding (Metot Ezme): Alt sınıflarda üst sınıfın metotlarının yeniden tanımlanması.
#Method Overloading (Metot Aşırı Yükleme): Aynı isme sahip ancak farklı parametrelerle çalışan metotlar.

#Pratik Örnek:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

#Dynamic Memory Allocation (Dinamik Bellek Yönetimi)

#Dinamik bellek yönetimi, belleği program çalışırken ayırma ve serbest bırakma işlemidir. 
#Python'da bellek yönetimi genellikle otomatik olsa da, dilin altında bu işlemler yapılır. 
#C/C++ gibi dillerde malloc, free gibi fonksiyonlar kullanılır.

#Pratik Örnek:

import gc

# Garbage Collector'ı manuel çalıştırmak
gc.collect()

#Inheritance (Kalıtım)

#Inheritance, bir sınıfın başka bir sınıfın özelliklerini devralmasıdır. 
#Bu, kodun yeniden kullanılabilirliğini artırır ve modüler hale getirir.

#Pratik Örnek:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} çalışıyor!")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} sürülüyor!")

car = Car("Toyota")
car.start()
car.drive()

#Abstraction ve Interfaces (Soyutlama ve Arayüzler)

#Abstraction, yalnızca önemli bilgileri gösterirken gereksiz detayları gizler. 
#Interface ise bir sınıfın uygulaması gereken bir grup metot bildirir.

#Pratik Örnek:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 78.5
