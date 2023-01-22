# FeCuNgCpTzqdlJQ2


from ftplib import FTP

host = 'brainnest.bplaced.net'
user = 'brainnest_transfer'
password = 'muzik4813324'


with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)

    print(ftp.getwelcome())