import requests

def fetch_barcode_info(barcode: str):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    if data.get("status") == 1:
        product = data.get("product", {})
        nutriments = product.get("nutriments", {})
        return {
            "product_name": product.get("product_name", "Unknown Product"),
            "image_url": product.get("image_url", ""),
            "macros": {
                "calories": nutriments.get("energy-kcal_100g", 0),
                "protein": nutriments.get("proteins_100g", 0),
                "carbs": nutriments.get("carbohydrates_100g", 0),
                "fat": nutriments.get("fat_100g", 0)
            }
        }
    return None

def fetch_food_macros_by_name(food_name: str):
    # Using OpenFoodFacts search API to get an approximation for a food category
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food_name}&search_simple=1&action=process&json=1&page_size=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("products") and len(data["products"]) > 0:
            product = data["products"][0]
            nutriments = product.get("nutriments", {})
            return {
                "calories": nutriments.get("energy-kcal_100g", 0),
                "protein": nutriments.get("proteins_100g", 0),
                "carbs": nutriments.get("carbohydrates_100g", 0),
                "fat": nutriments.get("fat_100g", 0)
            }
    
    # Fallback generic mapping if OFF fails to find a raw ingredient/food
    fallback_db = {
        "pizza": {"calories": 266, "protein": 11, "carbs": 33, "fat": 10},
        "apple_pie": {"calories": 237, "protein": 2, "carbs": 34, "fat": 11},
        "hamburger": {"calories": 295, "protein": 17, "carbs": 24, "fat": 14},
        "sushi": {"calories": 143, "protein": 4.5, "carbs": 30, "fat": 0.5},
        "salad": {"calories": 150, "protein": 5, "carbs": 10, "fat": 10},
    }
    
    for key, value in fallback_db.items():
        if key in food_name.lower():
            return value

    return {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
