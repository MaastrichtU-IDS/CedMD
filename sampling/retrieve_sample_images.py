
import os
import shutil
import pandas as pd

directory='C:\\Users\\P70065719\\Desktop\\Thesis\\FULL_LUNA_5_slices\\segmented_sequence_slices\\'
annos_path='C:\\Users\\P70065719\\Desktop\\Thesis\\code_snippets\\mycode\\positive_samples_new.csv'
test_op='C:\\Users\\P70065719\\Desktop\\Thesis\\Crowd_pos_unseg\\'
subdir=[]


df=pd.read_csv(annos_path)
df=df.dropna()

for dirpaths, dirnames, filenames in os.walk(directory):
    if not dirnames:
    	subdir.append(dirpaths)
df['slicenumber']=df['slicenumber'].astype(int)

for path in subdir:
 	path_split=path.split('\\')
 	row=df.loc[(df['seriesuid'] == path_split[-2]) & (abs(df['slicenumber'] - int(path_split[-1])) < 3)]
 	if len(row)>0:
 		new_path=test_op+path_split[-3]+"\\"+path_split[-2]+"\\"+path_split[-1]
 		print(new_path)
 		if not os.path.exists(new_path):
 			os.makedirs(new_path)
 		if not os.path.exists(new_path):
 			shutil.copytree(path,new_path)



 