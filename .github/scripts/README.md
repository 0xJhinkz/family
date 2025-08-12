# Update Ages Script

This script automatically updates the ages of siblings in both the `ages.json` file and the `README.md` file. It is designed to be run by GitHub Actions on a daily schedule.

## Features

- Calculates ages with precision (years, months, days, hours)
- Updates the `ages.json` file with detailed age information
- Updates the `README.md` file's Family Information section
- Includes timestamps with timezone information (Asia/Makassar - WITA/UTC+8)
- Provides detailed logging for troubleshooting

## How it works

1. The script reads the current `ages.json` file which contains information about siblings
2. It calculates the current age for each sibling based on their birthdate
3. It updates the `ages.json` file with the new age information
4. It updates the Family Information section in the `README.md` file
5. If run by GitHub Actions, the changes are automatically committed and pushed

## Running manually

You can run this script manually with:

```bash
python .github/scripts/update_ages.py
```

## GitHub Actions Integration

This script is automatically run daily by the GitHub Actions workflow defined in `.github/workflows/update-ages.yml`.
