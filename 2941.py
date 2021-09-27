import re

S = input()
_S = (
    S.replace("c=", "č")
    .replace("c-", "ć")
    .replace("dz=", "dž")
    .replace("d-", "đ")
    .replace("lj", "lj")
    .replace("nj", "nj")
    .replace("s=", "š")
    .replace("z=", "ž")
)
print("_S", _S)
print(len(re.sub(r"/[a-zA-Z]/g", "", _S)))
