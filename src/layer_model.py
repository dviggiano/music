from pydub import AudioSegment
import librosa

NOTE_THRESHOLD = -35  # decibels required for sound to be considered a note


class LayerModel:
    """An interpretable data model of an instrument layer."""

    def __init__(self, filename: str):
        """Builds an interpretable data model from an instrument layer MP3 file."""
        layer, _ = librosa.load(filename)
        bpm = librosa.beat.tempo(layer)[0]
        sixteenth_notes_per_second = bpm * 4 / 60
        sixteenth_note_interval = 1000 / sixteenth_notes_per_second
        layer = AudioSegment.from_mp3(filename)
        intervals = layer[::sixteenth_note_interval]
        volume_per_interval = [interval.dBFS for interval in intervals]
        note_present_per_interval = [volume > -35 for volume in volume_per_interval]
        self.note_sequence = []  # TODO FFT if note present, None otherwise
