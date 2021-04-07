from mutagen.flac import FLAC
orig_audio = FLAC("Tartaglia.flac")
orig_audio.pop("synopsis")
orig_audio.pop("purl")
orig_audio.pop("description")
orig_audio.pop("encoder")
orig_audio["artist"] = "Yu-Peng Chen"
orig_audio["title"] = "Tartaglia"
print(orig_audio)

orig_audio.save("Tartaglia.flac")
