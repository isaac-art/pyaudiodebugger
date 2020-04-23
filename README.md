# PYAUDIODEBUGGER - QUICK MOCKUP
plays samples when function called/completes

# REQUIREMENTS
simpleaudio

# USE
```
@AudioDebug()
def two():
    print('two')

@AudioDebug(pre='samples/g.wav', post='samples/w.wav')
def one():
    print('one start')
    two()
    print('one end')

for i in range(0, 10):
    one()
```

## TODO/IDEAS
- assign unique samples automatically
- play synthesized sounds rather than wavs
- export to track option rather than interupting
- sample duration based on time for function to complete (post only)
