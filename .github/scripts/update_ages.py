#!/usr/bin/env python3

import json
import re
from datetime import datetime

def calculate_age(birth_date):
    """Calculate age based on birthdate"""
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()
    
    age = today.year - birth_date.year
    
    # Check if birthday has occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age

def update_ages_json():
    """Update ages in the ages.json file"""
    with open('ages.json', 'r') as file:
        data = json.load(file)
    
    today = datetime.now()
    data['last_updated'] = today.strftime('%Y-%m-%d')
    
    for sibling in data['siblings']:
        birth_date = sibling['birthdate']
        sibling['age'] = calculate_age(birth_date)
    
    with open('ages.json', 'w') as file:
        json.dump(data, file, indent=2)
    
    return data

def update_readme(data):
    """Update the README.md file with current ages"""
    with open('README.md', 'r') as file:
        content = file.read()
    
    # Find the table section with siblings info
    table_pattern = r"## Family Information\n\nBelow are my siblings and their current ages.*?(?=\n\n## |$)"
    table_section = re.search(table_pattern, content, re.DOTALL)
    
    siblings_table = "## Family Information\n\nBelow are my siblings and their current ages (as of {}):\n\n| Name | Birthdate | Age |\n|------|-----------|-----|\n".format(data['last_updated'])
    
    for sibling in data['siblings']:
        birth_date = datetime.strptime(sibling['birthdate'], '%Y-%m-%d')
        formatted_date = birth_date.strftime('%B %d, %Y')
        siblings_table += "| {} | {} | {} |\n".format(sibling['name'], formatted_date, sibling['age'])
    
    if table_section:
        # Replace the existing table with the updated one
        updated_content = re.sub(table_pattern, siblings_table.strip(), content, flags=re.DOTALL)
    else:
        # If section doesn't exist, add it after the main description
        main_desc_pattern = r"# my-cat\n\nA simple implementation.*?(?=\n\n)"
        if re.search(main_desc_pattern, content, re.DOTALL):
            updated_content = re.sub(main_desc_pattern, lambda m: m.group(0) + "\n\n" + siblings_table, content, flags=re.DOTALL)
        else:
            # If main description not found, just add at the beginning
            updated_content = siblings_table + "\n\n" + content
    
    with open('README.md', 'w') as file:
        file.write(updated_content)

def main():
    """Main function to update both files"""
    data = update_ages_json()
    update_readme(data)
    print("Files updated successfully!")

if __name__ == "__main__":
    main()
