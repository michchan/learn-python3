temps = [132, 235, 21351, 215]

# simple way
new_temps = []
for temp in new_temps:
    new_temps.append(temp / 10)
print(new_temps)

# * A more elegant way
new_temps = [temp / 10 for temp in temps]
print(new_temps)


# With if conditional for FILTERING
new_temps = [temp / 10 for temp in temps if temp > 1000]
print(new_temps) # All number >1000 will be kept and divided

# With if-else conditional for REPLACING
new_temps = [temp / 10 if temp > 1000 else 0 for temp in temps]
print(new_temps) # All number <=1000 will be replaced by 0