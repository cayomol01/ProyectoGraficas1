from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad,oro,negative,painting,noise, rgb_map,prueba,glow,diamante,rubi

width = 960
height = 540

rend = Renderer(width, height)
rend.dirLight = V3(0.5, 0, -0.5)


rend.background = Texture("models/stoneWall.bmp")

rend.glClearBackground()
rend.active_texture = Texture("models/bullTexture.bmp")


rend.active_shader = negative
rend.glLoadModel("models/bull.obj",
                 translate = V3(-6, -0.8, -10),
                 scale = V3(0.20,0.20,0.20),
                 rotate = V3(0,45,0))

rend.active_shader = painting
rend.glLoadModel("models/bull.obj",
                 translate = V3(0, -0.8, -10),
                 scale = V3(0.20,0.20,0.20),
                 rotate = V3(0,0,0))

rend.active_shader = noise
rend.glLoadModel("models/bull.obj",
                 translate = V3(6, -0.8, -10),
                 scale = V3(0.20,0.20,0.20),
                 rotate = V3(0,-45,0))


rend.active_shader = oro
rend.glLoadModel("models/bull.obj",
                 translate = V3(-3, -5, -10),
                 scale = V3(0.20,0.20,0.20),
                 rotate = V3(0,22.5,0))

rend.active_shader = diamante
rend.glLoadModel("models/bull.obj",
                 translate = V3(3, -5, -10),
                 scale = V3(0.20,0.20,0.20),
                 rotate = V3(0,-22.5,0))


rend.glFinish("Outputs/Render.bmp")
#high angle
''' rend.active_shader = gourad
rend.active_texture = Texture("bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("bull.obj",
                 translate = V3(0, -1.7, -8),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(-35,0,0))

rend.glFinish("output.bmp") '''


#Low angle
''' rend.active_shader = gourad
rend.active_texture = Texture("bullTexture.bmp")

rend.dirLight = V3(0, -1, 0)
rend.glLoadModel("bull.obj",
                 translate = V3(0, -1.5, -7),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(-30,0,0))

rend.glFinish("output.bmp")
 '''
 
#middle shot
'''  
rend.active_shader = gourad
rend.active_texture = Texture("models/bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("models/bull.obj",
                 translate = V3(0, -1, -10),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(0,35,0))

rend.glFinish("Outputs/MiddleShot.bmp") '''

#Dutch shot
''' rend.active_shader = gourad
rend.active_texture = Texture("models/bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("models/bull.obj",
                 translate = V3(0, -1, -10),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(-20,0,45))

rend.glFinish("Outputs/DutchShot.bmp")
 '''