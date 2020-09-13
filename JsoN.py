import json,pandas,numpy as np,random
from skimage import io
import matplotlib.pyplot as plt

#print(np.ones(30))
print(np.linspace(2,10,4))
a = [i for i in range(0,10,2)]
b = [i for i in range(1,10,2)]
a = np.array(a)
b = np.array(b)
#content = {
    #'name': ['jason','nikhil','geoffrey'],
    #'phone': [15415,31,63156351]
    #}

#data = json.dumps(content)
#load  = json.loads(data)

#print(type(load))
#print(load['name'])

np.random.seed(0)
z1 =  np.random.randint(10, size=5)
print(z1)

photo = io.imread('something.png')
print(photo.shape)

plt.imshow(photo[:,::-1])

print(a@b)# Dot Product
plt.imshow(photo[:,:,0].T)#transpose


