class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age', 'score', 'set_age', '_year')

    def get_year(self):
         return self._year

    def set_year(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._year = value