# WhatsApp-Automation-using-selenium-and-Python
This python program will read the names of person from a csv file and send them a message on Whatsapp.

Requirements:
1. Open cmd and type: pip install openpyxl
2. Update chrome to latest version(or above 80)
3. Download chromedriver and store it in E://Drivers
4. If chromedriver is stored at any other location, make the required changes in python code.


After running the code:
1. Wait till the whatsapp web page opens.
2. Now scan the code shown at the page using whatsapp installed in mobile.
3. Press enter at python console.

In this project, a excel file is stored in same folder as the main python file with name sample.csv.
This csv file will have name of the contacts.
When the python file runs, these name are read and stored in a list within the python.
Now for each name in the list, the following chat is opened and message is send.
We even have the option to send same message multiple times, thus spaming the chat.
