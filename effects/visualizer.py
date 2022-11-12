import numpy as np
from scipy.signal import stft
import soundfile as sf
from utils.objects import VectorScale, Move
from utils.sb import Sprite

SB_DEFAULT_X, SB_DEFAULT_Y = 640, 480

class Visualizer:
    def __init__(self, fp):
        self._fp = fp
        self._data, self._sample_rate = sf.read(self._fp)
        self._data = np.sum(self._data, axis=1)
    
    @staticmethod
    def _duration(x, sample_rate):
        """Input the Sequence and sample rate, returns duration as millisecond"""
        return len(x) / sample_rate * 1000
    
    def duration(self):
        return self._duration(self._data, self._sample_rate)
    
    @staticmethod
    def _stft(sequence, nperseg):
        """Perform the Short Time Fourier Transform"""
        f, t, zxx = stft(sequence, nperseg=nperseg, noverlap=0)
        return f, t, zxx

    def render(self, ms=100, max_length=10, bar_count=20):
        dur = self.duration()
        nperseg = ms * self._sample_rate // 1000 
        f, t, zxx = self._stft(self._data, nperseg)
        # scaling time into ms
        t /= np.max(t)
        t *= dur
        # scaling frequency into bar count
        f = np.log(f + 1)
        f = (f - np.min(f)) / (np.max(f) - np.min(f))
        f *= bar_count
        spectrogram = np.log(np.abs(zxx) + 0.0001)
        bar_length = (spectrogram.T - spectrogram.min(axis=1)) / (spectrogram.max(axis=1) - spectrogram.min(axis=1)) * max_length
        bar_length[np.isnan(bar_length)] = 0
        bar_length = bar_length.T ** 4

        def get_bar_length(x):
            return np.mean(bar_length[(np.floor(f) == x) | (np.ceil(f) == x)].T, axis=1).T
        
        visualizer_render = []

        for i in range(bar_count):
            actions = []
            size_t = get_bar_length(i)
            pos = (SB_DEFAULT_X * (i + 1) // bar_count, SB_DEFAULT_Y + 20)
            actions.append(Move(0, t[0], t[-1], pos, pos))
            for t1, size1, t2, size2 in zip(t[:-1], size_t[:-1], t[1:], size_t[1:]):
                actions.append(VectorScale(0, int(t1), int(t2), (0.025, float(size1)), (0.025, float(size2))))
            visualizer_object = Sprite('sb/white.png')
            visualizer_object.add_actions(actions)
            visualizer_render.append(visualizer_object)
            
        return visualizer_render

def last_wish_visualizer():
    audio_fp = "Kry.exe - Last Wish (feat. Ice).wav"
    visualizer = Visualizer(audio_fp)
    objects = visualizer.render(ms=33, max_length=1)
    return objects
