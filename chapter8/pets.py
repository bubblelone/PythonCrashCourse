
def describe_pet(pet_name, animal_type='dog'):
    print("\ni have a " + animal_type + ".")
    print("my " + animal_type + "'s name is " + pet_name.title()+ ".")

describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')