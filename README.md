## Family Information

> Last updated: August 13, 2025 05:49:21 (Denpasar, WITA Time (UTC+8))

Below are my siblings and their current ages:

| Name | Birthdate | Age | Detailed Age |
|------|-----------|-----|-------------|
| Jay-r | February 14, 2006 | 19 | 19 years, 6 months, 4 days, 21 hours |
| Noynoy | August 21, 2008 | 16 | 16 years, 12 months, 0 days, 21 hours |
| Axel | August 20, 2024 | 0 | 0 years, 11 months, 27 days, 21 hours |


# Siblings Age Tracker

An automated system to track and update the ages of my siblings. The repository uses GitHub Actions to update the ages daily and provides notifications through Discord.

## Family Information

> Last updated: August 13, 2025 05:49:12 (Denpasar, WITA Time (UTC+8))

Below are my siblings and their current ages:

| Name | Birthdate | Age | Detailed Age |
|------|-----------|-----|-------------|
| Jay-r | February 14, 2006 | 19 | 19 years, 6 months, 4 days, 21 hours |
| Noynoy | August 21, 2008 | 16 | 16 years, 12 months, 0 days, 21 hours |
| Axel | August 20, 2024 | 0 | 0 years, 11 months, 27 days, 21 hours |

## Features

- Automatically calculates and updates ages daily using GitHub Actions
- Tracks detailed age information (years, months, days, hours)
- Stores age data in structured JSON format
- Updates README with the latest age information
- Sends Discord notifications when changes are made
- Uses Asia/Makassar timezone (WITA/UTC+8) for timestamps

## How It Works

1. A GitHub Actions workflow runs daily at midnight (UTC)
2. The Python script calculates the current age of each sibling
3. Updates are made to both `ages.json` and this README file
4. Changes are automatically committed and pushed
5. A Discord notification is sent when changes are made

## Technical Implementation

- GitHub Actions workflow (`.github/workflows/update-ages.yml`)
- Python script for age calculation (`.github/scripts/update_ages.py`)
- JSON data storage (`ages.json`)
- Discord webhook integration for notifications

## Manual Triggering

You can manually trigger the age update workflow through the GitHub Actions tab in the repository.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.