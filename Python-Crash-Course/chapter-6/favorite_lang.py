favorite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

lang = favorite_lang['sarah'].title()
print(f"Sarah's favorite language is {lang}.")
# # Looping Through All the Keys in a Dictionary
# for name, language in favorite_lang.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for var in favorite_lang:
#     print(f'{var.title()} is favorite language is {favorite_lang[var].title()}.')

# friends = ['phil', 'sarah']
# for name in favorite_lang:
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         lang = favorite_lang[name].title()
#         print(f"\t{name.title()}, I see you love {lang}!")

# if 'erin' in favorite_lang.keys():
#     print('Erin, thank you for taking the poll.')
# else:
#     print('Erin, please take our poll!')

# Looping Through a Dictionary’s Keys in a Particular Order
for name in sorted(favorite_lang):
    print(f'{name.title()}, thank you for taking the poll.')

# Looping Through All Values in a Dictionary
print('The following languages have been mentioned:')
for language in favorite_lang.values():
    print(language.title())

# To see each language chosen without repetition, we can use a set. A set is similar to a list except that each item in the set must be unique:
print('The following languages have been mentioned:')
for language in set(favorite_lang.values()):
    print(language.title())