# my-cat

A simple implementation of the Unix/Linux "cat" command in multiple programming languages. This utility allows you to display file contents with optional line numbering.

## Family Information

Below are my siblings and their current ages (as of 2025-08-12):

| Name | Birthdate | Age |
|------|-----------|-----|
| Jay-r | February 14, 2006 | 19 |
| Noynoy | August 21, 2008 | 16 |
| Axel | August 20, 2024 | 0 |

## Implementations

This repository contains implementations in:

- Python (`my_cat.py`)
- Bash shell script (`my_cat.sh`)
- JavaScript (Node.js) (`my_cat.js`)
- Go (`my_cat.go`)

## Features

- Display contents of one or more files
- Option to number all lines (`-n` or `--number`)
- Option to number non-blank lines only (`-b` or `--number-nonblank`)

## Usage

### Python Version

```bash
# Make the script executable
chmod +x my_cat.py

# Display a file
./my_cat.py filename.txt

# Number all lines
./my_cat.py -n filename.txt

# Number non-blank lines
./my_cat.py -b filename.txt

# Display multiple files
./my_cat.py file1.txt file2.txt file3.txt
```

### Bash Version

```bash
# Make the script executable
chmod +x my_cat.sh

# Display a file
./my_cat.sh filename.txt

# Number all lines
./my_cat.sh -n filename.txt

# Number non-blank lines
./my_cat.sh -b filename.txt

# Display multiple files
./my_cat.sh file1.txt file2.txt file3.txt
```

### Node.js Version

```bash
# Make the script executable
chmod +x my_cat.js

# Display a file
node my_cat.js filename.txt

# Number all lines
node my_cat.js -n filename.txt

# Number non-blank lines
node my_cat.js -b filename.txt

# Display multiple files
node my_cat.js file1.txt file2.txt file3.txt
```

### Go Version

```bash
# Compile the Go program
go build -o my_cat my_cat.go

# Display a file
./my_cat filename.txt

# Number all lines
./my_cat -n filename.txt

# Number non-blank lines
./my_cat -b filename.txt

# Display multiple files
./my_cat file1.txt file2.txt file3.txt
```

## Error Handling

All implementations provide error handling for common issues:

- File not found
- Permission denied
- Other read errors

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.