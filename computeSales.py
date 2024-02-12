import json
import sys
from datetime import datetime
import unidecode


def compute_total_cost(price_catalogue, sales_record):
    """Calcula el costo total de las ventas."""
    with open(price_catalogue, 'r', encoding='utf-8') as file:
        products = json.load(file)
        prices = {
            unidecode.unidecode(product['title'].lower().strip()): product['price']
            for product in products
        }

    total_cost = 0
    with open(sales_record, 'r', encoding='utf-8') as file:
        sales = json.load(file)
        for sale in sales:
            product_title = unidecode.unidecode(sale['Product'].lower().strip())
            quantity = sale['Quantity']
            if product_title in prices:
                product_price = prices[product_title]
                total_cost += product_price * quantity
            else:
                print(f"Error: El producto '{product_title}' no se encontró en el catálogo de precios.")
    return total_cost


def main():
    """Función principal que ejecuta el cálculo de costo y registra el resultado."""
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = datetime.now()
    price_catalogue = sys.argv[1]
    sales_record = sys.argv[2]
    total_cost = compute_total_cost(price_catalogue, sales_record)
    end_time = datetime.now()

    print(f"Costo total: {total_cost}")
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido: {elapsed_time}")

    with open("SalesResults.txt", 'a', encoding='utf-8') as file:
        file.write(f"Fecha y hora de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Costo total: {total_cost}\n")
        file.write(f"Tiempo transcurrido: {elapsed_time.total_seconds()} segundos\n")
        file.write("-" * 20 + "\n")


if __name__ == "__main__":
    main()
