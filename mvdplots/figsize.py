class FigSize:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._width = 3.25
            cls._height = 0.75 * 3.25
        return cls._instance

    def __call__(self, nr_cols: int = None, nr_rows: int = None):
        if nr_cols is nr_rows is None:
            return self._width, self._height
        elif nr_rows is None:
            return nr_cols * self._width, self._height
        else:
            return nr_cols * self._width, nr_rows * self._height

    def set_base(self, width, height=None, aspect=0.75):
        self._width = width
        if height is None:
            self._height = aspect * height
        else:
            self._height = height


figsize = FigSize()
