def evaluate_pearson_strength(r_value):  
    abs_r = abs(r_value)  
      
    if abs_r > 1.0 or abs_r < 0.0:  
        return "Invalid configuration scope bounds."  
          
    if r_value >= 0.9: return "Very high positive correlation"  
    elif r_value >= 0.7: return "High positive correlation"  
    elif r_value >= 0.5: return "Moderate positive correlation"  
    elif r_value >= 0.3: return "Low positive correlation"  
    elif r_value > -0.3: return "No meaningful correlation profile discovered"  
    elif r_value >= -0.5: return "Low negative correlation"  
    elif r_value >= -0.7: return "Moderate negative correlation"  
    elif r_value >= -0.9: return "High negative correlation"  
    else: return "Very high negative correlation"

# Print verification output execution trace preview  
print("r=0.73 Evaluation:", evaluate_pearson_strength(0.73)) # High positive correlation
