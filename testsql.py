import mysql.connector

cnx = mysql.connector.connect(user='root',
                             password='YOUR-PASSWORD-FOR-MYSQL',
                             host='localhost',
                             database='YOUR-DATABASE-NAME')
cursor =cnx.cursor()

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError, msg:
            print "Command skipped: ", msg

executeScriptsFromFile('SQL-FILE-LOCATION')
cnx.commit()
