first_name = "tal"
last_name = "zohar"
full_name = f"{first_name} {last_name}"
print(full_name)
print("/////////////////\n")
print(f"Hello, {full_name.title()}!\n")
print("/////////////////\n")
message = f"\tHello, {full_name.title()}!\n"
print(message)


print("\t//////// Stripping whitespaces\n")
favorite_language = "   Python   "
print(favorite_language)

print("\t//////// Stripping right whitesapces ////////\n")
print(favorite_language.rstrip())

print("\t//////// Stripping left whitesapces ////////\n")
print(favorite_language.lstrip())

print("\t//////// Stripping left and right whitesapces ////////\n")
print(favorite_language.strip())
