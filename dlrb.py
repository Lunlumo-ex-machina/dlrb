import requests
from bs4 import BeautifulSoup as bs

def main():
    req = requests.get("https://www.dolar.blue")
    div = bs(req.text, "html.parser").body.find("div", class_="container pricing-table-container")
    rows = [div.contents[1], div.contents[1].next_sibling.next_sibling]
    blue = rows[0].find_all("p", class_="price-blue")
    oficial = rows[1].find_all("p", class_="price")

    print(f"+{'+':->28}")
    print(f"|{' ':^9}|{'Compra':^8}|{'Venta':^8}|")
    print(f"+{'+':->10}{'+':->9}{'+':->9}")
    print(f"|{'Blue':^9}| {blue[0].next:6} | {blue[1].next:6} |")
    print(f"| Oficial | {oficial[0].next:6} | {oficial[1].next:6} |")
    print(f"+{'+':->28}")

if __name__ == "__main__":
    main()
