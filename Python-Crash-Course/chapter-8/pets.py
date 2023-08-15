def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\ni have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')