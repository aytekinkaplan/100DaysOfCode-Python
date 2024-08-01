from prettytable import PrettyTable, MARKDOWN

# City Information Table
city_table = PrettyTable(["City Name", "Area", "Population", "Annual Rainfall"])
city_table.set_style(MARKDOWN)
city_table.add_row(["Adelaide", 1295, 1158259, 600.5])
city_table.add_row(["Brisbane", 5905, 1857594, 1146.4])
city_table.add_row(["Darwin", 112, 120900, 1714.7])
city_table.add_row(["Hobart", 1357, 205556, 619.5])
city_table.add_row(["Sydney", 2058, 4336374, 1214.8])
city_table.add_row(["Melbourne", 1566, 3806092, 646.9])
city_table.add_row(["Perth", 5386, 1554769, 869.4])
city_table.align["City Name"] = "l"
city_table.align["Area"] = "c"
city_table.align["Population"] = "c"
city_table.align["Annual Rainfall"] = "c"
print(city_table)
print("----------------------------------------------------------------------------------")
print(city_table.get_string(sortby="City Name"))
print("----------------------------------------------------------------------------------")
# Employee Information Table
employee_table = PrettyTable(["Employee Name", "Employee ID", "Role", "Salary"])
employee_table.set_style(MARKDOWN)
employee_table.add_row(["John Doe", 12345, "Manager", "$50,000"])
employee_table.add_row(["Jane Smith", 54321, "Developer", "$30,000"])
print("----------------------------------------------------------------------------------")
# Product Table
product_table = PrettyTable(["Product Name", "Price", "Stock"])
product_table.set_style(MARKDOWN)
product_table.add_row(["Laptop", "$999.99", 25])
product_table.add_row(["Smartphone", "$499.99", 50])
product_table.add_row(["Tablet", "$299.99", 35])
product_table.add_row(["Headphones", "$99.99", 100])
product_table.add_row(["Smartwatch", "$199.99", 75])
print(product_table)
print("----------------------------------------------------------------------------------")
# Student Grades Table
student_table = PrettyTable(["Student Name", "Math", "Science", "English"])
student_table.set_style(MARKDOWN)
student_table.add_row(["John Doe", 85, 92, 78])
student_table.add_row(["Jane Smith", 90, 88, 84])
student_table.add_row(["Emily Davis", 76, 95, 80])
student_table.add_row(["Michael Brown", 89, 90, 92])
student_table.add_row(["Jessica White", 95, 94, 93])
student_table.add_row(["David Wilson", 81, 87, 79])
student_table.add_row(["Sarah Taylor", 83, 85, 82])
student_table.add_row(["Olivia Anderson", 87, 91, 86])
student_table.add_row(["Daniel Thompson", 92, 93, 91])
student_table.add_row(["Sophia Martinez", 79, 88, 83])
student_table.add_row(["Matthew Clark", 94, 90, 94])
student_table.add_row(["Ava Rodriguez", 80, 86, 81])
student_table.add_row(["James Harris", 85, 89, 87])
student_table.add_row(["Emma Walker", 91, 92, 90])
student_table.add_row(["William Allen", 82, 87, 84])
student_table.add_row(["Ethan Young", 93, 91, 95])
student_table.add_row(["Abigail Moore", 78, 86, 80])
student_table.align["Math"] = "c"
student_table.align["Science"] = "c"
student_table.align["English"] = "c"
student_table.align["Student Name"] = "l"
student_table.border = True
student_table.padding_width =1
print(student_table)
print("----------------------------------------------------------------------------------")
# Movie List Table
movie_table = PrettyTable(["Movie Title", "Director", "Year"])
movie_table.set_style(MARKDOWN)
movie_table.add_row(["The Shawshank Redemption", "Frank Darabont", 1994])
movie_table.add_row(["The Godfather", "Francis Ford Coppola", 1972])
movie_table.add_row(["The Dark Knight", "Christopher Nolan", 2008])
movie_table.add_row(["Pulp Fiction", "Quentin Tarantino", 1994])
movie_table.add_row(["Forrest Gump", "Robert Zemeckis", 1994])
movie_table.add_row(["Inception", "Christopher Nolan", 2010])
movie_table.add_row(["The Lord of the Rings: The Return of the King", "Peter Jackson", 2003])
movie_table.add_row(["The Matrix", "The Wachowskis", 1999])
movie_table.add_row(["The Silence of the Lambs", "Jonathan Demme", 1991])
movie_table.add_row(["Interstellar", "Christopher Nolan", 2014])
movie_table.add_row(["The Prestige", "Christopher Nolan", 2006])
movie_table.add_row(["The Departed", "Martin Scorsese", 2006])
movie_table.align = "l"
print(movie_table)
print("----------------------------------------------------------------------------------")
# Sports Teams Table
team_table = PrettyTable(["Team Name", "Sport", "Championships"])
team_table.set_style(MARKDOWN)
team_table.add_row(["Los Angeles Lakers", "Basketball", 17])
team_table.add_row(["New York Yankees", "Baseball", 27])
team_table.add_row(["New England Patriots", "American Football", 6])
team_table.add_row(["Chicago Bulls", "Basketball", 6])
team_table.add_row(["Liverpool FC", "Soccer", 19])
team_table.add_row(["Milwaukee Bucks", "Basketball", 7])
team_table.add_row(["Philadelphia 76ers", "Basketball", 4])
team_table.add_row(["Boston Celtics", "Basketball", 5])
team_table.add_row(["Toronto Raptors", "Basketball", 5])
team_table.add_row(["Miami Heat", "Basketball", 5])
team_table.add_row(["Cleveland Cavaliers", "Basketball", 5])
team_table.add_row(["Indiana Pacers", "Basketball", 5])
team_table.add_row(["Washington Wizards", "Basketball", 5])
team_table.add_row(["Brooklyn Nets", "Basketball", 5])
team_table.add_row(["Orlando Magic", "Basketball", 5])
team_table.add_row(["Atlanta Hawks", "Basketball", 5])
team_table.add_row(["Charlotte Hornets", "Basketball", 5])
team_table.add_row(["Detroit Pistons", "Basketball", 5])
team_table.align["Team Name"] = "l"
team_table.align["Sport"] = "l"
team_table.align["Championships"] = "l"
print(team_table)
print("----------------------------------------------------------------------------------")
