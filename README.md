# ChemE545HW1

### extract_parameter:

This function takes the unit name, parameter name, and index of the wanted value as inputs. Then it searches the dictionary for the unit name key, then searches the unit name dictionary for the parameter name key, and grabs the value at the given index of that list. If the program can't find any of the dictionary keys or the index, it returns an error message. Otherwise, it formats the other variables and returns them.

### calculate_solution_weights:

This function takes the molecular weight dictionary and a solutions needed list as inputs. It first formats the solution needed to split up the chemical name and the concentration. Then it searches the molecular weight dictionary for the chemical name and gets the molecular weight value. This is then divided by the concentration to get the total weight needed. Then, the chemical name, concentration, and weight are added to an output list. If the program cannot find the chemical name in the keys of the molecular weight dictionary, it adds unknown to the list.

### Running these Files:

The python files can be ran in Jupyter notebook by adding them to the folder that the notebook file is in, then importing the functions. For example:

from extract_parameter import extract_parameter

Then the functions can be used as normal
