from pydub import AudioSegment
import numpy as np
import librosa

NOTE_THRESHOLD = -32  # decibels required for sound to be considered a note


def note(interval: AudioSegment):
    """Returns the note at a given interval of a pydub AudioSegment using a Fast-Fourier transform."""
    audio_data = interval.get_array_of_samples()
    audio_array = np.array(audio_data)
    fft = np.fft.fft(audio_array)
    dominant_frequency = np.argmax(np.abs(fft))
    return librosa.hz_to_note(dominant_frequency)


class Layer:
    """An interpretable data model of an instrument layer of a song."""

    def __init__(self, filename: str):
        """Builds an interpretable data model from an instrument layer MP3 file."""
        layer, sr = librosa.load(filename)
        onset_env = librosa.onset.onset_strength(y=layer, sr=sr)
        self.beats_per_minute = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0]
        sixteenth_notes_per_second = self.beats_per_minute * 4 / 60
        sixteenth_note_interval = 1000 / sixteenth_notes_per_second
        layer = AudioSegment.from_mp3(filename)
        intervals = layer[::sixteenth_note_interval]
        volume_per_interval = [interval.dBFS for interval in intervals]
        note_present_per_interval = [volume > NOTE_THRESHOLD for volume in volume_per_interval]
        self.note_sequence = [
            note(interval) if note_present else None
            for interval, note_present in zip(intervals, note_present_per_interval)
        ]
