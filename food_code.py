

import pandas as pd
import webbrowser
import requests
import io
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Label
from PIL import Image, ImageTk
import tkinter as tk
import customtkinter as ctk
from IPython.display import display
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS2
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




dataset = pd.read_excel(resource_path("food_dataset.xlsx"))


# In[ ]:


display(pd.DataFrame(dataset))


# In[ ]:


def food_classifier(cuisine, course_type, flavor_type, time_of_day, diet):
    if (cuisine == "indian"):
        indian_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
              if (flavor_type == "sour") or (flavor_type == "mild"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
              if (flavor_type == "sweet") or (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "main course"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet) & (indian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                      if(flavor_type == "sweet") or (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour")or (flavor_type == "savory"):
                        filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet)  & (indian_dataset['Breakfast'] == 1) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet) & (indian_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour")or (flavor_type == "savory"):
                        filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet)  & (indian_dataset['Lunch'] == 1) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet) & (indian_dataset['Dinner'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                      if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour")or (flavor_type == "savory"):
                        filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet)  & (indian_dataset['Dinner'] == 1) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet) & (indian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour"):
                        filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet)  & (indian_dataset['Breakfast'] == 1) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet) & (indian_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour"):
                        filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet)  & (indian_dataset['Lunch'] == 1) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian"):
                    filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet) & (indian_dataset['Dinner'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour"):
                        filtered_dataset = indian_dataset[(indian_dataset['Course_Type'] == course_type) & (indian_dataset['Diet'] == diet)  & (indian_dataset['Dinner'] == 1) & (indian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
    elif (cuisine == "carribean"):
            carribean_dataset = dataset[(dataset['Cuisine'] == cuisine)]
            if(course_type == "dessert"):
                filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type)]
                recommend_dish(filtered_dataset)
            elif(course_type == "drink"):
                 if(flavor_type == "sour") or (flavor_type == "sweet"):
                    filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
            elif(course_type == "snack"):
                 if(diet == "vegetarian") or (diet =="non vegetarian"):
                    filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)]
                    recommend_dish(filtered_dataset)
            elif (course_type == "main course"):
                if(time_of_day == "breakfast"):
                    if(diet == "non vegetarian"):
                        filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet) & (carribean_dataset['Breakfast'] == 1)]
                        recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                         if(flavor_type == "sweet") or (flavor_type == "mild"):
                                filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Breakfast'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
                elif(time_of_day == "lunch"):
                        if(diet == "non vegetarian"):
                            if(flavor_type == "spicy") or (flavor_type == "mild"):
                                filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Lunch'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
                        elif(diet == "vegetarian"):
                             if(flavor_type == "mild") or (flavor_type == "sweet"):
                                    filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Lunch'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                                    recommend_dish(filtered_dataset)
                elif(time_of_day == "dinner"):
                    if(diet == "non vegetarian"):
                        if(flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Dinner'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                        if (flavor_type == "sweet") or (flavor_type == "mild"):
                            filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Dinner'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
            elif(course_type == "side dish"):
                if(time_of_day == "breakfast"):
                    if(flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sweet"):
                        filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type)  & (carribean_dataset['Breakfast'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(time_of_day == "lunch"):
                    if(diet == "non vegetarian") or (diet == "vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "mild"):
                            filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Lunch'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                elif(time_of_day == "dinner"):
                     if(diet == "non vegetarian") or (diet == "vegetarian"):
                        if(flavor_type == "spicy") or (flavor_type == "mild"):
                            filtered_dataset = carribean_dataset[(carribean_dataset['Course_Type'] == course_type) & (carribean_dataset['Diet'] == diet)  & (carribean_dataset['Lunch'] == 1) & (carribean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
    elif (cuisine == "brazilian"):
        brazilian_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if(course_type == "dessert") or (course_type == "drink"):
            filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
            if(diet == "vegetarian"):
                if(flavor_type == "sweet") or (flavor_type == "mild"):
                    filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet) & (brazilian_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
            elif(diet == "non vegetarian"):
                    filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)]
                    recommend_dish(filtered_dataset)
        elif(course_type == "main course"):
            if(time_of_day == "breakfast"):
                    if(diet == "non vegetarian") or (diet == "vegetarian"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet) & (brazilian_dataset['Breakfast'] == 1)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "savory") or (flavor_type == "mild"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1) & (brazilian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "savory") or (flavor_type == "mild"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1) & (brazilian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1)]
                        recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian") or (diet == "vegetarian"):
                    filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet) & (brazilian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1) & (brazilian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild"):
                        filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1) & (brazilian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    filtered_dataset = brazilian_dataset[(brazilian_dataset['Course_Type'] == course_type) & (brazilian_dataset['Diet'] == diet)  & (brazilian_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
    elif (cuisine == "peruvian"):
        peruvian_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
            if (flavor_type == "sour") or (flavor_type == "sweet"):
                filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                recommend_dish(filtered_dataset)
        elif (course_type == "main course"):
            if(time_of_day == "breakfast"):
                if(flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Flavor_Profile'] == flavor_type) & (peruvian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Flavor_Profile'] == flavor_type) & (peruvian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Flavor_Profile'] == flavor_type) & (peruvian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour"):
                        filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet)  & (peruvian_dataset['Dinner'] == 1) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
            if(time_of_day == "breakfast"):
                if(diet == "vegetarian"):
                    filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet) & (peruvian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "non vegetarian"):
                    if (flavor_type == "savory") or (flavor_type == "mild"):
                            filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet)  & (peruvian_dataset['Breakfast'] == 1) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "savory") or (flavor_type == "mild") or (flavor_type == "spicy"):
                        filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet) & (peruvian_dataset['Lunch'] == 1) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                        if (flavor_type == "savory") or (flavor_type == "mild"):
                            filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet)  & (peruvian_dataset['Lunch'] == 1) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "savory") or (flavor_type == "mild") or (flavor_type == "spicy"):
                        filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet) & (peruvian_dataset['Lunch'] == 1) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                      if (flavor_type == "savory") or (flavor_type == "mild"):
                        filtered_dataset = peruvian_dataset[(peruvian_dataset['Course_Type'] == course_type) & (peruvian_dataset['Diet'] == diet)  & (peruvian_dataset['Lunch'] == 1) & (peruvian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
    elif (cuisine == "french"):
        french_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            if (flavor_type == "sour") or (flavor_type == "sweet"):
                filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Flavor_Profile'] == flavor_type)]
                recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
                filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type)]
                recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
                if (flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "main course"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Diet'] == diet)  & (french_dataset['Breakfast'] == 1) & (french_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                        filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Diet'] == diet) & (french_dataset['Breakfast'] == 1)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian") or (diet == "vegetarian"):
                    if (flavor_type == "mild") or  (flavor_type == "savory"):
                        filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Diet'] == diet)  & (french_dataset['Lunch'] == 1) & (french_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian") or (diet == "vegetarian"):
                    if (flavor_type == "mild") or  (flavor_type == "savory"):
                        filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Diet'] == diet)  & (french_dataset['Dinner'] == 1) & (french_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
            if(time_of_day == "breakfast"):
                filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type)  & (french_dataset['Breakfast'] == 1)]
                recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Lunch'] == 1) & (french_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                   if(flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = french_dataset[(french_dataset['Course_Type'] == course_type) & (french_dataset['Dinner'] == 1) & (french_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
    elif (cuisine == "spanish"):
        spanish_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
            if (flavor_type == "sour") or (flavor_type == "mild") or (flavor_type == "sweet"):
                filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
            if(diet == "non vegetarian"):
                if  (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif (diet == "vegetarian"):
                    filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type)]
                    recommend_dish(filtered_dataset)
        elif(course_type == "main course"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "savory"):
                        filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Flavor_Profile'] == flavor_type) & (spanish_dataset['Breakfast'] == 1)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild"):
                        filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet)  & (spanish_dataset['Breakfast'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                    if(diet == "non vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "savory"):
                                filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type)  & (spanish_dataset['Lunch'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                            if (flavor_type == "spicy") or (flavor_type == "mild"):
                                filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet)& (spanish_dataset['Lunch'] == 1)  & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                    if(diet == "non vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "savory"):
                            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type)  & (spanish_dataset['Dinner'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "mild"):
                            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet)& (spanish_dataset['Dinner'] == 1)  & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
            if(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                        if (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet) & (spanish_dataset['Lunch'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet)  & (spanish_dataset['Lunch'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                    if(diet == "non vegetarian"):
                        if (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet) & (spanish_dataset['Dinner'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = spanish_dataset[(spanish_dataset['Course_Type'] == course_type) & (spanish_dataset['Diet'] == diet)  & (spanish_dataset['Dinner'] == 1) & (spanish_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
    elif(cuisine == "korean"):
        korean_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
            if (flavor_type == "sweet") or (flavor_type == "bitter"):
                filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Flavor_Profile'] == flavor_type)]
                recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
            if(diet == "non vegetarian"):
                filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Flavor_Profile'] == flavor_type) & (korean_dataset['Diet'] == diet)]
                recommend_dish(filtered_dataset)
            elif (diet == "vegetarian"):
                if (flavor_type == "sweet") or (flavor_type == "spicy"):
                    filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Flavor_Profile'] == flavor_type) & (korean_dataset['Diet'] == diet)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "main course"):
                if(time_of_day == "breakfast"):
                    if(diet == "non vegetarian") or (diet == "vegetarian"):
                        if(flavor_type == "spicy") or ((flavor_type == "savory")):
                            filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet)  & (korean_dataset['Breakfast'] == 1) & (korean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                elif(time_of_day == "lunch"):
                    if(diet == "non vegetarian") or (diet == "vegetarian"):
                        if(flavor_type == "spicy") or ((flavor_type == "savory")):
                            filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet)  & (korean_dataset['Breakfast'] == 1) & (korean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                elif(time_of_day == "dinner"):
                    if(diet == "non vegetarian") or (diet == "vegetarian"):
                        if(flavor_type == "spicy") or ((flavor_type == "savory")):
                            filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet)  & (korean_dataset['Breakfast'] == 1) & (korean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
                if(time_of_day == "lunch"):
                    if(diet == "non vegetarian"):
                        filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet) & (korean_dataset['Lunch'] == 1)]
                        recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "savory"):
                            filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet)  & (korean_dataset['Lunch'] == 1) & (korean_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                elif(time_of_day == "dinner"):
                    if(diet == "non vegetarian"):
                        filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet) & (korean_dataset['Lunch'] == 1)]
                        recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                          if (flavor_type == "spicy") or (flavor_type == "savory"):
                                filtered_dataset = korean_dataset[(korean_dataset['Course_Type'] == course_type) & (korean_dataset['Diet'] == diet)  & (korean_dataset['Lunch'] == 1) & (korean_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
    elif (cuisine == "chinese"):
            chinese_dataset = dataset[(dataset['Cuisine'] == cuisine)]
            if (course_type == "dessert"):
                filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type)]
                recommend_dish(filtered_dataset)
            elif (course_type == "drink"):
                  if(flavor_type == "sour" or flavor_type == "sweet"):
                        filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif (course_type == "snack"):
                if ( diet == "non vegetarian"):
                    filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)]
                    recommend_dish(filtered_dataset)
                elif (diet == "vegetarian"):
                    if (flavor_type == "sweet") or (flavor_type == "spicy") or (flavor_type == "mild"):
                        filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Flavor_Profile'] == flavor_type) & (chinese_dataset['Diet'] == diet)]
                        recommend_dish(filtered_dataset)
            elif (course_type == "main course"):
                    if(time_of_day == "breakfast"):
                        if(diet == "non vegetarian"):
                            if ( flavor_type == "spicy") or ( flavor_type == "savory"):
                                filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet) & (chinese_dataset['Breakfast'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
                        elif(diet == "vegetarian"):
                            if(flavor_type == "mild") or (flavor_type == "savory"):
                                filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)  & (chinese_dataset['Breakfast'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
                    elif(time_of_day == "lunch"):
                        if(diet == "non vegetarian"):
                            filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet) & (chinese_dataset['Lunch'] == 1)]
                            recommend_dish(filtered_dataset)
                        elif(diet == "vegetarian"):
                            if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "sour")or (flavor_type == "savory"):
                                filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)  & (chinese_dataset['Lunch'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
                    elif(time_of_day == "dinner"):
                        if(diet == "vegetarian"):
                            filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet) & (chinese_dataset['Dinner'] == 1)]
                            recommend_dish(filtered_dataset)
                        elif(diet == "non vegetarian"):
                            if (flavor_type == "spicy") or (flavor_type == "savory"):
                                filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)  & (chinese_dataset['Dinner'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
            elif (course_type == "side dish"):
                    if(time_of_day == "breakfast"):
                        if (flavor_type == "spicy") or (flavor_type == "savory"):
                            filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)  & (chinese_dataset['Breakfast'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(time_of_day == "lunch"):
                        if(diet == "non vegetarian"):
                            filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet) & (chinese_dataset['Lunch'] == 1)]
                            recommend_dish(filtered_dataset)
                        elif(diet == "vegetarian"):
                                if(flavor_type == "spicy") or (flavor_type == "savory"):
                                    filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)  & (chinese_dataset['Lunch'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                                    recommend_dish(filtered_dataset)
                    elif(time_of_day == "dinner"):
                            if(diet == "non vegetarian"):
                                filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet) & (chinese_dataset['Dinner'] == 1)]
                                recommend_dish(filtered_dataset)
                            elif(diet == "vegetarian"):
                                if (flavor_type == "spicy") or (flavor_type == "savory"):
                                    filtered_dataset = chinese_dataset[(chinese_dataset['Course_Type'] == course_type) & (chinese_dataset['Diet'] == diet)  & (chinese_dataset['Dinner'] == 1) & (chinese_dataset['Flavor_Profile'] == flavor_type)]
                                    recommend_dish(filtered_dataset)
    elif (cuisine == "japanese"):
        japanese_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
                if (flavor_type == "sweet") or (flavor_type == "mild") or (flavor_type == "spicy"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
                if(diet == "non vegetarian"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                      if (flavor_type == "sweet") or (flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
        elif (course_type == "main course"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet) & (japanese_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if(flavor_type == "sweet") or (flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Breakfast'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "non vegetarian"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet) & (japanese_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                    if (flavor_type == "mild") or  (flavor_type == "savory"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Lunch'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "non vegetarian"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet) & (japanese_dataset['Dinner'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                        if (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Dinner'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
        elif(course_type == "side dish"):
            if(time_of_day == "breakfast"):
                if(diet == "non vegetarian"):
                    if (flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Breakfast'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
                elif(diet == "vegetarian"):
                     if (flavor_type == "savory")  or (flavor_type == "sweet"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Breakfast'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                if(diet == "vegetarian"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet) & (japanese_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "non vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Lunch'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                if(diet == "vegetarian"):
                    filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet) & (japanese_dataset['Lunch'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "non vegetarian"):
                    if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                        filtered_dataset = japanese_dataset[(japanese_dataset['Course_Type'] == course_type) & (japanese_dataset['Diet'] == diet)  & (japanese_dataset['Lunch'] == 1) & (japanese_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)
    elif (cuisine == "italian"):
        italian_dataset = dataset[(dataset['Cuisine'] == cuisine)]
        if (course_type == "dessert"):
            filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type)]
            recommend_dish(filtered_dataset)
        elif (course_type == "drink"):
              if (flavor_type == "sour") or (flavor_type == "mild"):
                    filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "snack"):
              if (flavor_type == "sweet") or (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                    filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
        elif (course_type == "main course"):
            if(time_of_day == "breakfast"):
                if(diet == "vegetarian"):
                    filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet) & (italian_dataset['Breakfast'] == 1)]
                    recommend_dish(filtered_dataset)
                elif(diet == "non vegetarian"):
                        if(flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Breakfast'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
            elif(time_of_day == "lunch"):
                    if(diet == "non vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Lunch'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                        if (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Lunch'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                    if(diet == "non vegetarian"):
                        if (flavor_type == "spicy") or (flavor_type == "mild") or (flavor_type == "savory"):
                            filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Lunch'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                            recommend_dish(filtered_dataset)
                    elif(diet == "vegetarian"):
                          if (flavor_type == "mild") or (flavor_type == "savory"):
                                filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Lunch'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                                recommend_dish(filtered_dataset)
        elif (course_type == "side dish"):
            if(time_of_day == "lunch"):
                if (flavor_type == "savory") or (flavor_type == "sour"):
                    filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Lunch'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                    recommend_dish(filtered_dataset)
            elif(time_of_day == "dinner"):
                  if (flavor_type == "savory") or (flavor_type == "sour"):
                        filtered_dataset = italian_dataset[(italian_dataset['Course_Type'] == course_type) & (italian_dataset['Diet'] == diet)  & (italian_dataset['Lunch'] == 1) & (italian_dataset['Flavor_Profile'] == flavor_type)]
                        recommend_dish(filtered_dataset)


# In[ ]:


def recommend_dish(filtered_dataset):
    recommended_dish = filtered_dataset.sample(n=1).iloc[0]
    dish_name = recommended_dish['Name']
    nutritious = recommended_dish['Nutritional_Info']
    image_url = recommended_dish['Image_URL']
    recipe_url = recommended_dish['Recipe_URL']
    display_dish(dish_name, nutritious, image_url, recipe_url)
    open_link(recipe_url)


# In[ ]:


def update_dropdowns(event):
    selected_cuisine = cuisine_dropdown.get()
    selected_coursetype = coursetype_dropdown.get()
    selected_flavor = flavor_dropdown.get()
    selected_diet = diet_dropdown.get()
    selected_time = time_dropdown.get()
    
    if selected_cuisine == "Indian" or selected_cuisine == "Italian" or selected_cuisine == "Spanish" or selected_cuisine == "Korean" or selected_cuisine == "French" or selected_cuisine == "Carribean" or selected_cuisine == "Chinese" or selected_cuisine == "Brazilian" or selected_cuisine == "Japanese":
        coursetype_dropdown['values'] = ["Dessert", "Snack", "Drink", "Main Course", "Side Dish"]
    elif selected_cuisine == "Peruvian":
            coursetype_dropdown['values'] = ["Dessert", "Drink", "Main Course", "Side Dish"]
    if selected_cuisine != "French" and selected_coursetype == "Dessert":
        flavor_dropdown['values'] = ["Sweet"]
        diet_dropdown['values'] = ["Vegetarian"]
        time_dropdown['values'] = ["N/A"]
    
    #Indian cuisine
    if selected_cuisine == "Indian" and selected_coursetype == "Snack":
            flavor_dropdown['values'] = ["Sweet", "Savory", "Spicy", "Mild"]
            diet_dropdown['values'] = ["Vegetarian"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Indian" and selected_coursetype == "Drink":
            flavor_dropdown['values'] = ["Sour", "Mild"]
            diet_dropdown['values'] = ["N/A"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Indian" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet =="Vegetarian" and selected_time == "N/A":
        buttonwow()
    if selected_cuisine == "Indian" and selected_coursetype == "Snack" and (selected_flavor == "Sweet" or selected_flavor == "Savory" or selected_flavor == "Spicy" or selected_flavor == "Mild") and selected_diet =="Vegetarian":
            buttonwow()
    if selected_cuisine == "Indian" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish"):
        time_dropdown['values'] = ["Breakfast", "Lunch","Dinner"]
    if selected_cuisine == "Indian" and (selected_coursetype == "Main Course" and selected_time == "Breakfast"):
        flavor_dropdown['values'] = ["Sweet", "Spicy", "Mild","Sour"]
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and (selected_time == "Lunch" or selected_time == "Dinner"):
            flavor_dropdown['values'] = ["Sour", "Spicy", "Mild"]
    if selected_cuisine == "Indian" and selected_coursetype == "Side Dish" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner"):
            flavor_dropdown['values'] = ["Sour", "Spicy", "Mild"]
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and selected_time == "Breakfast" and (selected_flavor == "Sweet" or selected_flavor == "Mild" or selected_flavor == "Sour"):
        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and (selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Sour" or selected_flavor == "Mild"):
            diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and selected_time == "Breakfast" and (selected_flavor == "Sweet" or selected_flavor == "Mild" or selected_flavor == "Sour") and selected_diet =="Vegetarian":
        buttonwow()
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and (selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Sour" or selected_flavor == "Mild") and selected_diet =="Vegetarian":
            buttonwow()
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy":
        diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Indian" and selected_coursetype == "Main Course" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy" and (selected_diet == "Vegetarian" or selected_diet == "Non Vegetarian"):
        buttonwow()
    if selected_cuisine == "Indian" and selected_coursetype == "Side Dish" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Mild" or selected_flavor == "Sour"):
        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Indian" and selected_coursetype == "Side Dish" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy":
            diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Indian" and selected_coursetype == "Side Dish" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Mild" or selected_flavor == "Sour") and selected_diet =="Vegetarian":
        buttonwow()
    if selected_cuisine == "Indian" and selected_coursetype == "Side Dish" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Spicy") and (selected_diet =="Vegetarian" or selected_diet =="Non Vegetarian"):
        buttonwow()
    if selected_cuisine == "Indian" and selected_coursetype == "Drink" and (selected_flavor =="Sour" or selected_flavor == "Mild") and selected_diet == "N/A" and selected_time=="N/A":
        buttonwow()

    #carribean cuisine
    if selected_cuisine == "Carribean" and selected_coursetype == "Snack":
            flavor_dropdown['values'] = ["Spicy", "Mild"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Drink":
            flavor_dropdown['values'] = ["Sour", "Sweet"]
            diet_dropdown['values'] = ["N/A"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Snack" and selected_flavor == "Spicy":
        diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Snack" and selected_flavor == "Mild":
        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet =="Vegetarian" and selected_time == "N/A":
        buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Snack" and selected_flavor == "Spicy" and selected_diet =="Non Vegetarian" and selected_time == "N/A":
          buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Snack" and selected_flavor == "Mild" and selected_diet == "Vegetarian" and selected_time == "N/A":
          buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Drink" and (selected_flavor == "Sour" or selected_flavor == "Sweet") and selected_diet =="N/A" and selected_time == "N/A":
          buttonwow()
    if selected_cuisine == "Carribean" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish"):
        time_dropdown['values'] = ["Breakfast", "Lunch","Dinner"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and selected_time == "Breakfast":
        flavor_dropdown['values'] = ["Sweet","Mild"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and selected_time == "Lunch":
            flavor_dropdown['values'] = ["Sweet", "Spicy", "Mild"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and selected_time == "Dinner":
            flavor_dropdown['values'] = ["Savory", "Spicy", "Mild", "Sweet"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and selected_time == "Breakfast":
            flavor_dropdown['values'] = ["Sweet", "Spicy", "Mild"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and (selected_time == "Lunch" or selected_time == "Dinner"):
            flavor_dropdown['values'] = ["Spicy", "Mild"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Sweet":
        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course"  and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Mild":
        diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"] 
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and (selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy":
            diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and selected_time == "Dinner" and selected_flavor == "Savory":
            diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Sweet" or selected_flavor == "Mild" ) and selected_diet =="Vegetarian":
        buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Mild" and selected_diet =="Non Vegetarian":
            buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and (selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy" and selected_diet == "Non Vegetarian":
        buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Main Course" and  selected_time == "Dinner" and selected_flavor == "Savory" and selected_diet == "Non Vegetarian":
        buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and selected_time != "Breakfast":
        flavor_dropdown['values'] = ["Spicy","Mild"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and selected_time == "Breakfast":
        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and selected_time == "Breakfast" and (selected_flavor == "Sweet" or selected_flavor == "Spicy" or selected_flavor == "Mild" )and selected_diet == "Vegetarian":
        buttonwow()
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and (selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Spicy" or selected_flavor == "Mild"):
         diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Carribean" and selected_coursetype == "Side Dish" and (selected_time == "Lunch" or selected_time == "Dinner") and (selected_flavor == "Spicy" or selected_flavor == "Mild") and (selected_diet == "Vegetarian" or selected_diet == "Non Vegetarian"):
        buttonwow()  
  
    #brazilian cuisine
    if selected_cuisine == "Brazilian" and selected_coursetype == "Snack":
            flavor_dropdown['values'] = ["Sweet", "Mild"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Brazilian" and selected_coursetype == "Drink":
            flavor_dropdown['values'] = ["Sour"]
            diet_dropdown['values'] = ["N/A"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Brazilian" and selected_coursetype == "Snack" and selected_flavor == "Mild":
        diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Brazilian" and selected_coursetype == "Snack" and selected_flavor == "Sweet":
        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Brazilian" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet =="Vegetarian" and selected_time == "N/A":
        buttonwow()
    if selected_cuisine == "Brazilian" and selected_coursetype == "Snack" and (selected_flavor == "Sweet" or selected_flavor == "Mild") and selected_diet =="Vegetarian" and selected_time == "N/A":
          buttonwow()
    if selected_cuisine == "Brazilian" and selected_coursetype == "Snack" and selected_flavor == "Mild" and selected_diet =="Non Vegetarian" and selected_time == "N/A":
          buttonwow()
    if selected_cuisine == "Brazilian" and selected_coursetype == "Drink" and selected_flavor == "Sour" and selected_diet =="N/A" and selected_time == "N/A":
          buttonwow()
    if selected_cuisine == "Brazilian" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish"):
        time_dropdown['values'] = ["Breakfast", "Lunch","Dinner"]
    if selected_cuisine == "Brazilian" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish") and selected_time == "Breakfast":
        flavor_dropdown['values'] = ["Mild"]
    if selected_cuisine == "Brazilian" and selected_coursetype == "Main Course" and (selected_time == "Lunch" or selected_time == "Dinner"):
            flavor_dropdown['values'] = ["Savory", "Mild"]
    if selected_cuisine == "Brazilian" and selected_coursetype == "Side Dish" and (selected_time == "Lunch" or selected_time == "Dinner"):
            flavor_dropdown['values'] = ["Spicy", "Mild"]
    if selected_cuisine == "Brazilian" and (selected_flavor == "Spicy" or selected_flavor == "Savory"):
            diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Brazilian" and selected_flavor == "Mild":
        diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Brazilian" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish") and (selected_time=="Breakfast" or selected_time=="Lunch" or selected_time=="Dinner") and selected_flavor=="Mild" and (selected_diet=="Vegetarian" or selected_diet == "Non Vegetarian"):
        buttonwow()
    if selected_cuisine == "Brazilian" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish") and (selected_flavor == "Spicy" or selected_flavor == "Savory") and (selected_time == "Lunch" or selected_time == "Dinner") and selected_diet == "Non Vegetarian":
        buttonwow()
    
    #peruvian cuisine
    if selected_cuisine == "Peruvian" and selected_coursetype == "Drink":
                flavor_dropdown['values'] = ["Sour", "Sweet"]
                diet_dropdown['values'] = ["N/A"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Peruvian" and (selected_coursetype == "Drink" or selected_coursetype == "Dessert") and (selected_flavor == "Sweet" or selected_flavor == "Sour") and (selected_diet == "Vegetarian" or selected_diet == "N/A") and selected_time== "N/A":
            buttonwow()
    if selected_cuisine == "Peruvian" and (selected_coursetype == "Main Course" or selected_coursetype == "Side Dish"):
            time_dropdown['values'] = ["Breakfast", "Lunch", "Dinner"]
    if selected_cuisine == "Peruvian"  and selected_coursetype == "Main Course":
            diet_dropdown['values'] = ["Non Vegetarian"]
            flavor_dropdown['values']= ["Mild", "Spicy", "Savory"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Main Course" and (selected_flavor == "Mild" or selected_flavor == "Spicy" or selected_flavor == "Savory") and selected_diet == "Non Vegetarian" and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner"):
                buttonwow()
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and selected_time =="Breakfast":
                flavor_dropdown['values'] = ["Savory", "Mild"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and selected_time !="Breakfast":
                flavor_dropdown['values'] = ["Savory", "Mild","Spicy"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and selected_time == "Breakfast" and selected_flavor == "Mild":
                    diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and selected_time == "Breakfast" and selected_flavor != "Mild":
                    diet_dropdown['values'] = ["Vegetarian","Non Vegetarian"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and (selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor != "Spicy":
                        diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and (selected_time == "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy":
                        diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Peruvian" and selected_coursetype == "Side Dish" and (selected_flavor == "Mild" or selected_flavor == "Spicy" or selected_flavor == "Savory") and (selected_diet == "Non Vegetarian" or selected_diet == "Vegetarian") and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner"):
                buttonwow()
    
    #italian cuisine
    if selected_cuisine == "Italian" and (selected_flavor == "Sour" or selected_flavor == "Spicy") :
                    diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Italian" and selected_coursetype == "Drink":
                flavor_dropdown['values'] = ["Sour", "Mild"]
                diet_dropdown['values'] = ["N/A"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Italian" and selected_coursetype == "Snack":
                flavor_dropdown['values'] = ["Sweet","Spicy", "Savory", "Mild"]
                diet_dropdown['values'] = ["Vegetarian"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Italian" and selected_coursetype == "Drink" and (selected_flavor == "Sour" or selected_flavor == "Mild") and selected_time=="N/A" and selected_diet == "N/A":
            buttonwow()
    if selected_cuisine == "Italian" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet == "Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Italian" and selected_coursetype == "Snack" and (selected_flavor == "Sweet" or selected_flavor == "Spicy" or selected_flavor == "Savory" or selected_flavor == "Mild") and selected_diet == "Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course":
            time_dropdown['values'] = ["Breakfast", "Lunch", "Dinner"]
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and selected_time == "Breakfast":
                flavor_dropdown['values'] = ["Savory", "Mild"]
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and selected_flavor == "Savory":
                    diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and selected_flavor == "Savory":
                    diet_dropdown['values'] = ["Vegetarian","Non Vegetarian"]
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and selected_time != "Breakfast":
                flavor_dropdown['values'] = ["Savory","Mild", "Spicy"]
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and (selected_time ==  "Lunch" or selected_time == "Dinner") and (selected_flavor == "Savory" or selected_flavor == "Mild"):
                        diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and (selected_time ==  "Lunch" or selected_time == "Dinner") and selected_flavor == "Spicy":
                        diet_dropdown['values'] = ['Non Vegetarian']
    if selected_cuisine == "Italian" and selected_coursetype == "Main Course" and (selected_flavor == "Spicy" or selected_flavor == "Mild" or selected_flavor == "Savory") and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and (selected_diet == "Non Vegetarian" or selected_diet == "Vegetarian"):
                buttonwow()
    if selected_cuisine == "Italian" and selected_coursetype == "Side Dish":
            time_dropdown['values'] = ["Lunch", "Dinner"]
            flavor_dropdown['values'] = ["Savory","Sour"]
            diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Italian" and selected_coursetype == "Side Dish" and (selected_flavor == "Savory" or selected_flavor == "Sour") and (selected_time == "Lunch" or selected_time == "Dinner") and selected_diet == "Non Vegetarian":
                buttonwow()
    
    #french cuisine
    if selected_cuisine == "French" and selected_coursetype == "Dessert":
            flavor_dropdown['values'] = ["Sour", "Sweet"]
            diet_dropdown['values'] = ["Vegetarian"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "French" and selected_coursetype == "Drink":
                flavor_dropdown['values'] = ["Sweet"]
                diet_dropdown['values'] = ["N/A"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "French" and selected_coursetype == "Snack":
                flavor_dropdown['values'] = ["Savory", "Mild"]
                diet_dropdown['values'] = ["Non Vegetarian"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "French" and selected_coursetype == "Drink" and selected_flavor == "Sweet" and selected_time=="N/A" and selected_diet == "N/A":
            buttonwow()
    if selected_cuisine == "French" and selected_coursetype == "Dessert" and (selected_flavor == "Sweet" or selected_flavor == "Sour") and selected_diet == "Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "French" and  selected_coursetype == "Snack" and (selected_flavor == "Savory" or selected_flavor == "Mild") and selected_diet == "Non Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "French" and selected_coursetype == "Side Dish":
            diet_dropdown['values']= ["Vegetarian"]
            time_dropdown['values'] = ["Breakfast", "Lunch", "Dinner"]
    if selected_cuisine == "French" and selected_coursetype == "Side Dish" and selected_diet == "Breakfast":
                flavor_dropdown['values']= ["Mild"]
    if selected_cuisine == "French" and selected_coursetype == "Side Dish" and selected_diet != "Breakfast":
                flavor_dropdown['values']= ["Mild","Savory"]
    if selected_cuisine == "French" and selected_coursetype == "Side Dish" and (selected_flavor=="Mild" or selected_flavor == "Savory") and (selected_time == "Breakfast" or selected_time == "Lunch" or selected_time == "Dinner") and selected_diet == "Vegetarian":
                buttonwow()
    if selected_cuisine == "French" and selected_coursetype == "Main Course":
            time_dropdown['values'] = ["Breakfast", "Lunch", "Dinner"]
            flavor_dropdown['values'] = ["Mild", "Savory"]
            diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "French" and selected_coursetype == "Main Course" and selected_flavor == "Mild":
                diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "French" and selected_coursetype == "Main Course" and (selected_flavor in ["Mild", "Savory"]) and (selected_time in ["Breakfast", "Lunch", "Dinner"]) and (selected_diet in ["Vegetarian", "Non Vegetarian"]):
                buttonwow()
    
    
    
    #spanish cuisine
    if selected_cuisine == "Spanish" and selected_coursetype == "Drink":
                flavor_dropdown['values'] = ["Mild", "Sour","Sweet"]
                diet_dropdown['values'] = ["N/A"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Snack":
        flavor_dropdown['values'] = ["Savory", "Mild", "Spicy", "Sweet"]
        time_dropdown['values'] = ["N/A"] 
    if selected_cuisine == "Spanish" and selected_coursetype == "Drink" and (selected_flavor in ["Sweet", "Sour", "Mild"]) and selected_time=="N/A" and selected_diet == "N/A":
            buttonwow()
    if selected_cuisine == "Spanish" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet == "Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Spanish" and selected_coursetype == "Snack" and (selected_flavor in ["Spicy", "Mild"]):
                diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Snack" and (selected_flavor == "Savory"):
                diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Snack" and (selected_flavor == "Sweet"):
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Snack" and (selected_flavor in ["Savory", "Sweet", "Spicy", "Mild"]) and (selected_diet in ["Vegetarian" , "Non Vegetarian"]) and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Spanish" and selected_coursetype in ["Main Course", "Side Dish"]:
            flavor_dropdown['values'] = ["Savory", "Spicy", "Mild"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Side Dish":
            time_dropdown['values'] = ["Lunch","Dinner"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Side Dish" and selected_flavor in ["Savory", "Mild"]:
                diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Side Dish" and selected_flavor== "Spicy":
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype in "Main Course":
            time_dropdown['values'] = ["Breakfast","Lunch","Dinner"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Side Dish" and (selected_flavor in ["Savory", "Spicy", "Mild"]) and (selected_time in ["Lunch","Dinner"]) and (selected_diet in ["Non Vegetarian", "Vegetarian"]):
            buttonwow()
    if selected_cuisine == "Spanish" and selected_coursetype == "Main Course" and selected_flavor == "Savory":
                diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Main Course" and selected_flavor == "Spicy":
                diet_dropdown['values'] = ["Non Vegetarian","Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Main Course" and selected_flavor == "Mild":
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Spanish" and selected_coursetype == "Main Course" and (selected_flavor in ["Savory", "Spicy", "Mild"]) and (selected_time in ["Breakfast","Lunch","Dinner"]) and (selected_diet in ["Non Vegetarian", "Vegetarian"]):
                buttonwow()
    
    
    #korean cuisine
    if selected_cuisine == "Korean" and selected_coursetype == "Drink":
                flavor_dropdown['values'] = ["Bitter","Sweet"]
                diet_dropdown['values'] = ["N/A"]
                time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Korean" and selected_coursetype == "Snack":
                flavor_dropdown['values'] = ["Spicy", "Sweet"]
                time_dropdown['values'] = ["N/A"] 
    if selected_cuisine == "Korean" and selected_coursetype == "Drink" and (selected_flavor in ["Sweet", "Bitter"]) and selected_time=="N/A" and selected_diet == "N/A":
            buttonwow()
    if selected_cuisine == "Korean" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet == "Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Korean" and selected_coursetype == "Snack" and (selected_flavor == "Spicy"):
                diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Korean" and selected_coursetype == "Snack" and (selected_flavor == "Sweet"):
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Korean" and selected_coursetype == "Snack" and (selected_flavor in ["Sweet", "Spicy"]) and (selected_diet in ["Vegetarian" , "Non Vegetarian"]) and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Korean" and selected_coursetype in ["Main Course", "Side Dish"]:
            flavor_dropdown['values'] = ["Savory", "Spicy"]
    if selected_cuisine == "Korean" and selected_coursetype == "Side Dish":
            time_dropdown['values'] = ["Lunch","Dinner"]
    if selected_cuisine == "Korean" and selected_coursetype == "Side Dish" and selected_flavor == "Spicy":
                diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Korean" and selected_coursetype == "Side Dish" and selected_flavor == "Savory":
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Korean" and selected_coursetype == "Main Course":
            time_dropdown['values'] = ["Breakfast","Lunch","Dinner"]
    if selected_cuisine == "Korean" and selected_coursetype == "Side Dish" and (selected_flavor in ["Savory", "Spicy"]) and (selected_time in ["Lunch","Dinner"]) and (selected_diet in ["Non Vegetarian", "Vegetarian"]):
            buttonwow()
    if selected_cuisine == "Korean" and selected_coursetype == "Main Course" and selected_time == "Breakfast" and selected_flavor == "Savory": 
                    diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Korean" and selected_coursetype == "Main Course" and (selected_time in ["Lunch","Dinner"]) and selected_flavor == "Savory": 
                    diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]        
    if selected_cuisine == "Korean" and selected_coursetype == "Main Course" and (selected_time in ["Breakfast","Lunch","Dinner"]) and selected_flavor == "Spicy":
                diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Korean" and selected_coursetype == "Main Course" and  (selected_flavor in ["Savory", "Spicy"]) and (selected_time in ["Breakfast","Lunch","Dinner"]) and (selected_diet in ["Non Vegetarian", "Vegetarian"]):
                buttonwow()
    
    #chinese cuisine
    if selected_cuisine == "Chinese" and selected_coursetype == "Drink":
            flavor_dropdown['values'] = ["Sour","Sweet"]
            diet_dropdown['values'] = ["N/A"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Chinese" and selected_coursetype == "Snack":
                flavor_dropdown['values'] = ["Spicy", "Sweet", "Mild"]
                time_dropdown['values'] = ["N/A"] 
    if selected_cuisine == "Chinese" and selected_coursetype == "Drink" and (selected_flavor in ["Sweet", "Sour"]) and selected_time == "N/A" and selected_diet == "N/A":
            buttonwow()
    if selected_cuisine == "Chinese" and  selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet == "Vegetarian" and selected_time == "N/A":
            buttonwow()
    if selected_cuisine == "Chinese" and  selected_coursetype == "Snack" and (selected_flavor == "Spicy"):
                diet_dropdown['values'] = ["Non Vegetarian", "Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype == "Snack" and (selected_flavor in ["Sweet", "Mild"]):
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype == "Snack" and (selected_flavor in ["Sweet", "Spicy", "Mild"]) and (selected_diet in ["Vegetarian" , "Non Vegetarian"]) and selected_time == "N/A":
            buttonwow() 
    if selected_cuisine == "Chinese" and selected_coursetype =="Side Dish":
            flavor_dropdown['values'] = ["Savory", "Spicy"]
            time_dropdown['values'] = ["Breakfast","Lunch","Dinner"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Side Dish" and selected_time == "Breakfast":
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Side Dish" and selected_time != "Breakfast" and selected_flavor == "Spicy":
                    diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Side Dish" and selected_time != "Breakfast" and selected_flavor != "Spicy":
                     diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Side Dish" and (selected_flavor in ["Savory", "Spicy"]) and selected_diet in ["Vegetarian", "Non Vegetarian"] and selected_time in ["Breakfast","Lunch","Dinner"]:
                buttonwow()
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course":
            time_dropdown['values'] = ["Breakfast","Lunch","Dinner"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course" and selected_time != "Breakfast":
                flavor_dropdown['values'] = ["Savory", "Spicy"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course" and selected_time == "Breakfast":
                flavor_dropdown['values'] = ["Savory", "Spicy", "Mild"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course" and selected_flavor == "Savory":
                diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course" and selected_flavor == "Spicy":
                diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course" and selected_flavor == "Mild":
                diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Chinese" and selected_coursetype =="Main Course" and(selected_flavor in ["Savory", "Spicy", "Mild"]) and (selected_diet in ["Vegetarian", "Non Vegetarian"]) and (selected_time in ["Breakfast","Lunch","Dinner"]):
                buttonwow()
        
    #japanese cuisine
    if selected_cuisine == "Japanese" and selected_coursetype == "Drink":
            flavor_dropdown['values'] = ["Mild","Sweet", "Spicy"]
            diet_dropdown['values'] = ["N/A"]
            time_dropdown['values'] = ["N/A"]
    if selected_cuisine == "Japanese" and selected_coursetype == "Snack":
                    flavor_dropdown['values'] = [ "Sweet", "Mild", "Savory"]
                    time_dropdown['values'] = ["N/A"] 
    if selected_cuisine == "Japanese" and selected_coursetype == "Drink" and (selected_flavor in ["Mild", "Sweet", "Spicy"]) and selected_time == "N/A" and selected_diet == "N/A":
                buttonwow()
    if selected_cuisine == "Japanese" and selected_coursetype == "Dessert" and selected_flavor == "Sweet" and selected_diet == "Vegetarian" and selected_time == "N/A":
                buttonwow()
    if selected_cuisine == "Japanese" and selected_coursetype == "Snack" and (selected_flavor in ["Sweet", "Mild"]):
                    diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype == "Snack" and selected_flavor == "Savory":
                    diet_dropdown['values'] = ["Non Vegetarian","Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype == "Snack" and (selected_flavor in ["Sweet", "Savory", "Mild"]) and (selected_diet in ["Vegetarian" , "Non Vegetarian"]) and selected_time == "N/A":
                buttonwow() 
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish":
                time_dropdown['values'] = ["Breakfast","Lunch","Dinner"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and selected_time == "Breakfast":
                    flavor_dropdown['values'] = [ "Sweet", "Mild", "Savory"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and selected_time == "Breakfast" and selected_flavor == "Sweet":
                        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and  selected_flavor == "Mild":
                        diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and selected_time == "Breakfast" and  selected_flavor == "Savory":
                        diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and selected_time != "Breakfast":
                    flavor_dropdown['values'] = [ "Spicy", "Mild", "Savory"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and selected_time != "Breakfast" and selected_flavor == "Savory": 
                            diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and selected_time != "Breakfast" and selected_flavor == "Spicy":
                             diet_dropdown['values'] = ["Non Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Side Dish" and (selected_flavor in ["Savory", "Spicy" , "Mild", "Sweet"]) and selected_diet in ["Vegetarian", "Non Vegetarian"] and (selected_time in ["Breakfast","Lunch","Dinner"]):
                    buttonwow()
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course":
                time_dropdown['values'] = ["Breakfast","Lunch","Dinner"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and selected_time == "Breakfast":
                    flavor_dropdown['values'] = [ "Sweet", "Mild", "Savory"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and (selected_flavor in ["Sweet", "Mild"]):
                        diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and selected_flavor == "Savory":
                        diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and selected_time != "Breakfast":
                    flavor_dropdown['values'] = ["Mild", "Savory"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and selected_time != "Breakfast" and selected_flavor == "Savory": 
                            diet_dropdown['values'] = ["Vegetarian", "Non Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and selected_time != "Breakfast" and selected_flavor == "Mild":
                         diet_dropdown['values'] = ["Vegetarian"]
    if selected_cuisine == "Japanese" and selected_coursetype =="Main Course" and (selected_flavor in ["Savory", "Mild", "Sweet"]) and (selected_diet in ["Vegetarian", "Non Vegetarian"]) and (selected_time in ["Breakfast","Lunch","Dinner"]):
                    buttonwow()


# In[ ]:


def recommend_food():
    cuisine = cuisine_var.get()
    cuisine = cuisine.lower()
    course_type = coursetype_var.get()
    course_type = course_type.lower()
    flavor_type = flavor_var.get()
    flavor_type = flavor_type.lower()
    time_of_day = time_var.get()
    time_of_day = time_of_day.lower()
    diet = diet_var.get()
    diet = diet.lower()
    if 'dish_label' in globals():
        dish_label.pack_forget()
    if 'nutritious_label' in globals():
        nutritious_label.pack_forget()
    if 'label' in globals():
        label.pack_forget()
    if 'link_label' in globals():
        link_label.pack_forget()
    food_classifier(cuisine, course_type, flavor_type, time_of_day, diet)


# In[ ]:


root = ctk.CTk()
root.title("Food Recommendation System")
root.iconbitmap(resource_path("pizzaicon.ico"))
root.geometry("1000x700")
root.pack_propagate(False)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


global recommends
recommends = False

def reset_inputs():
    global recommends
    cuisine_var.set('')
    coursetype_var.set('')
    time_var.set('')
    flavor_var.set('')
    diet_var.set('')
    if 'dish_label' in globals():
        dish_label.pack_forget()
    if 'nutritious_label' in globals():
        nutritious_label.pack_forget()
    if 'label' in globals():
        label.pack_forget()
    if 'link_label' in globals():
        link_label.pack_forget()
    if recommends == True:
        recommend_button.pack_forget()
        recommends = False

larger_font = ('Arial', 14)

reset_button = ctk.CTkButton(root, text="RESET", command=reset_inputs)
reset_button.pack(anchor='nw')
reset_button.place(x=50, y=50)

# Create labels for dropdown menus
cuisine_label = ctk.CTkLabel(root, text="Cuisine:", text_color = "black", fg_color="transparent", font = larger_font)
cuisine_label.pack()
cuisine_var = tk.StringVar()
cuisine_dropdown = ttk.Combobox(root, textvariable=cuisine_var, values=["Italian", "Indian", "Chinese", "Korean","Carribean", "Peruvian", "Spanish", "French", "Japanese", "Brazilian"], font = larger_font)
cuisine_dropdown.pack()
cuisine_dropdown.configure(font=larger_font)
cuisine_dropdown.option_add("*TCombobox*Listbox.font", larger_font)

coursetype_label = ctk.CTkLabel(root, text="Course Type:",text_color = "black", fg_color="transparent", font = larger_font)
coursetype_label.pack()
coursetype_var = tk.StringVar()
coursetype_dropdown = ttk.Combobox(root, textvariable=coursetype_var, values=[],font = larger_font)
coursetype_dropdown.pack()
coursetype_dropdown.configure(font=larger_font)
coursetype_dropdown.option_add("*TCombobox*Listbox.font", larger_font)

time_label = ctk.CTkLabel(root, text="Time of Day:",text_color = "black", fg_color="transparent",font = larger_font)
time_label.pack()
time_var = tk.StringVar()
time_dropdown = ttk.Combobox(root, textvariable=time_var, values=[],font = larger_font)
time_dropdown.pack()   
time_dropdown.configure(font=larger_font)
time_dropdown.option_add("*TCombobox*Listbox.font", larger_font)

flavor_label = ctk.CTkLabel(root, text="Flavor Type:",text_color = "black", fg_color="transparent",font = larger_font)
flavor_label.pack()
flavor_var = tk.StringVar()
flavor_dropdown = ttk.Combobox(root, textvariable=flavor_var, values=[],font = larger_font)
flavor_dropdown.pack()
flavor_dropdown.configure(font=larger_font)
flavor_dropdown.option_add("*TCombobox*Listbox.font", larger_font)

diet_label =ctk.CTkLabel(root, text="Diet Type:" , text_color = "black", fg_color="transparent",font = larger_font)
diet_label.pack()
diet_var = tk.StringVar()
diet_dropdown = ttk.Combobox(root, textvariable=diet_var, values=[],font = larger_font)
diet_dropdown.pack()
diet_dropdown.configure(font=larger_font)
diet_dropdown.option_add("*TCombobox*Listbox.font", larger_font)

cuisine_dropdown.bind("<<ComboboxSelected>>", update_dropdowns)
coursetype_dropdown.bind("<<ComboboxSelected>>", update_dropdowns)
flavor_dropdown.bind("<<ComboboxSelected>>", update_dropdowns)
diet_dropdown.bind("<<ComboboxSelected>>", update_dropdowns)
time_dropdown.bind("<<ComboboxSelected>>", update_dropdowns)


recommends = False
# Create the recommend food button (only if it doesn't exist)
def buttonwow():
    global recommends
    global recommend_button
    if recommends == False:
        recommend_button = ctk.CTkButton(root, text="Recommend Food", command=recommend_food)
        recommend_button.pack()
        recommends= True

def display_dish(dish_name, nutritious, image_url, recipe_url):
    global dish_label
    dish_label_text = "Recommended dish: " + dish_name
    dish_label = ctk.CTkLabel(root, text = dish_label_text)
    dish_label.pack()
    global nutritious_label
    nutritious_label_text = "Nutritious?: " + nutritious
    nutritious_label = ctk.CTkLabel(root, text = nutritious_label_text)
    nutritious_label.pack()
    global label
    response = requests.get(image_url, stream=True, allow_redirects = False)
    image = Image.open(response.raw)
    tk_image = ctk.CTkImage(image, size=(280, 280))
    label = ctk.CTkLabel(root, image=tk_image, text = " ")
    label.pack()

def open_link(recipe_url):
    global link_label
    link = recipe_url
    link_label = ctk.CTkLabel(root, text="Recipe Link", text_color="blue", cursor="hand2")
    link_label.pack()
    link_label.bind("<Button-1>", lambda event: open_url(recipe_url))

def open_url(recipe_url):
    webbrowser.open(recipe_url)


# Start the main GUI event loop
root.mainloop()
