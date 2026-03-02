def release_decision(state, variables):
    # Unpack the decision variables found by Borg
    w, phi, tau = unpack(variables)
    
    # Calculate the current Gini coefficient of the 16 sub-deficits
    current_gini = calculate_gini(state.recent_deficits)
    
    # THE SWITCH
    if current_gini < tau:
        # Normal operations (Efficiency Mode)
        return radial_basis_function(state, w)
    else:
        # Justice-Explicit operations (Equity Mode)
        return radial_basis_function(state, phi)