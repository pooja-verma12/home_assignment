Steps to setup:

To work with Google Drive API, we have to set up our account and enable Google Drive API. Follow the steps below:

1. Go to https://console.cloud.google.com/
2. Click on "Google drive" and selecte "NEW PROJECT"
3. Write the name of the project in the field "Project name", keep "location" field as it is. Click on "Create"
4. Go to APIs and Services.
5. Enable Google Drive API for the new project you created project.
6. Go to the OAuth Consent screen and configure the Consent screen for your project.
7. Enter the name of your application. It will be shown on the consent screen.
8. Now go to Credentials.
9. Click on Create credentials, and go to OAuth Client ID. Select application type as "Desktop".
10.Enter your application’s name, and click Create
11.Your Client ID will be created. Download it to your computer and save it as credentials.json
12.Copy this "credentials.json" file to the checked out directory from GitHub.

Installation:
1. pip install –upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
2. pip install -U pytest

You will have to change the file name and file id in the test script as per the files present in your drive
Steps to run test file:
1. Open Python prompt
2. type "pytest -v -s test_google_drive.py > log.txt" 

Steps to run python file:
1. Open Python prompt
2. type "python google_drive.py" 
3. Select the option as per your choice 1. to download a file 2. exit
4. Provide file name and file id as string input, eg "xxx.pdf"


Test Cases which couldn't be automated:
1. Partial download of a file,check size of file in drive and then in local disk
2. Download of Zip password protected file
3. Download of files shared by someone else
4. Download of a very large file to verify timeout
5. Download of file to any desired path
6. Download file with view only/read only options
