from collections import Counter
import csv
import os
import locale

def analyze_sales_data(filename):
    products = {}
    collection = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            collection.append(product)

            if product in products:
                products[product] += sales
            else:
                products[product] = sales

    print(collection) 

    #TODO: Hitta den mest sålda produkten (TIPS! Använd Counter från collections)
    most_common_product = Counter(collection).most_common(1)[0]

    # Hitta den mest lukrativa produkten
    most_lucrative_product = max(products, key=products.get)
    
    # Genomsnittlig försäljning per produkt
    average_sales = sum(products.values()) / len(products)

    print(f"Mest sålda produkt:", most_common_product[0], "Antal:", most_common_product[1])  #FIXME: Redovisa mest sålda produkt här
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(products[most_lucrative_product],grouping=True)}")
    print(f"Genomsnittlig försäljning per produkt: {locale.currency(average_sales, grouping=True)}")


# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
analyze_sales_data('sales_data.csv')
