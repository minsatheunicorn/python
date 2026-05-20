import pandas as pd
import numpy as np
exam_data={"name":["bananananananana","monkey","banana","mmoonnkkeeyy","banananannananananananana","mmmmooonnnkkkeeeyyy","bananaaaaaaaaaaaaaaa","monkeyyyyyyyyyyyyy","az","abcdefghijklmnopqrstuvwxyz"],
"score":[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
"attempt":[1,2,3,1,2,3,1,2,3,1]
}
labels=["a","b","c","d","e","f","g","h","i","j"]
df=pd.DataFrame(exam_data,index=labels)
print(df)