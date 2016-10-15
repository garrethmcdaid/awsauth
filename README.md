# awsauth
Python library for authenticating to AWS API with GPG encrypted key and secret

This library allows you to use an encrypted AWS key and secret in python scripts that make calls to the AWS API.

This removes the need to keep your credentials in clear text on your local system.

To use, store your GPG encrypted credentials file in your ~/.aws/ directory, with an appropriate name. The file your key on the first line and your secret on the second line. No other text should be included.

To use the library in your python script, include it:

    import auth

and call it

    set_auth(key)

Where "key" is the name of the file in your ~/.aws/ directory excluding the GPG extension.


