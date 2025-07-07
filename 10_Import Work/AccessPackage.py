from Mypack import Mymodule1

print(Mymodule1.add(10, 20))   # 30
print(Mymodule1.PI)            # 3.14

import Mypack.Mymodule1

print(Mypack.Mymodule1.sub(20, 10))   # 10
print(Mypack.Mymodule1.PI)            # 3.14
