pywavparser v0.2.0 by Andy Chamberlain

A simple script that you can use to parse a wav file into a list of lists of floats.

The return value from parse() is a list of channels, where each channel is a list of floats and each float represents an audio sample and ranges from -1.0 to 1.0

You can pass in a list of the above format to the save() function and optionally add a filepath/filename, specify a bit depth, or specify a sample rate.

The save function will make sure the filename saved is unique so it doesn't overwrite but if you want to have more control over the save process you can get the bytes directly with get_wav_bytes()

Parsing a wav file loses the sample rate and bit depth information, so there are functions to get those values from a file as well: samplerate() and bitdepth()

Functions:

	parse(filepath)
	returns: list

	save(audio_data, filepath=None, bitdepth=16, samplerate=44100)
	returns: void

	samplerate(filepath)
	returns: int

	bitdepth(filepath)
	returns: int
