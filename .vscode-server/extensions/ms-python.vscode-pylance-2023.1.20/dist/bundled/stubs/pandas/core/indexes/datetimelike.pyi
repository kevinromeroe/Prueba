from pandas.core.indexes.extension import ExtensionIndex
from pandas.core.indexes.numeric import Int64Index

from pandas._libs.tslibs import BaseOffset

class DatetimeIndexOpsMixin(ExtensionIndex):
    @property
    def freq(self) -> BaseOffset | None: ...
    freqstr: str | None
    @property
    def is_all_dates(self) -> bool: ...
    @property
    def values(self): ...
    def __array_wrap__(self, result, context=...): ...
    def equals(self, other) -> bool: ...
    def __contains__(self, key): ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ...): ...
    def take(
        self, indices, axis: int = ..., allow_fill: bool = ..., fill_value=..., **kwargs
    ): ...
    def tolist(self) -> list: ...
    def min(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def argmin(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def max(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def argmax(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def isin(self, values, level=...): ...
    def where(self, cond, other=...): ...
    def shift(self, periods: int = ..., freq=...): ...
    def delete(self, loc): ...

class DatetimeTimedeltaMixin(DatetimeIndexOpsMixin, Int64Index):
    def difference(self, other, sort=...): ...
    def intersection(self, other, sort: bool = ...): ...
    def join(
        self, other, *, how: str = ..., level=..., return_indexers=..., sort=...
    ): ...
