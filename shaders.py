import numpy as np
from prueba import matlib

changer1 = 0
last_color1 = 0,0,0
changer2 = 0
last_color2=0,0,0
lib = matlib()

def flat(render, **kwargs):
    global lib
    # Normal calculada por poligono
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return (1-r), (1-g), (1-b)
    else:
        return 0,0,0


def gourad(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal =    [nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
    
    
def negative(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return (1-r), (1-g), (1-b)
    else:
        return 1,1,1
    




def unlit(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    return r, g, b


def toon(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.8:
        intensity = 0.7
    elif intensity <= 1:
        intensity = 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def metal(render, **kwargs):
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    if intensity < 0.2:
        r,g,b =0.2,0.2,0.2
    elif intensity <= 0.3:
        r,g,b = 0.1,0.1,0.1
    elif intensity < 0.5:
         r,g,b = 0.5,0.5,0.5
    elif intensity <= 0.6:
        r,g,b = 0.7,0.7,0.7
    elif intensity < 0.8:
        r,g,b = 0,0,0
    elif intensity <= 1:
        r,g,b = 1,1,1

    if intensity > 0:
        return r, g, b
    else:
        return 1,1,1
    
def oro(render, **kwargs):
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    if intensity < 0.2:
        r,g,b =0.3,0.3,0
    elif intensity <= 0.3:
        r,g,b = 0.2,0.2,0
    elif intensity < 0.5:
         r,g,b = 0.5,0.5,0
    elif intensity <= 0.6:
        r,g,b = 0.7,0.7,0
    elif intensity < 0.8:
        r,g,b = 0.1,0.1,0.1
    elif intensity <= 1:
        r,g,b = 0.9,0.9,0.0
    if intensity > 0:
        return r, g, b
    else:
        return 1,1,0.85
    
def diamante(render, **kwargs):
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    if intensity < 0.2:
        r,g,b =0,0.3,0.3
    elif intensity <= 0.3:
        r,g,b = 0,0.2,0.2
    elif intensity < 0.5:
         r,g,b = 0,0.5,0.5
    elif intensity <= 0.6:
        r,g,b = 0,0.7,0.7
    elif intensity < 0.8:
        r,g,b = 0,0.1,0.1
    elif intensity <= 1:
        r,g,b = 0,0.9,0.9
    if intensity > 0:
        return r, g, b
    else:
        return 0.85,1,1
    
    
def rubi(render, **kwargs):
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    if intensity < 0.2:
        r,g,b =0.3,0,0.3
    elif intensity <= 0.3:
        r,g,b = 0.2,0,0.2
    elif intensity < 0.5:
        r,g,b = 0.5,0,0.5
    elif intensity <= 0.6:
        r,g,b = 0.7,0,0.7
    elif intensity < 0.8:
        r,g,b = 0.1,0,0.1
    elif intensity <= 1:
        r,g,b = 0.9,0,0.9
    if intensity > 0:
        return r, g, b
    else:
        return 1,0.85,1


def glow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (render.camMatrix.item(0,2),
                    render.camMatrix.item(1,2),
                    render.camMatrix.item(2,2))

    glowAmount = 1 - lib.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    yellow = (1,1,0)

    b += yellow[2] * glowAmount
    g += yellow[1] * glowAmount
    r += yellow[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def textureBlend(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if render.active_texture2:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor2 = render.active_texture2.getColor(tU, tV)

        b += (1 - intensity) * texColor2[2]
        g += (1 - intensity) * texColor2[1]
        r += (1 - intensity) * texColor2[0]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if b < 0: b = 0
    if g < 0: g = 0
    if r < 0: r = 0

    return r, g, b

def painting(render, **kwargs):
    global changer1
    global last_color1
    
    
        
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))
    

    b *= intensity
    g *= intensity
    r *= intensity
    if changer1%7==0:
        changer1 +=1
        if intensity > 0:
            last_color1=r,g,b
            return r,g,b
        else:
            return 0,0,0
    else:
        changer1+=1
        if intensity > 0:
            return last_color1
        else:
            return 0,0,0
        
        
def rgb_map(render, **kwargs):
    
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                    nA[1] * u + nB[1] * v + nC[1] * w,
                    nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))
    

    b *= intensity
    g *= intensity
    r *= intensity
    
    lista = [r,g,b]
    maximo = max(lista)
    for i in range(len(lista)):
        if lista[i]!= maximo:
            lista[i]= 0
    if intensity > 0:
        return lista[0],lista[1],lista[2]
    else:
        return 0,0,0
    
def noise(render, **kwargs):
    
    
    global changer2
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if changer2%4==0:
        changer2+=1
        if intensity > 0 :
            return (1-g),(1-r),(1-b)
        else:
            return 1,0,0
    else:
        changer2+=1
        if intensity > 0 :
            return r,g,b
        else:
            return 0,1,1
        
        
def prueba(render, **kwargs):
    
    
    
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]
    
    print(u,v,w)
    print(tA,tB,tC)
    print(" ")

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    dirLight = list(render.dirLight)
    intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity


    if u==v or u ==w or v==w:
        return 0,0,0
    else:
        return 1,1,1
    
def normalMap(render, **kwargs):
        # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    tangent = kwargs["tangent"]
    bitangent = kwargs["bitangent"]

    

    b /= 255
    g /= 255
    r /= 255

    # P = Au + Bv + Cw
    tU = tA[0] * u + tB[0] * v + tC[0] * w
    tV = tA[1] * u + tB[1] * v + tC[1] * w

    if render.active_texture:
        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = list(render.dirLight)

    if render.normal_map:
        texNormal = render.normal_map.getColor(tU, tV)
        texNormal = [texNormal[0] * 2 - 1,
                     texNormal[1] * 2 - 1,
                     texNormal[2] * 2 - 1]
        texNormal = lib.scalarDiv(texNormal , lib.norm(texNormal))

        tangentMatrix = [[tangent[0],bitangent[0],triangleNormal[0]],
                        [tangent[1],bitangent[1],triangleNormal[1]],
                        [tangent[2],bitangent[2],triangleNormal[2]]]

        texNormal = lib.matmul(tangentMatrix,texNormal)
        texNormal = lib.scalarDiv(texNormal, lib.norm(texNormal))

        intensity = lib.dot(texNormal, lib.NegativeVector(dirLight))
    else:
        intensity = lib.dot(triangleNormal, lib.NegativeVector(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity
    if intensity >= 1:
        return 1,1,1 
    elif 0<intensity<1:
        return r,g,b
    else:
        return 0,0,0
    
    


