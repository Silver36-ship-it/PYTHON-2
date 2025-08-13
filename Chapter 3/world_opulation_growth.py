initial_population = 8.1e9
growth_rate = 0.009  
years = 100
population = initial_population
print(f"{'Year':<5}{'Population(billion)':<10}{'Annual Increase':<10}")

for year in range(1, years + 1):
    new_population = population * (1 + growth_rate)
    increase = new_population - population

    print(f"{year:<5}{new_population/1e9:<10}{increase/1e9:<10}")
