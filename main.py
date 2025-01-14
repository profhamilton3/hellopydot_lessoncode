


def on_forever():

    music.play(music.tone_playable(Note.F, music.beat(BeatFraction.SIXTEENTH)), music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HEART,300)
    music.play(music.tone_playable(Note.G, music.beat(BeatFraction.SIXTEENTH)), music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.SMALL_HEART,150)

basic.forever(on_forever)



def onEvery_interval():
    basic.show_icon(IconNames.STICK_FIGURE,50)

loops.every_interval(1500, onEvery_interval)