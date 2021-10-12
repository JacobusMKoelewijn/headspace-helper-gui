from pathlib import Path
from os import listdir
from time import sleep
import sys
import openpyxl

available_solvent_list = ["IPA", "MeOH", "DCM", "MeCN", "Acetone", "Dioxane", "EtOAc", "EtOH", "TBME", "Pentane", "Et2O", "THF", "DMSO"]
available_diluent_list = ["NMP"]