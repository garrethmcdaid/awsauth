import gnupg
import os
import getpass

def set_auth(k, phrase=False):

    h = os.path.expanduser("~")

    gpg = gnupg.GPG(homedir='~/.gnupg')

    with open(h + "/.aws/" + k + ".gpg", "rb") as f:
        if phrase != True :
            status = gpg.decrypt_file(f, output=h + "/.aws/aws.key.tmp")
        else:
            status = gpg.decrypt_file(f, passphrase=getpass.getpass(prompt="Please enter your GPG passphrase:") , output=h + "/.aws/aws.key.tmp")

    if not status.ok:
       print "Decryption error, exiting..."
       exit()

    with open(h + "/.aws/aws.key.tmp", "rb") as f:
        lines = f.read().splitlines()

    os.environ["AWS_ACCESS_KEY_ID"] = lines[0]
    os.environ["AWS_SECRET_ACCESS_KEY"] = lines[1]

    os.remove(h + "/.aws/aws.key.tmp")
