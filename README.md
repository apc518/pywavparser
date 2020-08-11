pywavparser v0.2.3 by Andy Chamberlain

A simple script that you can use to parse a wav file into a list of lists of floats.

At the moment there is no formal installation so you'll just need to put wavparser.py into your working directory.

Example:

```python
import wavparser as wp

audio_data = wp.parse("song.wav")

sample_rate = wp.samplerate("song.wav")
bit_depth = wp.bitdepth("song.wav")

# save in working directory with a filename
# wavparser will ensure ".wav" is the file extension
wp.save(audio_data, "altered song")

# save with a filepath
wp.save(audio_data, "example export folder/altered song")

# save in working directory with auto-generated filename
# on first run this will call the file "wavparser_output_0.wav"
wp.autopath = True
wp.save(audio_data)
```

The return value from parse() is a list of channels, where each channel is a list of floats and each float represents an audio sample and ranges from -1.0 to 1.0

You can pass in a list of the above format to the save() function and optionally add a filepath/filename, specify a bit depth, or specify a sample rate.

The save function will make sure the filename saved is unique so it doesn't overwrite but if you want to have more control over the save process you can get the bytes directly with get_wav_bytes()

Parsing a wav file loses the sample rate and bit depth information, so there are functions to get those values from a file as well: samplerate() and bitdepth()

Functions:

	parse(filepath)
	returns: list

	save(audio_data, filepath=None, bitdepth=16, samplerate=44100)
	returns: destination path, or simply filename if saved in working directory

	samplerate(filepath)
	returns: int

	bitdepth(filepath)
	returns: int

Fields/Flags:
	
	autopath
	type: bool
	default: False
	description: tells whether the save() function will automatically generate a filepath. If autopath is false, you must enter a filepath argument into the save() function.