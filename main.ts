basic.forever(function on_forever() {
    music.play(music.tonePlayable(Note.F, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.Heart, 300)
    music.play(music.tonePlayable(Note.G, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.SmallHeart, 150)
})
loops.everyInterval(1500, function onEvery_interval() {
    basic.showIcon(IconNames.StickFigure, 50)
})
