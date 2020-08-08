wavparser v0.1.0 by Andy Chamberlain

A simple script that you can use to parse a wav file into a list of lists of floats.

The return value from parse() called channel_data is a list of channels, where
each channel is a list of floats, where each float represents an audio sample and ranges
from -1.0 to 1.0

You can pass in a list of the above format to the save() function and optionally add
a filepath/filename, specify a bit depth, or specify a sample rate.

The save function will make sure the filename saved is unique so it doesn't overwrite
but if you want to have more control over the save process you can get the bytes
directly with get_wav_bytes()