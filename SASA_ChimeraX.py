import csv
from chimerax.core.commands import run

def calculate_sasa_for_residues(session):
    # Open the structure (you can change the PDB ID or path here)
    run(session, "open 4byh")
    
    # Create a list to store the SASA results
    sasa_data = []

    # Loop over residues from 1 to 422 in chain A
    for res_num in range(290, 423):
        # Select each residue in chain A
        run(session, f"select :{res_num}")
        
        # Measure the SASA for the selected residue and get the direct output as a float
        sasa_value = run(session, "measure sasa sel")
        
        # Append the residue number and SASA value to the list
        sasa_data.append([res_num, sasa_value])
        
        # Clear selection before the next residue
        run(session, "select clear")

    # Save the results into a CSV file
    with open("sasa_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Residue", "SASA (Å²)"])
        writer.writerows(sasa_data)

    print("SASA results exported to sasa_results.csv")

# Call the function
calculate_sasa_for_residues(session)
