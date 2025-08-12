# GitHub Action: Update Sibling Ages

This GitHub Action automatically updates the ages of siblings in the `ages.json` file and the `README.md` file on a daily basis.

## How It Works

1. The action runs daily at midnight UTC using a scheduled cron job.
2. It calculates the current age of each sibling based on their birthdate.
3. It updates the `ages.json` file with the current ages and the last updated date.
4. It updates the siblings table in the `README.md` file.
5. If changes are detected, it commits and pushes those changes to the repository.

## Files Involved

- `.github/workflows/update_ages.yml`: The GitHub Action workflow file
- `.github/scripts/update_ages.py`: The Python script that updates the ages
- `ages.json`: The JSON file containing sibling information
- `README.md`: The main README file that displays the ages

## Manual Trigger

You can also trigger this action manually from the GitHub Actions tab in your repository by clicking on the "Run workflow" button.

## Siblings Information

- Jay-r: Born February 14, 2006
- Noynoy: Born August 21, 2008  
- Axel: Born August 20, 2024
