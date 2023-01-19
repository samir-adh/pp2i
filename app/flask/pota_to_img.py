import numpy as np
import matplotlib.pyplot as plt

# sample = [['Ail', 'Ail', 'Radis'], ['Radis', 'Radis', 'Radis'], ['Radis', 'Salade', 'vide']]

def pota_to_img(pota, titre): 
    plt.switch_backend('agg')
    pota = np.array(pota)
    n,m = pota.shape
    legumes = []
    for i in range(n):
        for j in range(m):
            legumes.append(pota[i,j])
    legumes = np.unique(legumes)
    colors_map = {}
    for legume in legumes:
            colors_map[legume] = np.random.randint(low=0,high=256,size=3)
    colors_map['vide'] = [255,255,255]
    img = np.full(shape=(n,m,3),fill_value=([0,1,2]))
    for i in range(n):
        for j in range(m):
            img[i,j] = colors_map[pota[i,j]]
    markers = [plt.Line2D([0,0,],[0,0],color=[c/255 for c in color], marker='o', linestyle='') for color in colors_map.values()]
    plt.legend(markers,colors_map.keys(),numpoints=1)
    plt.title(label=titre)
    plt.axis('off')
    plt.imshow(img)
    filename = f"{np.random.randint(2048)}.png"
    plt.savefig('app/flask/static/pota/'+filename)
    return filename

