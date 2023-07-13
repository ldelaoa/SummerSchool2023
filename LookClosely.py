import os
import matplotlib.image as mpimg
import random

train3_path = './HelloWorldDeepLearning_ImagingData/TRAIN3/'
train2_path = './HelloWorldDeepLearning_ImagingData/TRAIN2/'
val3_path = './HelloWorldDeepLearning_ImagingData/VAL3/'
val2_path = './HelloWorldDeepLearning_ImagingData/VAL2/'

path_list = [train3_path,val3_path,train2_path,val2_path]
name_list = ["train3","val3","train2","val2"]
num_imgs = 4

for i in range(len(path_list)):
    files_list = []
    for root, directories, files in os.walk(path_list[i]):
        for f in files:
            if f != ".DS_Store":
                files_list.append(os.path.join(root,f))
    for m in range(num_imgs):
        image = mpimg.imread(files_list[random.randint(0,len(files_list)-1)])
        plt.subplot(1,num_imgs,m+1),plt.imshow(image),plt.title(name_list[i]),plt.axis('off')

    plt.show()
