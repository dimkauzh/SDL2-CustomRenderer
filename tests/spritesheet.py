import fusionengine as fusion

window = fusion.Window("Spritesheet test", 500, 500)
window.set_fps(30)
main_image = fusion.Image(fusion.DEBUGIMAGE, 200, 200, 50, 50)

spr = fusion.SpriteSheet(fusion.DEBUGIMAGE, 100, 100)
spr.frame_size(60, 60)
spr.frame_pos(50, 50)

anim = fusion.Animation(window, spr)


@window.loop
def loop():
    anim.play(0.1)
    main_image.draw()
