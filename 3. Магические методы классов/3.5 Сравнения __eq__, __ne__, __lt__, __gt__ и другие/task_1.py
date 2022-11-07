class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y

    @property
    def max_speed(self):
        return self._max_speed


class Track:
    def __init__(self, start_x, start_y):
        self._start_x = start_x
        self._start_y = start_y
        self._tracks = []

    def add_track(self, tr):
        self._tracks.append(tr)

    def get_tracks(self):
        return tuple(self._tracks)

    def __get_lenght(self, i):
        return ((self._tracks[i-1].x - self._tracks[i].x) ** 2 + (self._tracks[i-1].y - self._tracks[i].y) ** 2) ** 0.5

    def __len__(self):
        len_1 = ((self._start_x - self._tracks[0].x) ** 2 + (self._start_y - self._tracks[0].y) ** 2) ** 0.5
        return int(len_1 + sum(self.__get_lenght(i) for i in range(1, len(self._tracks))))

    def __eq__(self, other) -> bool:
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
