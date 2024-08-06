# Nested Functions

def say_my_name(name):
    print(f"My name is {name}")

    def say_my_age(age):
        print(f"My age is {age}")

        def say_my_city(city):
            print(f"My city is {city}")

            def say_my_hobby(hobby):
                print(f"My hobby is {hobby}")

            # İç içe fonksiyonu burada çağırıyoruz
            say_my_hobby("reading")

        # Bir sonraki iç fonksiyonu burada çağırıyoruz
        say_my_city("New York")

    # İlk iç fonksiyonu burada çağırıyoruz
    say_my_age(30)


say_my_name("John")





