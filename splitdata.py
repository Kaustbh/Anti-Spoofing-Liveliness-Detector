import os 
import random
import shutil
from itertools import islice


outputFolderpath = "Datasets/SplitData2"
inputFolderpath = "Datasets/All2"
splitRatio ={"train":0.7, "val":0.2, "test":0.1}
classes = ["fake","real"]

try:
   shutil.rmtree(outputFolderpath)
   print("Removed Directory")

except OSError as e:
   os.mkdir(outputFolderpath)


# ---------- Directories to Create ---------- #

os.makedirs(f"{outputFolderpath}/train/images",exist_ok=True)
os.makedirs(f"{outputFolderpath}/train/labels",exist_ok=True)
os.makedirs(f"{outputFolderpath}/val/images",exist_ok=True)
os.makedirs(f"{outputFolderpath}/val/labels",exist_ok=True)
os.makedirs(f"{outputFolderpath}/test/images",exist_ok=True)
os.makedirs(f"{outputFolderpath}/test/labels",exist_ok=True)

# ---------- Get the Names ---------- #
listNames=os.listdir(inputFolderpath)
# print(listNames)

uniqueNames=[]

for name in listNames:
   # print(name)
   # print("\n")

   # --------------Original---------------#
   # uniqueNames.append(name.split('.')[0])

   # --------------Modified---------------#
   parts = name.rsplit('.', 1)

   # 'parts' is now a list containing two elements: the base name and the extension
   base_name = parts[0]
   extension = parts[1]

   print(base_name)
   print("\n")
   uniqueNames.append(base_name)
uniqueNames=list(set(uniqueNames))
# uniqueNames = set( base_name)

print("Unique Values:")
# for value in uniqueNames:
#     print(value)

print(len(uniqueNames))

# ---------- Shuffle ---------- #

random.shuffle(uniqueNames)

# ---------- Find the number of images for each folder ---------- #

lenData = len(uniqueNames)

lenTrain = int(lenData*splitRatio['train'])
lenVal = int(lenData*splitRatio['val'])
lenTest = int(lenData*splitRatio['test'])

print(f'Total Images: {lenData} \n Split: {lenTrain} {lenVal} {lenTest}')

# ---------- Put remaining images in Training ---------- #

if lenData != lenTrain+lenTest+lenVal:
   remaining = lenData-(lenTrain+lenTest+lenVal)
   lenTrain += remaining

print(f'Total Images: {lenData} \n Split: {lenTrain} {lenVal} {lenTest}')

# ---------- Split the list ---------- #

lengthToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input,elem)) for elem in lengthToSplit]
# print(Output)
print(f'Total Images: {lenData} \n Split: {len(Output[0])} {len(Output[1])} {len(Output[0])}')

# ---------- Copy the Files ---------- #

sequence = ['train', 'val', 'test']

for i, out in enumerate(Output):
   for filename in out:
    print(f'{filename}')
    print("\n")
    shutil.copy(f"{inputFolderpath}/{filename}.jpg",f"{outputFolderpath}/{sequence[i]}/images/{filename}.jpg")
    shutil.copy(f"{inputFolderpath}/{filename}.txt",f"{outputFolderpath}/{sequence[i]}/labels/{filename}.txt")


print("Split Process Completed ....")

# ---------- Creating Data.yaml File ---------- #

dataYaml = f'path: ../Data\n\
train: ../train/images\n\
val: ../val/images\n\
test: ../test/images\n\
\n\
nc: {len(classes)}\n\
names: {classes}'
             
           
f=open(f"{outputFolderpath}/data2.yaml",'a')
f.write(dataYaml)
f.close()

print("Data.yaml file Created ...")

   