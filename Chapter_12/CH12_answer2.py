# Assuming a local source text file named 'input_text.txt' exists  
try:  
    with open("input_text.txt", "r") as src, open("text_analysis.tsv", "w") as dest:  
        dest.write("Line Text	Character Count
")  
        for line in src:  
            clean_line = line.strip()  
            dest.write(f"{clean_line}	{len(clean_line)}
")  
    print("text_analysis.tsv metrics processed completely.")  
except FileNotFoundError:  
    print("Error: Ensure 'input_text.txt' resides in current scope workspace.")
