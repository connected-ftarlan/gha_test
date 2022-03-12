import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="f", required=True, help="path to the json schema file to be uploaded")
args = parser.parse_args()

print(args.f)