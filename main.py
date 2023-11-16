import predict as pred
import waste_detect as detect
import waste_graph as gr
import nutri as n
import pandas as pd
print("ResQbites: Transforming Waste into Ripples of Change")

print("Welcome Donor! \n\nFrom Plate to Planet: Analyzing Foodprints\n\n")

while (True):
    print("Choose an option: \n1. Generate the present accuracy of the model \n2. Predict the waste generation status of my food item \n3. Generate the Nutritional Analysis for the given food item \n4. Exit\n")
    ch=int(input("Enter your choice: "))
    print()
    if(ch==1):
        print("Here's your Model Performance Report: \n")
        print("Cross-Validated Scores:", detect.cross_val_scores)
        print(f"Model Accuracy: {detect.accuracy:.2f}")
        print("Classification Report:")
        print(detect.report)
        detect.check_overfitting(detect.clf,detect.X,detect.y,detect.X_valid,detect.y_valid,detect.kf)
        gr.draw()
    elif(ch==2):
        print("Enter the requirements-: ")
        user_quantity_in_grams = float(input("Enter the quantity in grams of the food item: "))
        user_ingredient_count = int(input("Enter the number of ingredients in the food item: "))
        user_food = input("Enter the food item: ")
        prediction_result = pred.predict_waste_category(user_quantity_in_grams, user_ingredient_count, user_food)
        print("\n",prediction_result)
    elif(ch==3):
        food_name = input("Enter the name of the food: ")
        nutrient_data = n.get_nutritional_info(food_name)

        if nutrient_data:
            # Create a Pandas DataFrame for the nutrient data
            df = pd.DataFrame(nutrient_data, index=[0])

            # Display the nutritional information
            print("\nNutritional Information for", food_name)
            print(df)

    elif(ch==4):
        print("Hope I could stand upto your expectations!\n \nHave a Good Day")
        break
    else:
        print("Invalid choice!")

