# Dictionary of character roles
character_types = {
    "Ossas": "Sniper",
    "Sindri": "Medic",
    "Jabali": "Defender",
    "Glory": "Attacker"
}

# items(): returns a list of dictionary's key-value pairs as tuples
print(character_types.items())
print("*" * 40)

# keys(): returns a list of all keys in the dictionary
print(character_types.keys())
print("*" * 40)

# update(): updates the dictionary with new or modified key-value pairs
character_types.update({"Sindri": "All rounder", "Victor": "Attacker"})
print(character_types)
print("*" * 40)

# get(key): retrieves the value for a key; returns None if key is not found (avoids error)
print(character_types.get("Jabali"))     # Retrieves value for "Jabali"
print(character_types["Jabali"])         # Prints same value, but raises KeyError if key is absent
print(character_types.get("Alita"))      # Returns None (safe lookup)
# print(character_types["Alita"])        # Uncomment to see KeyError

print("*" * 40)

# Additional dictionary methods with examples:

# values(): returns a list of all values in the dictionary
print(character_types.values())

# pop(key): removes the key-value pair for the specified key and returns the value
removed_value = character_types.pop("Victor")
print(f"Removed value: {removed_value}")
print(character_types)

# clear(): removes all items from the dictionary
character_types.clear()
print("Dictionary after clear:", character_types)
