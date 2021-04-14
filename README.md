# How much time?
That is the question *everyone* asks. I've made the spreadsheet with my schedule to understand how much free time I have to spend it (or at least motivate myself) more productively.

The time is entered via ` - ` because for me it is visually more pleasant than through individual cells (I have already created this version of the table)

The program returns us the **number of hours**, even if it is minutes. That's what I need.

## Example
`10:55 - 13:25` returns `2.5`

## Quickstart
In order for this program to work, you need to do this: 
- Turn on the Google Sheets API (For more info use [Google Spreadsheets API](https://developers.google.com/sheets/api/quickstart/python));
- Install the Google Client Library: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`;
- Then you need to enter the ID of your table in Google Sheets in the file `tokens.py`. To determine what your table ID is, just look at the link. For example: `https://docs.google.com/spreadsheets/d/1UB1rF11HUTtIzRFbLOVEwBESmTSitlT_EGORvjHu54A/view`. In this case: `spreadsheet_id = '1UB1rF11HUTtIzRFbLOVEwBESmTSitlT_EGORvjHu54A'`

## For what needs?
This project will help me to remember how to cope with Google Spreadsheets API. It will also be used for my previous [one](https://github.com/htmlprogrammist/auto-sudoku)

## Someday
- Redo the `try` and `except` construction to avoid repetition
- Briefly do getting letters in `range_names`
- If the number of hours equals 0, then do not enter anything
