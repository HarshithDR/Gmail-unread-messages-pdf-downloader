# Email Attachment Downloader
The Email Attachment Downloader is a Python script designed to fetch attachments (specifically PDF files) from unread emails in your Gmail inbox. It allows you to automate the process of downloading attachments and organizing them on your local machine.

## How It Works
## Authentication:

The script connects to your Gmail account using IMAP and SSL.
You need to provide your email address and password when prompted.

## Attachment Download:

- The script identifies unread emails in your inbox.
- It extracts the attachments (PDF files) from these emails.
- The downloaded attachments are saved in a specific directory on your local machine, and a text file is generated listing the downloaded files.

## Customization:

You can customize the script to specify the type of attachments you want to download (in this case, PDF files).
The script organizes the attachments into directories based on your settings.

## Counter:

- The script uses a counter to create a unique folder for each download session to prevent overwriting.

## Prerequisites
Before using the script, make sure you have the following:

- A Gmail account
- Python installed on your local machine
- Required Python libraries: imaplib, os, and email


## Running the Script
- Run the script and provide your Gmail email address and password when prompted.
- The script will identify and download attachments from unread emails.
- Downloaded attachments are saved in a dedicated folder, and a text file listing the - downloaded files is generated.
- The script uses a counter to create a unique folder for each session, ensuring that files are not overwritten.

You can customize the script to fit your needs by adjusting the following parameters:

**Attachment Type:** You can specify the type of attachments you want to download (e.g., PDF files).
**Download Directory:** You can change the directory where the attachments are saved.
**Counter:** The script uses a counter to create unique folders for each session. You can modify the counter logic as needed.

**Important Note:**
- Make sure to use your Gmail email address and password when prompted.
- The script organizes attachments into folders and generates a text file listing the downloaded files.


Enjoy automating your email attachment downloads with this script!
