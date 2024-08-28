from collections import defaultdict, Counter

def analyze_purchases(purchases: list) -> dict:
    # Initialize dictionaries to hold the results
    customer_purchases = defaultdict(lambda: defaultdict(int))
    product_counts = defaultdict(Counter)
    
    # Analyze purchases
    for customer_id, product_category, product_name in purchases:
        # Count the number of times a customer bought the same product in the same category
        customer_purchases[customer_id][product_category] += 1
        # Count how often each product is bought in each category
        product_counts[product_category][product_name] += 1

    # Find the most frequent product in each category
    most_frequent = {}
    for category, products in product_counts.items():
        # Find the product with the highest count, and choose lexicographically smallest if there's a tie
        most_frequent_product = min(products.items(), key=lambda x: (-x[1], x[0]))
        most_frequent[category] = most_frequent_product[0]
    
    # Prepare the result dictionary
    result = {customer_id: dict(purchases) for customer_id, purchases in customer_purchases.items()}
    result["most_frequent"] = most_frequent
    
    return result

# Example usage
purchases = [
    ("cust1", "electronics", "laptop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "laptop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera"),
]

print(analyze_purchases(purchases))
