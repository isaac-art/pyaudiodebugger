import simpleaudio as sa


class AudioDebug:
    def __init__(self, pre='samples/1.wav', post='samples/2.wav'):
        self.pre = sa.WaveObject.from_wave_file(pre)
        self.post = sa.WaveObject.from_wave_file(post)

    def play_sample(self, sample):
        play_obj = sample.play()
        play_obj.wait_done()

    def __call__(self, func):
        def my_logic(*args, **kwargs):
            # print('pre')
            self.play_sample(self.pre)
            result = func(*args, **kwargs)
            # print('post')
            self.play_sample(self.post)
            return result
        return my_logic


@AudioDebug()
def two():
    print('two')


@AudioDebug(pre='samples/3.wav', post='samples/4.wav')
def one():
    print('one start')
    two()
    print('one end')


for i in range(0, 10):
    one()
