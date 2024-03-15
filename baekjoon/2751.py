import sys

i = int(input())
#EOF
data = [int(d.rstrip()) for d in sys.stain.readlines()]
print("\n".join(sorted(data)))


-------
import json

data = ' { "name" : "kim", "age" : 23 }'
# data_json = json.lo
with open('member2.json', 'w') as w_file:
    d = json.load(r_file)
    print(d, type_(d))


d2 = json.dumps(member)
# 리스트 같은걸 저장할때 dump 보다는 pickle.dump()같은거

with open('dump_member.pk')