from getpass import getpass
import imaplib
import os
import email
import sys
import json
from dotenv import load_dotenv

load_dotenv()
cwd = os.getcwd()

class GMAIL_EXTRACTOR():
    def helloWorld(self):
        print("\nWelcome to Gmail extractor,\ndeveloped by Joseph Whincup.")

    def initializeVariables(self):
        self.usr = ""
        self.pwd = ""
        self.mail = object
        self.mailbox = ""
        self.mailCount = 0
        self.destFolder = ""
        self.data = []
        self.ids = []
        self.idsList = []
        self.pdfList = []
    
    def getLogin(self):
        print(f"\nPlease enter your Gmail password for user {os.getenv('GMAIL_USER')}.")
        self.usr = os.getenv('GMAIL_USER')
        self.pwd = os.getenv('GMAIL_APP_PASS') or getpass("Password: ")
    
    def attemptLogin(self):
        self.mail = imaplib.IMAP4_SSL(os.getenv('IMAP_ADDRESS'),os.getenv('IMAP_PORT') )
        if self.mail.login(self.usr, self.pwd):
            print("\nLogon SUCCESSFUL")
            self.destFolder = cwd + "/storage/"
            return True
        else:
            print("\nLogon FAILED")
            return False

    def selectMailbox(self):
        self.mailbox = os.getenv('DEFAULT_MAILBOX') or input("\nPlease type the name of the mailbox you want to extract, e.g. Inbox: ")
        bin_count = self.mail.select(self.mailbox)[1]
        self.mailCount = int(bin_count[0].decode("utf-8"))
        return True if self.mailCount > 0 else False
    
    def searchThroughMailbox(self):
        lol, self.data = self.mail.search(None, "ALL")
        self.ids = self.data[0]
        self.idsList = self.ids.split()
    
    def checkIfUsersWantsToContinue(self):
        print("\nWe have found "+str(self.mailCount)+" emails in the mailbox "+self.mailbox+".")
        return True if input("Do you wish to continue extracting all the emails into "+self.destFolder+"? (y/N) ").lower().strip()[:1] == "y" else False
    
    def parseEmails(self):
        
     
        emails = self.data[0].split()
        
        for anEmail in emails:
            type, self.data = self.mail.fetch(anEmail, '(UID RFC822)')
            raw = self.data[0][1]
            try:
                raw_str = raw.decode("utf-8")
            except UnicodeDecodeError:
                try:
                    raw_str = raw.decode("ISO-8859-1") # ANSI support
                except UnicodeDecodeError:
                    try:
                        raw_str = raw.decode("ascii") # ASCII ?
                    except UnicodeDecodeError:
                        pass
						
            msg = email.message_from_string(raw_str)
            
            raw = self.data[0][0]
            raw_str = raw.decode("utf-8")
           
            # Body #
            if msg.is_multipart():
                for part in msg.walk():
                    partType = part.get_content_type()
                    if partType == "application/pdf":
                        attchName = part.get_filename()
                        if bool(attchName):
                            self.pdfList.append({
                                "filename": attchName,
                                "subject": msg['subject'],
                                "part": part
                            })
                        
    def savePdfs(self):
     
        pdfs = self.pdfList
        for pdf in pdfs:
            attchFilePath = str(self.destFolder)+str(pdf.get('subject'))+str("/")+str(pdf.get('filename'))
            if not os.path.exists(attchFilePath):
                os.makedirs(os.path.dirname(attchFilePath), exist_ok=True)
                with open(attchFilePath, "wb") as f:
                    f.write(pdf.get('part').get_payload(decode=True))
                
    def __init__(self):
        os.makedirs(cwd+'/storage', exist_ok=True)
        self.initializeVariables()
        self.helloWorld()
        self.getLogin()
        if self.attemptLogin():
            not self.selectMailbox() and sys.exit()
        else:
            sys.exit()
        not self.checkIfUsersWantsToContinue() and sys.exit()
        self.searchThroughMailbox()
        self.parseEmails()
        self.savePdfs()