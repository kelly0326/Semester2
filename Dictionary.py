# Dictionary & List

info = {'personal_data':
         {'name': 'Hermione',
          'age': 16,
          'major': 'Potions',
          'physical_features':
             {'color': {'eye': 'brown',
                        'hair': 'brown'},
              'height': "5'6"}
         },
       'other':
         {'friends': ['Harry', 'Ron', 'Victor'],
          'interests': ['horcruxes', 'homework', 'dentistry']
         }
      }

info.keys()
# dict_keys(['personal_data', 'other'])

info["personal_data"]["physical_features"]["color"]["hair"]
# 'brown'


# See Jupyter: 'Python4_Dictionary'

# Initial State [list vs. dictionary]
student = {'id': 87654321, 'name': 'Jose', 'homework': [10,9,9], 'exams': [91,86,92] }
temp = [87654321,"jose",[10,9,9], [91,86,92]]

# Retrive
temp[1]
# 'jose'

student["name"]
# 'Jose'

# Add 
# dictionary is to update, it's not to append values
temp.append(["cs50", "ds8"])
temp
# [87654321, 'jose', [10, 9, 9], [91, 86, 92], ['cs50', 'ds8']]

student.append(["cs50", "ds8"])
# AttributeError: 'dict' object has no attribute 'append'



