from decimal import Decimal
import pytest
from app.errors import DataError
from app.modules.domain.rule import evaluate


def test_reprint(cases):
    actual, evidence = evaluate(cases['reprint'])
    assert actual == Decimal('19')
    assert evidence and all(len(row)==3 for row in evidence)


def test_trace_zero(cases):
    actual, evidence = evaluate(cases['trace_zero'])
    assert actual == Decimal('1')


def test_printed_overlap(cases):
    actual, evidence = evaluate(cases['printed_overlap'])
    assert actual == Decimal('8')


def test_large_ids(cases):
    actual, evidence = evaluate(cases['large_ids'])
    assert actual == Decimal('3')


def test_double_reprint(cases):
    with pytest.raises(DataError) as error:
        evaluate(cases['double_reprint'])
    assert error.value.code in {'BUSINESS','NUMBER','RANGE','TIMESTAMP'}


def test_out_of_range(cases):
    with pytest.raises(DataError) as error:
        evaluate(cases['out_of_range'])
    assert error.value.code in {'BUSINESS','NUMBER','RANGE','TIMESTAMP'}


def test_existing(cases):
    with pytest.raises(DataError) as error:
        evaluate(cases['existing'])
    assert error.value.code in {'BUSINESS','NUMBER','RANGE','TIMESTAMP'}

