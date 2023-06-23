from pydub import AudioSegment
import numpy as np
import librosa

NOTE_THRESHOLD = -34  # decibels required for sound to be considered a note


def note(interval: AudioSegment):
    """Returns the note at a given interval of a pydub AudioSegment using a Fast-Fourier transform."""
    samples = interval.get_array_of_samples()
    audio_data = np.array(samples)
    fft = np.fft.fft(audio_data)
    dominant_frequency = np.argmax(np.abs(fft))
    return librosa.hz_to_note(dominant_frequency)


class Layer:
    """An interpretable data model of an instrument layer of a song."""

    def __init__(self, filename: str):
        """Builds an interpretable users model from an instrument layer MP3 file."""
        layer, sampling_rate = librosa.load(filename)
        self.duration = librosa.get_duration(y=layer, sr=sampling_rate)
        onset_envelope = librosa.onset.onset_strength(y=layer, sr=sampling_rate)
        self.beats_per_minute = librosa.beat.tempo(onset_envelope=onset_envelope, sr=sampling_rate)[0]
        sixteenth_notes_per_second = self.beats_per_minute * 4 / 60
        sixteenth_note_interval = int(1000 / sixteenth_notes_per_second)
        layer = AudioSegment.from_mp3(filename)
        intervals = [(interval, interval.dBFS) for interval in layer[::sixteenth_note_interval]]
        note_present_per_interval = [volume > NOTE_THRESHOLD for _, volume in intervals]
        self.note_sequence = [
            note(interval) if note_present else None
            for (interval, _), note_present in zip(intervals, note_present_per_interval)
        ]
