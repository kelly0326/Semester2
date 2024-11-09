# Dictionary

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