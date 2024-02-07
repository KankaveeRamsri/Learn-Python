# Import Pandas

import pandas 

mydataset = {
    'cars' : ["BMW","Volvo","Ford"],
    'passings' : [3,7,2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

print("------------------------------------")

#Pandas as pd 

# import pandas as pd

# mydataset = {
#     'cars' : ["BMW","Volvo","Ford"],
#     'passing' : [3,7,2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

print("------------------------------------")

#Checking Pandas Version 

import pandas as pd

print(pd.__version__)

print("------------------------------------")
