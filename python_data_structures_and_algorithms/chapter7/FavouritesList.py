class FavouritesList:

    class _item:
        # slots hard codes the attrs, which streamlines mem use.
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0

    def find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        # move item to pos p
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                        cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

        # public methods
        def __init__(self):
            # create empty list of pos favourites
            self._data = PosiitionalList()

