import numpy as np
import cv2
from skimage.util.shape import view_as_windows
import imageio
import os

mat = np.zeros((255,255),dtype='float32')
mat[128:148,128:158] = 1

cv2.imshow("Initialization",mat)
stride = 4
mat2 = view_as_windows(mat,(stride,stride),step=stride)

rows = mat2.shape[0]
cols = mat2.shape[1]
neighbors = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
count = 1
while True:
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for n in neighbors:
                r = row+n[0]
                c = col+n[1]
                if (r<rows and r>=0) and (c < cols and c>=0) and abs(mat2[r][c]).all()==1:
                    live_neighbors+=1
            if (mat2[row][col].all() == 1) and (live_neighbors>3 or live_neighbors<2):
                    mat2[row][col] = -1
            if (mat2[row][col].all() == 0) and (live_neighbors==3):
                    mat2[row][col] = 2

    for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    if mat[i][j] > 0:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = 0
    cv2.imshow("mat",mat)
    cv2.imwrite(f"game/{count}.jpg",255*mat)
    count += 1
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

