import pandas
# Pandas kütüphanesini içe aktarır. Pandas, veri analizi için kullanılan güçlü bir Python kütüphanesidir.

data = pandas.read_csv("weather_data.csv")
# "weather_data.csv" dosyasını okur ve içeriğini bir pandas DataFrame'ine yükler.

print(data["temp"])
# "temp" sütunundaki tüm değerleri yazdırır.

data_dict = data.to_dict()
print(data_dict)
# DataFrame'i bir sözlüğe dönüştürür ve yazdırır. Her sütun, sözlüğün bir anahtarı olur.

temp_list = data["temp"].to_list()
print(temp_list)
# "temp" sütunundaki değerleri bir liste olarak alır ve yazdırır.

average = sum(temp_list) / len(temp_list)
print(average)
# Sıcaklıkların ortalamasını manuel olarak hesaplar ve yazdırır.

print(data["temp"].mean())
# Pandas'ın mean() fonksiyonunu kullanarak sıcaklıkların ortalamasını hesaplar ve yazdırır.

print(data["temp"].max())
# "temp" sütunundaki en yüksek değeri bulur ve yazdırır.

monday = data[data.day == "Monday"]
print(monday)
# Günü "Monday" olan satırı seçer ve yazdırır.

monday_temp = int(monday.temp)
print(monday_temp)
# Pazartesi gününün sıcaklığını tam sayıya dönüştürür ve yazdırır.

monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)
# Pazartesi gününün sıcaklığını Fahrenheit'a dönüştürür ve yazdırır.