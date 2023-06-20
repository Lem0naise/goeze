# We are running this program on a subset of the pictures we received, after we ran another program to exclude pictures whose majority is black or indistinguishable colours.
import numpy as np
from PIL import Image

cols = [[[40, 50, 150], 0, "Water"], [[200, 200, 200], 0, "Land"], [[220, 220, 220],0, "Cloud"]] #blue, green, white


dir = 'imgs'
l = len(os.listdir(dir))
i = 0
for file in os.listdir(dir):

    img = im = Image.open(os.path.join(dir, file))
    img = im.convert('RGB')
    arr = np.array(img)
    x = 0
    l2 = len(arr)
    for row in range(len(arr)):
        x += 1
        for pix in range(0, len(arr[row]), 1): # increase this value for more speed but les accuracy (1 is every single pixel)
            dists = [0, 0, 0]
            for col in range(len(cols)): # for each rgb
                for each in range(3): # for each colour
                    dists[col] += abs(arr[row][pix][each] - cols[col][0][each]) # find distance from each colour
            mi = dists.index(min(dists)) # min
            cols[mi][1] += 1 # add one to pixel count
            if mi == 2: # cloud
                arr[row][pix] = np.array([255, 0, 0]) # make it red
            elif mi == 1: # land
                arr[row][pix] = np.array([0, 255, 0]) # make it green
            elif mi == 0: # water
                arr[row][pix] = np.array([0, 0, 255]) # make it blue

    im2 = Image.fromarray(arr)
    im2 = im2.convert("RGB")
    i += 1
    im2.save(f"new/{i}.jpg")     
    print(cols)
    print(f"{i} pics out of {l}")

cols.pop()
total = sum([x[1] for x in cols])
for each in cols:
    print(f'{each[2]} - {round((each[1]/total)*100, 2)}%')
