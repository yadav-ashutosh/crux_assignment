# CRUX - Assignment 1

This is an assignment for crux.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites
- Openai paid account 
- Openai key
- Python version 3.11+ (might work for older versions also)

### Installation

1. Clone the repository
2. Install dependencies from requirments.txt
3. Create a constants.py file inside helper , create a variable OPEN_AI_KEY = 'secret_open_ai_key_copied_from_your_dashboard'
4. Run the project(make sure you are in the project directory) using "python manage.py runserver"

### Running
1. Once the project starts running you can go over port 8000 to test
2. Upload the excel sheet you want to test.
3. Once uploaded go to the terminal to see the progress of the processing
4. Currently proper validation for non-xlsx files is missing so project might break if any other type of file is given.
