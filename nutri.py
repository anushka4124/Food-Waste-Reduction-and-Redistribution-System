import requests


API_KEY ='h8F03dtkxI2mDLCLbewdVetm3BBc9a2r7vyKt11z'

def get_nutritional_info(food_name):
    base_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

    params = {
        'query': food_name,
        'api_key': API_KEY
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'foods' in data and len(data['foods']) > 0:
            food_item = data['foods'][0]

            nutrients = food_item['foodNutrients']
            nutrient_data = {}
            for nutrient in nutrients:
                nutrient_data[nutrient['nutrientName']] = nutrient['value']

            return nutrient_data
        else:
            print(f"Error: Unable to retrieve data for {food_name}")
            return None
    else:
        print(f"Error: Unable to retrieve data for {food_name}")
        return None


