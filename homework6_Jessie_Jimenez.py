#1. Create a list of existing web users
web_users = ['chachasoccer', 'turkeysandwichesrule', 'frankenstein', 'Fred', 'superstar8000']

#2. Create a list of new users 
new_users = ['chachasoccer', 'turkeysandwichesrule', 'winnethepooh', 'valentinesday', 'dino123']

#3. Loop to check if each new username is already taken
print("\nChecking new usernames:\n")

for username in new_users:
        if username in web_users:
            print(f"X '{username}': This username is already in use. Please choose a different usename.")
        else:
            print(f"✓ '{username}':This username is available.")

print("\n")



 #1 & 2 & 3. Create cities dictionary with nested information
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37400000,
        'fact': 'Tokyo is the world\'s most populous metropolitan area.'
    },
    'Paris': {
        'country': 'France',
        'population': 2161000,
        'fact': 'Paris is known as the City of Light and is famous for the Eiffel Tower.'
    },
    'Cape Town': {
        'country': 'South Africa',
        'population': 4618000,
        'fact': 'Cape Town is located at the southern tip of Africa and is known for Table Mountain.'
    }
}

# 4. Print information in the specified format
print("\n")
for city_name, city_info in cities.items():
    print(f"City: {city_name}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']:,}")
    print(f"Fact: {city_info['fact']}")
    print()

print("=" * 60)
print("Assignment Complete!")
print("=" * 60)
