def create_water():
    hydrogen = 2
    oxygen = 1
    
    print(f"Combining {hydrogen} hydrogen atoms with {oxygen} oxygen atom...")
    
    water_molecules = min(hydrogen // 2, oxygen)
    
    if water_molecules > 0:
        print(f"Successfully created {water_molecules} water molecule(s)!")
        print("Chemical formula: H2O")
    else:
        print("Not enough atoms to create water.")

    return water_molecules

# Run the function
created_molecules = create_water()
print(f"Total water molecules created: {created_molecules}")