# pywavparser 

v0.4.0 by Andy Chamberlain

A simple script that you can use to parse a wav file into a list of lists of floats.

At the moment there is no formal installation so you'll just need to put wavparser.py into your working directory.

## Example:

```python
import wavparser as wp

sample_rate, audio_data = wp.parse("song.wav")

# get the bit depth of a wav file
bit_depth = wp.bitdepth("song.wav")

# save with a filepath
# wavparser will ensure ".wav" is the file extension
wp.save(audio_data, "some/path/to/altered song")

# save in working directory with auto-generated filename
wp.save(audio_data)
```

## Functions:

`parse(filepath) : tuple`

(sample_rate, audio_data) where audio_data is a list of lists of floats

`parseraw(filepath) : list`

audio data as a list of lists of floats

`save(audio_data, filepath=None, bitdepth=16, samplerate=44100) : string`

the destination path

`samplerate(filepath) : int`

the sample rate of the wav file at `filepath`

`bitdepth(filepath) : int`

the bit depth of the wav file at `filepath`