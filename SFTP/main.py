import pysftp
myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print
    "Connection succesfully stablished ... "

    # Switch to a remote directory
    sftp.cwd('/var/www/vhosts/')

    # Obtain structure of the remote directory '/var/www/vhosts'
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:
        print
        attr.filename, attr

# connection closed automatically at the end of the with-block