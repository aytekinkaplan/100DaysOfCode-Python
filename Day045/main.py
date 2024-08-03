from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print("------------------------------------------------")
print(soup.prettify())
print("------------------------------------------------")
print(soup.a)
print(soup.a.attrs)
print(f"The link is: {soup.a["href"]}")
print("------------------------------------------------")
print(f" All links are: {soup.find_all("a")}")
print("------------------------------------------------")

all_anchor_tags = soup.find_all("a")

for link in soup.find_all("a"):
    print(link.get("href"))

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section = soup.find(name="h3", class_="heading")
print(section)
