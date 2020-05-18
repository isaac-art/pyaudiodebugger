from synthesizer import Player, Synthesizer, Waveform


class AudioDebug:
    def __init__(self, pre=["C3", "E3", "G3"], post=["C3", "D3", "F3"]):
        self.pre = pre
        self.post = post
        self.player = Player()
        self.player.open_stream()
        self.synthesizer = Synthesizer(
            osc1_waveform=Waveform.sine, 
            osc1_volume=1.0, 
            use_osc2=False)

    def play_chord(self, chord):
        self.player.play_wave(self.synthesizer.generate_chord(chord, 0.5))

    def __call__(self, func):
        def logic(*args, **kwargs):
            print('pre')
            self.play_chord(self.pre)
            result = func(*args, **kwargs)
            print('post')
            self.play_chord(self.post)
            return result
        return logic


@AudioDebug(pre=["C3", "E3", "G3"], post=["C3", "D3", "F3"])
def test():
    return print("fun")

@AudioDebug(pre=["D3", "C4", "G4"], post=["C4", "D4", "F5"])
def test_two():
    test()
    return print("fun")


test_two()