import openpyxl
import requests

# Open the Excel file
wb = openpyxl.load_workbook('tasks_solana.xlsx')

# Select the sheet with the data
sheet = wb['Task 5 - Solana']

def alter_rows():
    # Iterate through each row in the sheet
    for row in sheet[5:336]:
        # Get the name of the project from column C
        project_name = row[2].value

        # Make a request to the website
        url = "https://defillama.com/chain/Solana"
        response = requests.get(url)

        # Check if the project name is in the website's HTML
        if project_name in response.text:
            # If it is, write "yes" to column G
            row[6].value = "yes"
        else:
            # If it is not, write "no" to column G
            row[6].value = "no"

    # Save the changes to the Excel file
    wb.save('tasks_solana.xlsx')

def display_results():
    for row in sheet[5:336]:
        status = row[6].value

        if status == "yes":
            print(row[6].row)

if __name__ == "__main__":
    display_results()