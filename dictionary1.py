# Dictionary
# testing example

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


# Initial state
student = {'id': 87654321, 'name': 'Jose', 'homework': [10,9,9], 'exams': [91,86,92] }
temp = [87654321,"jose",[10,9,9], [91,86,92]]

temp[1]
# 'jose'
student["name"]
# 'Jose'