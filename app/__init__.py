from pathlib import Path
from os import listdir
from time import sleep
import sys
import openpyxl

available_solvent_list = [
    "1,2-dioxane",
    "1,4-dioxane",
    "2-BuOH",
    "2-MeTHF",
    "n-PrOH",
    "acetone", 
    "DCM", 
    "DMF",
    "iPrOAc",
    "IPA", 
    "MeOH", 
    "MeCN", 
    "EtOAc", 
    "EtOH", 
    "TBME", 
    "pentane", 
    "Et2O", 
    "THF", 
    "DMSO"
    ]

available_diluent_list = ["NMP"]