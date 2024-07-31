def get_travel_log():
    travel_log = []

    countries_visited = input("Enter countries you have visited, separated by commas: ").split(",")

    for country in countries_visited:
        country = country.strip()
        cities_visited = input(f"Enter cities you have visited in {country}, separated by commas: ").split(",")
        visits = input(
            f"Enter the number of times you have visited each city in {country}, separated by commas: ").split(",")

        cities_info = []
        for i in range(len(cities_visited)):
            city = cities_visited[i].strip()
            visit_count = int(visits[i].strip())
            cities_info.append({"city": city, "visits": visit_count})

        new_country = {
            "country": country,
            "cities": cities_info
        }
        travel_log.append(new_country)

    return travel_log


travel_log = get_travel_log()
print(travel_log)
