import csv, sys, os
from collections import Counter

class process(object):

    def __init__(self, directory):
        self.user_roles = self.read(directory + "user__roles.csv")
        self.users_field_data = self.read(directory + "users_field_data.csv")

    def read(self, filepath):
        ret = []
        with open(filepath) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                ret.append(row)
        print(ret[0])
        ret.pop(0)
        return ret

    def users_n_custodians(self, user_roles, users_field_data):
        u_ids = []
        for user in user_roles:
            if user[6]=='data_custodian':
                u_ids.append(user[2])

        n = 0
        for row in users_field_data:
            if row[0] in u_ids and row[9] != 0 and row[12] != 0:
                n += 1

        u_addresses = []
        for row in users_field_data:
            if row[0] in u_ids:
                u_addresses.append(row[6].split('@')[1])
        publishers = zip(Counter(u_addresses).keys(), Counter(u_addresses).values())
        publishers.sort(key = lambda x: x[1], reverse=True)
        print(publishers)

        if not os.path.exists('output/Users/'):
            os.makedirs('output/Users/')

        with open('output/Users/ncustodians.csv','w') as fp:
            writer = csv.writer(fp, delimiter=',')
            writer.writerow(['custodians', str(n)])
            writer.writerow('')
            for name in publishers:
                writer.writerow(name)
            fp.close()

    def run(self):
        self.users_n_custodians(self.user_roles, self.users_field_data)
        print(sys.argv)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('USAGE: python process.py <directory>')
    elif not os.path.exists(args[1]):
        print('ERROR: invalid directory')
    else:
        process(args[1]).run()
