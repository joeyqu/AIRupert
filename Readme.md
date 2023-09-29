# AIRupert

The aim of this project is to create an application that uses AI to summarise the contents of email attachments.

As it stands this Python script allows you to extract PDF attachments from your Gmail mailbox. It uses the IMAP protocol to access your mailbox, fetch emails, and save PDF attachments to a specified folder on your local machine.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed on your machine.
- A Gmail account with IMAP access enabled.
- [dotenv](https://pypi.org/project/python-dotenv/) Python package installed for managing environment variables.

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/joeyqu/AIRupert.git
   ```

2. Navigate to the project directory:

   ```shell
   cd AIRupert
   ```

3. Create a virtual environment (recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the project directory and add your Gmail credentials:

   ```dotenv
   GMAIL_USER=your.email@gmail.com
   GMAIL_APP_PASS=your_app_password
   IMAP_ADDRESS=imap.gmail.com
   IMAP_PORT=993
   DEFAULT_MAILBOX=Inbox
   ```

   Replace `your.email@gmail.com` with your Gmail email address and `your_app_password` with your Gmail App Password. You can also customize the IMAP server and mailbox if needed.

## Usage

1. Run the script:

   ```shell
   python app.py
   ```

2. The script will prompt you for your Gmail password. If you have defined `GMAIL_APP_PASS` in the `.env` file, it will use that; otherwise, it will ask for your password interactively.

3. The script will log in to your Gmail account and attempt to select the mailbox specified in the `.env` file or ask you to enter the mailbox name.

4. It will display the number of emails found in the selected mailbox and ask if you want to continue with the extraction.

5. If you choose to continue, the script will extract PDF attachments from all emails in the mailbox and save them in a folder named `storage` within the project directory.

6. The extracted PDFs will be organized in subfolders based on the email subject.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Joseph Whincup**

Feel free to contribute to this project or report any issues you encounter. Happy extracting!
