# Next Round Team Updater

This Python program is designed to update the list of teams for the next round of a competition or tournament. It utilizes the tkinter library for the graphical user interface (GUI) and the gspread library, which is Google's official Python API for accessing Google Sheets, to interact with a Google Sheets document that stores the team information.

## Prerequisites

Before running the program, please make sure you have the following:

- Python 3.x installed on your local machine
- Tkinter library installed (comes with Python, no separate installation needed)
- Google account with access to Google Sheets and the Google Sheets API enabled
- gspread Python library installed. You can install it using pip with the following command: pip install gspread
- Google Sheets API credentials in the form of a JSON file. For instructions on how to obtain the credentials, you can refer to the official gspread documentation: [gspread - Authentication](https://gspread.readthedocs.io/en/latest/oauth2.html)

## Usage

1. Clone or download the repository to your local machine.

2. Install the required dependencies mentioned in the Prerequisites section.

3. Replace the `credentials.json` file in the project directory with your own Google Sheets API credentials JSON file.

4. Open the `next_round_team_updater.py` file in a Python IDE or text editor.

5. Run the `next_round_team_updater.py` file to start the program.

6. The program will open a GUI window where you can update team name for the next round.

7. Click on the "Add to next round" button to update the Google Sheets document with the new team information.

8. You can view the updated information in the Google Sheets document.
