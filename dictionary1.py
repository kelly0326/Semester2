# Dictionary
# testing example 1

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

# Testing example 2
# Below is nosql table
characters = {'bios':
        [
         {'name': 'Hermione',
          'age': 16,
          'major': 'Potions',
          'physical_features':
             {'color': {'eye': 'brown',
                        'hair': 'brown'},
              'height': "5'6"}
         },
         {'name': 'Harry',
          'age': 16,
          'major': 'Defense against the Dark Arts',
          'physical_features':
             {'color': {'eye': 'brown',
                        'hair': 'brown'},
              'height': "5'9"}
          },  
          {'name': 'Ron',
          'age': 16,
          'major': 'Care of Magical Creatures',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'red'},
              'height': "6'1"}
          }
        ]  
             }

characters["bios"][2]["major"]
# 'Care of Magical Creatures'

for character in characters["bios"]:
    # print(character)
    if character['name'] == 'Ron':
        print("Ron's major is:", character['major'])
        print("Ron's height is:", character['physical_features']['height'])

# Ron's major is: Care of Magical Creatures
# Ron's height is: 6'1

# Complex dictionary
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

info["personal_data"]
# {'name': 'Hermione',
#'age': 16,
#'major': 'Potions',
#'physical_features': {'color': {'eye': 'brown', 'hair': 'brown'},
# 'height': "5'6"}}

len(info["personal_data"])
# 4
info["personal_data"].keys()
# dict_keys(['name', 'age', 'major', 'physical_features'])
info["personal_data"]["physical_features"]
# {'color': {'eye': 'brown', 'hair': 'brown'}, 'height': "5'6"}

info["personal_data"]["physical_features"]["color"]
# {'eye': 'brown', 'hair': 'brown'}

info["personal_data"]["physical_features"]["color"]["hair"]
# 'brown'