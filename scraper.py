import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

#response = requests.get(url)
response = requests.get(url,headers={
    "User-Agent":"Mozilla/5.0"
},timeout=20
)
print(response.status_code)

soup = BeautifulSoup(response.text,"html.parser")
books = soup.find_all("article",class_="product_pod")

data =[]
for book in books:
    title = book.h3.a["title"]
    price = book.find("p",class_="price_color").text
    rating = book.find("p",class_="star-rating")["class"][1]
    data.append([title,price,rating])

    #save data to csv file
    with open("books_data.csv","w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Title","Price","Rating"])
        writer.writerows(data)

        print( f"Scraped {len(data)} books successfully!" )
        print("Data saved to books_data.csv") # name of the sheet in csv file
