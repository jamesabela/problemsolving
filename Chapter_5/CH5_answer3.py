towns = ["Sydney", "Melbourne", "Christchurch", "Auckland"]

print(f"{'Town Name':<20} | {'Letter Count':<12}")  
print("-" * 35)  
for town in towns:  
    # Use len() to check characters per string item  
    print(f"{town:<20} | {len(town):<12}")
