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