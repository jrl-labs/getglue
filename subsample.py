import json
import csv
from numpy.random import choice
import sys

infile = 'data/subsampled_3000.json'
outfile = 'data/subsampled_300.json'
num_users_to_keep = 300


def main():
    """
    Reads infile, subsamples in the space of users, and writes to outfile.
    """
    with open(infile, 'r') as f:
        users = get_users(f)

    sys.stderr.write("%d unique users in %s\n" % (len(users), infile))

    users_to_write = choice(users, num_users_to_keep, replace=False)

    with open(infile, 'r') as f:
        with open(outfile, 'w') as g:
            write_subsample(f, g, users_to_write)


def get_users(f):
    """
    Returns a list of unique users contained in file buffer f.
    """
    users = set()
    for line in f:
        d = json.loads(line.strip())
        users.add(d['userId'])

    return list(users)


def write_subsample(f, g, users_to_write):
    """
    Reads file buffer f, if the userId in the row is in users_to_write, then
    write that row to file buffer g.
    """
    for line in f:
        d = json.loads(line.strip())
        user = d['userId']
        if user in users_to_write:
            g.write(line)


if __name__ == '__main__':
    main()
