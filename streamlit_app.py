# Required Packages
import pandas as pd
import numpy as np
import random
import re
import fnmatch

# Streamlit Requirements
import streamlit
import requests
from urllib.error import URLError

streamlit.title('Farmer Joes Sandwich Randomizer')


streamlit.header('Sandwich Ingredients List')
# Ingredients List
temp = ['Hot','Cold']
temp_list = pd.DataFrame(temp, columns = ['Temperature'])

meat = ['Roast Turkey','Smoked Turkey','Grilled Chicken Breast','Roast Beef','Corned Beef','Pastrami','Black Forest Ham','Organic Smoked Tofu','Dry Salami','Tuna Salad','Chicken Salad','Prosciutto','Hot Coppa','Mild Coppa','Honey Ham']
meat_list = pd.DataFrame(meat, columns = ['Meats'])

greens = ['lettuce','tomato','red onions','pickles','pepperoncinis','mixed greens','arugula','sprouts','basil','jalapenos']
greens_list = pd.DataFrame(greens, columns = ['Veggies'])

spreads = ['mayonnaise','deli mustard','dijon mustard','aioli','chipotle mayo','mendocino mustard','basil pesto','hummus','cranberry sauce','sundried tomato pesto','balsamic vinagrette']
spreads_list = pd.DataFrame(spreads, columns = ['Spreads'])

bread = ['sliced wheat','sliced rye','sliced white','sliced sourdough','french roll (soft)','sourdough roll','wheat roll','rosemary focaccia','ciabatta','dutch crunch']
bread_list = pd.DataFrame(bread, columns = ['Breads'])

cheese = ['pepperjack','monterey jack','swiss','mozzarella','smoked gouda','havarti','meunster','provolone','american white cheese','american yellow cheese','cheddar','no cheese']
cheese_list = pd.DataFrame(cheese, columns = ['Cheeses'])

extra = ['double meat','double cheese','avocado','guacamole','bacon','olive oil & vinegar','roasted red peppers','goat cheese','cream cheese']
extra_list = pd.DataFrame(extra, columns = ['Extras'])

total_ingredients = pd.concat([temp_list, meat_list, greens_list, spreads_list, bread_list, cheese_list, extra_list], axis = 1)

separator = ","
all_ingredients = temp + meat + greens + spreads + bread + cheese + extra

# Streamlit Lists to =Show
streamlit.dataframe(total_ingredients)


# Dictionaries
everything = {'Hot':0,'Cold':0,'Roast Turkey':0,'Smoked Turkey':0,'Grilled Chicken Breast':0,'Roast Beef':0,'Corned Beef':0,'Pastrami':0,'Black Forest Ham':0,'Organic Smoked Tofu':0,'Dry Salami':0,'Tuna Salad':0,'Chicken Salad':0,'Prosciutto':1,'Hot Coppa':1,'Mild Coppa':1,'Honey Ham':0.75,'lettuce':0,'tomato':0,'red onions':0,'pickles':0,'pepperoncinis':0,'mixed greens':0,'arugula':0,'sprouts':0,'basil':0,'jalapenos':0,'mayonnaise':0,'deli mustard':0,'dijon mustard':0,'aioli':0,'chipotle mayo':0,'mendocino mustard':0,'basil pesto':0,'hummus':0,'cranberry sauce':0,'sundried tomato pesto':0,'balsamic vinagrette':0,'sliced wheat':0,'sliced rye':0,'sliced white':0,'sliced sourdough':0,'french roll (soft)':0,'sourdough roll':0,'wheat roll':0,'rosemary focaccia':0,'ciabatta':0,'dutch crunch':0,'pepperjack':0,'monterey jack':0,'swiss':0,'mozzarella':0,'smoked gouda':0,'havarti':0,'meunster':0,'provolone':0,'american white cheese':0,'american yellow cheese':0,'cheddar':0,'no cheese':0,'double meat':2,'double cheese':0.75,'avocado':0.75,'guacamole':0.75,'bacon':1,'olive oil & vinegar':0,'roasted red peppers':0.75,'goat cheese':0.75,'cream cheese':0.75,'':0}
everything2 = {'Hot':0,'Cold':0,'Roast Turkey':0,'Smoked Turkey':0,'Grilled Chicken Breast':0,'Roast Beef':0,'Corned Beef':0,'Pastrami':0,'Black Forest Ham':0,'Organic Smoked Tofu':0,'Dry Salami':0,'Tuna Salad':0,'Chicken Salad':0,'Prosciutto':1,'Hot Coppa':1,'Mild Coppa':1,'Honey Ham':0.75,'lettuce':0,'tomato':0,'red onions':0,'pickles':0,'pepperoncinis':0,'mixed greens':0,'arugula':0,'sprouts':0,'basil':0,'jalapenos':0,'mayonnaise':0,'deli mustard':0,'dijon mustard':0,'aioli':0,'chipotle mayo':0,'mendocino mustard':0,'basil pesto':0,'hummus':0,'cranberry sauce':0,'sundried tomato pesto':0,'balsamic vinagrette':0,'sliced wheat':0,'sliced rye':0,'sliced white':0,'sliced sourdough':0,'french roll (soft)':0,'sourdough roll':0,'wheat roll':0,'rosemary focaccia':0,'ciabatta':0,'dutch crunch':0,'pepperjack':0,'monterey jack':0,'swiss':0,'mozzarella':0,'smoked gouda':0,'havarti':0,'meunster':0,'provolone':0,'american white cheese':0,'american yellow cheese':0,'cheddar':0,'no cheese':0,'double meat':2,'double cheese':0.75,'avocado':0.75,'guacamole':0.75,'bacon':1,'olive oil & vinegar':0,'roasted red peppers':0.75,'goat cheese':0.75,'cream cheese':0.75,'':0}


# Required Function for sandwich_maker
def compute_price(ingredients):
    total = 7.99 # New price update
    total += sum([everything[s] for s in ingredients ])
    return total



# Final Version

def sandwich_maker(max_price,temperature,veggies,sauces,extras):
    # Max price is max amount you want to pay
    # Veggies (0-10), Sauces (0-12), Extras (0-8)
    #sandwich = str(random.choice(temp)) + " " + str(random.choice(meat))+ " Sandwich with " + str(separator.join(random.sample(greens,x)))+ ", " + str(separator.join(random.sample(spreads,y)))+ " on " + str(random.choice(bread)) + " with " + str(random.choice(cheese))+'.'+" Add " +str(separator.join(random.sample(extras,z)))+"."
    if veggies < 0: # Checks for negatives
        veggies = 0
        print("You can't have negative vegetables!")
    if veggies > 10: # Checks for values greater than total veggies possible
        veggies = 10
        print("There are only 10 total vegetables!")
    if sauces < 0:
        sauces = 0
        print("You can't have negative sauces!")
    if sauces > 11:
        sauces = 11
        print("There are only 11 total sauces!")
    if extras < 0:
        extras = 0
        print("You can't have negative extras!")
    if extras > 8:
        extras = 8 
        print("There are only 8 total extras!")
    if fnmatch.fnmatch(temperature.lower(), "*hot*"): #  if fnmatch.fnmatch(file, '*.txt'):
        rt = temp[0] # Changed to use temp list
    elif fnmatch.fnmatch(temperature.lower(), "*cold*"):
        rt = temp[1]
    else:
        rt = random.choice(temp)
        
    rm = random.choice(meat)
    rb = random.choice(bread)
    rc = random.choice(cheese)
    rv = separator.join(random.sample(greens,veggies))
    rs = separator.join(random.sample(spreads,sauces))
    ree = separator.join(random.sample(extra,extras))
    #sandwich2 = rt + "," + rm +","+ rb +","+ rc +','+ rv +"," + rs +","+ ree
    sandwich2 = f"{rt},{rm},{rb},{rc},{rv},{rs},{ree}"
    sandwich3 = sandwich2.split(",")
    cost = compute_price(sandwich3)
    if max_price < 7.99: # Updated price
        print("No sandwich is this cheap!")
    else:
        while cost > max_price:
                # rt = random.choice(temp)# Here is where temp issue arises     
                rm = random.choice(meat)
                rb = random.choice(bread)
                rc = random.choice(cheese)
                rv = separator.join(random.sample(greens,veggies))
                rs = separator.join(random.sample(spreads,sauces))
                ree = separator.join(random.sample(extra,extras))
                #sandwich2 = rt + "," + rm +","+ rb +","+ rc +','+ rv +"," + rs +","+ ree
                sandwich2 = f"{rt},{rm},{rb},{rc},{rv},{rs},{ree}"
                sandwich3 = sandwich2.split(",")
                cost = compute_price(sandwich3)
                extras = abs(extras-1)
                print("Extra or premium additions have been lowered by 1 or changed to accomodate price")
        if cost <= max_price:
            sandwich2 = f"{rt},{rm},{rb},{rc},{rv},{rs},{ree}"
            sandwich3 = sandwich2.split(",")
            cost = compute_price(sandwich3)
            if ree == "": # Basically if extras are all removed
                print(f"This Sandwich costs ${cost}") # Sick 
                sandwich = f"{rt} {rm} Sandwich on {rb},with {rc},{rv},{rs}."
                sandwich_remove_commas = sandwich.replace(",,",",")
                sandwich_final = sandwich_remove_commas.replace(",",", ")
                print(sandwich_final)
            else:
                print(f"This Sandwich costs ${cost}") # Sick 
                sandwich = f"{rt} {rm} Sandwich on {rb},with {rc},{rv},{rs}. Add {ree}."
                sandwich_remove_commas = sandwich.replace(",,",",")
                sandwich_final = sandwich_remove_commas.replace(",",", ")
                print(sandwich_final)
            #sandwich = rt + " " + rm + " Sandwich on " + rb + ", with " + rc + ", " + rv + " " + rs + ". Add " + ree + "."
            #sandwich = str(sandwich2[0])+ " " +str(sandwich2[1])+ " Sandwich on " + str(sandwich2[2]) + ", with " + str(sandwich2[3]) + " ," + str(sandwich2[4:4+veggies]) + " with " + str(sandwich2[4+veggies:4+veggies+sauces]) + ". Add " + str(sandwich2[4+veggies+sauces:4+veggies+sauces+extras])
    return

# Most recent changes: While -> if statements for performance

max_price_input = streamlit.number_input('Price Max', min_value = 0,)

sandwich_maker(14,"blank",4,3,4)