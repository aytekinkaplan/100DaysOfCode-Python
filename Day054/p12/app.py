import time  # Zaman ölçümü için time kütüphanesini import ediyoruz

# Şu anki zaman damgasını alıyoruz
current_time = time.time()
print(f"Current time (seconds since Jan 1st, 1970): {current_time}")

# Zaman ölçümü yapan dekoratörü tanımlıyoruz
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Fonksiyonun başlamadan önceki zamanı alıyoruz
        result = func(*args, **kwargs)  # Fonksiyonu çağırıyoruz
        end_time = time.time()  # Fonksiyonun bitimindeki zamanı alıyoruz
        elapsed_time = end_time - start_time  # Geçen süreyi hesaplıyoruz
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to complete")
        return result  # Fonksiyonun sonucunu döndürüyoruz
    return wrapper

# Bu fonksiyon, sadece zaman ölçümünü göstermek için dekoratörü test ediyor
@timer
def speed_calc_decorator():
    pass  # İçerik eklenmedi, sadece zaman ölçümünü test etmek için

# Hızlı işleyen fonksiyonu tanımlıyoruz
@timer
def fast_function():
    for i in range(1_000_000):  # 1 milyon iterasyon
        i * i

# Yavaş işleyen fonksiyonu tanımlıyoruz
@timer
def slow_function():
    for i in range(10_000_000):  # 10 milyon iterasyon
        i * i

# Fonksiyonları çağırıyoruz ve performanslarını ölçüyoruz
print("Calling fast_function:")
fast_function()

print("\nCalling slow_function:")
slow_function()
