import json

# Parsing JSON Data
def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(data)
        
        
        for product in data:
            name = product.get('name')
            category = product.get('category')
            price = product.get('price')
            availability = product.get('availability')
            
            print(f"Name: {name}")
            print(f"Category: {category}")
            print(f"Price: {price}")
            print(f"Availability: {availability}\n")

# Adding New Product
def add_new_product(file_path, new_product_data):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    data.append(new_product_data)
    
    with open('updated_data.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # Path to the JSON file
    json_file_path = '13_A_Data.json'
    
    # Parsing the JSON file and printing the contents
    parse_json(json_file_path)
    
    # New product data to be added
    new_product = {
        "name": "Python Programming Book",
        "category": "Books",
        "price": 39.99,
        "availability": True
    }
    
    # Adding the new product and writing to a new file
    add_new_product(json_file_path, new_product)
