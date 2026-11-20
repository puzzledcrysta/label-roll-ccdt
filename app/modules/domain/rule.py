from decimal import Decimal
from app.errors import DataError
from .values import spans, whole


def expanded(text, start, end, replay=False):
    recovered = set()
    for a,b in spans(text,closed=True):
        if a < start or b > end:
            raise DataError('BUSINESS',f'号段越界 {a}:{b}')
        chunk = set(range(a,b+1))
        if replay and recovered.intersection(chunk):
            raise DataError('BUSINESS',f'重复补打 {a}:{b}')
        recovered.update(chunk)
    return recovered


def evaluate(row):
    first, last = (whole(row[key],0,10**15) for key in ('计划首号','计划尾号'))
    if not 0 <= last-first < 50000:
        raise DataError('BUSINESS','计划范围须在五万枚内')
    printed = expanded(row['实印号段'],first,last)
    waste = expanded(row['判废号段'],first,last)
    if waste.difference(printed):
        raise DataError('BUSINESS','判废含未实印序号')
    reprints = expanded(row['补打号段'],first,last,replay=True)
    good = printed-waste
    if good.intersection(reprints):
        raise DataError('BUSINESS','补打含现存有效标签')
    count = len(good|reprints)
    return Decimal(count), [('已判废',len(waste),'枚'), ('补打成功',len(reprints),'枚'), ('缺号',last-first+1-count,'枚')]
