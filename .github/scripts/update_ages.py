#!/usr/bin/env python3

import json
import re
import os
from datetime import datetime
from zoneinfo import ZoneInfo

def calculate_age(birth_date):
    """Calculate age in years, months, days, and hours"""
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()
    
    # Calculate the difference in days
    diff_days = (today - birth_date).days
    years = diff_days // 365
    remaining_days = diff_days % 365
    
    # Calculate months (approximation)
    months = remaining_days // 30
    remaining_days = remaining_days % 30
    
    # Calculate days and hours
    days = remaining_days
    hours = today.hour - birth_date.hour
    if hours < 0:
        hours += 24
        days -= 1
    
    return {
        "years": years,
        "months": months,
        "days": days,
        "hours": hours,
        "total_years": years + (months / 12) + (days / 365)
    }

def update_ages_json():
    """Update ages in the ages.json file"""
    print("Starting to update ages.json...")
    
    # Get the absolute path to the ages.json file
    script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    json_path = os.path.join(script_dir, 'ages.json')
    print(f"Looking for ages.json at: {json_path}")
    
    with open(json_path, 'r') as file:
        data = json.load(file)
    print("Successfully loaded ages.json")
    
    # Set timezone to Asia/Makassar (WITA/UTC+8)
    wita_timezone = ZoneInfo("Asia/Makassar")
    today = datetime.now(wita_timezone)
    data['last_updated'] = today.strftime('%Y-%m-%d')
    data['last_updated_full'] = today.strftime('%B %d, %Y %H:%M:%S (%Z)')
    
    for sibling in data['siblings']:
        birth_date = sibling['birthdate']
        age_details = calculate_age(birth_date)
        sibling['age'] = age_details['years']  # Keep simple age for compatibility
        sibling['age_details'] = age_details   # Add detailed age information
        print(f"Updated age for {sibling['name']}: {age_details['years']} years, {age_details['months']} months, {age_details['days']} days, {age_details['hours']} hours")
    
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=2)
    print("Successfully wrote updated ages.json")
    
    return data

def update_readme(data):
    """Update the README.md file with current ages"""
    print("Starting to update README.md...")
    
    # Get the absolute path to the README.md file
    script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    readme_path = os.path.join(script_dir, 'README.md')
    print(f"Looking for README.md at: {readme_path}")
    
    with open(readme_path, 'r') as file:
        content = file.read()
    print("Successfully loaded README.md")
    
    # Find the table section with siblings info
    table_pattern = r"## Family Information\n\nBelow are my siblings and their current ages.*?(?=\n\n## |$)"
    table_section = re.search(table_pattern, content, re.DOTALL)
    
    # Get update timestamp with timezone info
    wita_timezone = ZoneInfo("Asia/Makassar")
    now = datetime.now(wita_timezone)
    update_timestamp = now.strftime('%B %d, %Y %H:%M:%S') + ' (Denpasar, WITA Time (UTC+8))'
    print(f"Generated timestamp: {update_timestamp}")
    
    siblings_table = f"## Family Information\n\n> Last updated: {update_timestamp}\n\nBelow are my siblings and their current ages:\n\n| Name | Birthdate | Age | Detailed Age |\n|------|-----------|-----|-------------|\n"
    
    for sibling in data['siblings']:
        birth_date = datetime.strptime(sibling['birthdate'], '%Y-%m-%d')
        formatted_date = birth_date.strftime('%B %d, %Y')
        age_details = sibling['age_details']
        detailed_age = f"{age_details['years']} years, {age_details['months']} months, {age_details['days']} days, {age_details['hours']} hours"
        siblings_table += f"| {sibling['name']} | {formatted_date} | {sibling['age']} | {detailed_age} |\n"
    
    if table_section:
        # Replace the existing table with the updated one
        print("Found existing family information section, updating it...")
        updated_content = re.sub(table_pattern, siblings_table.strip(), content, flags=re.DOTALL)
    else:
        # If section doesn't exist, add it after the main description
        print("No existing family information section found, creating new section...")
        main_desc_pattern = r"# my-cat\n\nA simple implementation.*?(?=\n\n)"
        if re.search(main_desc_pattern, content, re.DOTALL):
            updated_content = re.sub(main_desc_pattern, lambda m: m.group(0) + "\n\n" + siblings_table, content, flags=re.DOTALL)
        else:
            # If main description not found, just add at the beginning
            updated_content = siblings_table + "\n\n" + content
    
    with open(readme_path, 'w') as file:
        file.write(updated_content)
    print("Successfully wrote updated README.md")

def main():
    """Main function to update both files"""
    try:
        print(f"Script running from: {os.path.abspath(__file__)}")
        data = update_ages_json()
        update_readme(data)
        print("Files updated successfully!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        print(traceback.format_exc())
        raise

if __name__ == "__main__":
    main()
