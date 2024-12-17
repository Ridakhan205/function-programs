def kinetic_energy():
    # Get user inputs
    mass_kg = float(input("Enter the mass of the object in kilograms: "))
    velocity_ms = float(input("Enter the velocity of the object in meters per second: "))
    
    # Calculate kinetic energy
    KE = 0.5 * mass_kg * pow(velocity_ms, 2)
    
    # Return the calculated kinetic energy
    return KE

# Call the function and display the result
KE=kinetic_energy()
print(f"Kinetic energy of the body is {KE} joules.")