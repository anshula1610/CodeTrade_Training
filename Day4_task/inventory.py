import csv
from typing import Optional


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return (
            f"Product(Name={self.name}, "
            f"Price={self.price}, "
            f"Quantity={self.quantity})"
        )


class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def total_value(self) -> float:
        return sum(
            product.price * product.quantity
            for product in self.products
        )

    def find_product(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def save_to_csv(self, filename: str) -> None:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["name", "price", "quantity"])

            for product in self.products:
                writer.writerow([
                    product.name,
                    product.price,
                    product.quantity
                ])

    def load_from_csv(self, filename: str) -> None:
        self.products.clear()

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    row["name"],
                    float(row["price"]),
                    int(row["quantity"])
                )

                self.products.append(product)

    # -----------------------------
    # EXPLORE: Class Method Version
    # -----------------------------
    @classmethod
    def from_csv(cls, filename: str):
        inventory = cls()

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                inventory.add_product(
                    Product(
                        row["name"],
                        float(row["price"]),
                        int(row["quantity"])
                    )
                )

        return inventory


# -----------------------------
# Testing
# -----------------------------

inventory = Inventory()

inventory.add_product(Product("Laptop", 60000, 2))
inventory.add_product(Product("Mouse", 500, 10))
inventory.add_product(Product("Keyboard", 1200, 5))

print("Total Inventory Value:")
print(inventory.total_value())

print("\nSearching for Mouse:")
print(inventory.find_product("mouse"))

inventory.save_to_csv("products.csv")

print("\nInventory saved to products.csv")


# Load into a new inventory object

new_inventory = Inventory()
new_inventory.load_from_csv("products.csv")

print("\nLoaded Products:")

for product in new_inventory.products:
    print(product)


# Alternative classmethod approach

inventory_from_csv = Inventory.from_csv("products.csv")

print("\nLoaded using classmethod:")

for product in inventory_from_csv.products:
    print(product)