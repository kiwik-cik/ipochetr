class Abonent:#Класс Abonent - это базовый класс с основной информацией об абоненте, такой как фамилия, имя, отчество, адрес и паспортные данные. В нем определены конструктор __init__, который инициализирует атрибуты абонента, и метод __str__, который возвращает строковое представление абонента.
    def __init__(self, last_name, first_name, middle_name, address, city, passport):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.city = city
        self.passport = passport

    def __str__(self):
        return f"Фамилия: {self.last_name}\nИмя: {self.first_name}\nОтчество: {self.middle_name}\nАдрес: {self.address}\nГород: {self.city}\nПаспортные данные: {self.passport}"

class InternationalCall(Abonent):#Класс InternationalCall наследует от класса Abonent и добавляет дополнительные атрибуты, связанные с международными звонками, такие как страна, код города, длительность звонка, цена и сумма оплаты. В нем также переопределен метод __str__ для корректного вывода информации о международных звонках
    def __init__(self, last_name, first_name, middle_name, address, city, passport, country, city_code, duration, price, payment_amount, month, year):
        super().__init__(last_name, first_name, middle_name, address, city, passport)
        self.country = country
        self.city_code = city_code
        self.duration = duration
        self.price = price
        self.payment_amount = payment_amount
        self.month = month
        self.year = year

    def __str__(self):
        return f"{super().__str__()}\nСтрана: {self.country}\nКод города: {self.city_code}\nДлительность звонка (в минутах): {self.duration}\nЦена: {self.price}\nСумма оплаты: {self.payment_amount}\nМесяц: {self.month}\nГод: {self.year}"

class CityCall(Abonent):#Класс CityCall также наследует от класса Abonent и добавляет атрибуты, связанные с городскими звонками, такие как тариф, длительность звонка, сумма оплаты и дата (месяц и год). Метод __str__ переопределен для правильного вывода информации об абоненте городских звонков
    def __init__(self, last_name, first_name, middle_name, address, city, passport, tariff, duration, payment_amount, month, year):
        super().__init__(last_name, first_name, middle_name, address, city, passport)
        self.tariff = tariff
        self.duration = duration
        self.payment_amount = payment_amount
        self.month = month
        self.year = year

    def __str__(self):
        return f"{super().__str__()}\nТариф: {self.tariff}\nДлительность звонка (в минутах): {self.duration}\nСумма оплаты: {self.payment_amount}\nМесяц: {self.month}\nГод: {self.year}"

class InternetConnection(Abonent):#Класс InternetConnection добавляет атрибуты, связанные с интернет-подключением, такие как название подключения, предоставленный объем, сумма оплаты, месяц и год. В конструкторе __init__ инициализируются атрибуты, а метод __str__ переопределен для вывода информации об интернет-подключении в виде строки
    def __init__(self, last_name, first_name, middle_name, address, city, passport, connection_name, provided_volume, payment_amount, month, year):
        super().__init__(last_name, first_name, middle_name, address, city, passport)
        self.connection_name = connection_name
        self.provided_volume = provided_volume
        self.payment_amount = payment_amount
        self.month = month
        self.year = year

    def __str__(self):
        return f"{super().__str__()}\nНазвание подключения: {self.connection_name}\nПредоставленный объем: {self.provided_volume}\nСумма оплаты: {self.payment_amount}\nМесяц: {self.month}\nГод: {self.year}"
#Затем результаты выводятся с помощью функции print(). После создания экземпляров каждого класса, они выводятся в консоль, используя метод __str__, который возвращает строковое представление объекта
international_call = InternationalCall("Иванов", "Иван", "Иванович", "ул. Ленина, 10", "Москва", "1234567890", "USA", "+1", 10, 1.5, 15, "январь", 2022)
city_call = CityCall("Петров", "Петр", "Петрович", "ул. Пушкина, 5", "Санкт-Петербург", "0987654321", "Стандартный", 5, 3, "февраль", 2022)
internet_connection = InternetConnection("Сидоров", "Алексей", "Алексеевич", "ул. Гагарина, 15", "Екатеринбург", "5432167890", "Быстрый интернет", 100, 20, "март", 2022)

print(international_call)
print()
print(city_call)
print()
print(internet_connection)