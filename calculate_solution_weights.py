def calculate_solution_weights(molecular_weights, solutions_needed):
    outputlist = []
    for solution in solutions_needed:
        chemical_formula = solution.split('-')[0]
        concentration = solution.split('-')[1]
        try:
            weight = molecular_weights[chemical_formula]
            weight = weight * float(concentration[:-1])
            outputlist.append(f"{chemical_formula}-{concentration}-{weight:.2f}g")
        except KeyError:
            outputlist.append("unknown")
    return outputlist