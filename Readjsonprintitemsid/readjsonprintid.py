import sys
import json

if len(sys.argv) < 3:
    raise "Must pass in 2 arguments, input output"

print "Input File:", sys.argv[1]
print "Output File:", sys.argv[2]

ids = []
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        payload = json.loads(line)
        for user in payload["items"]:
            ids.append(str(user["id"]))
print "Stipped %s IDs" % (len(ids))

with open(sys.argv[2], "w") as f:
    f.writelines("\n".join(ids))

print "IDs written to %s" % sys.argv[2]
