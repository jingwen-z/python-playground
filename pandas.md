# Pandas

<https://pandas.pydata.org>

## Time Deltas

<https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html>

Add time delta to Pandas Timestamp:

```py
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 day')
Timestamp('2019-09-21 00:00:00')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 d')
Timestamp('2019-09-21 00:00:00')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 hour')
Timestamp('2019-09-20 01:00:00')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 h')
Timestamp('2019-09-20 01:00:00')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 minute')
Timestamp('2019-09-20 00:01:00')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 m')
Timestamp('2019-09-20 00:01:00')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 second')
Timestamp('2019-09-20 00:00:01')
>>> pandas.Timestamp('2019-09-20') + pandas.Timedelta('1 s')
Timestamp('2019-09-20 00:00:01')
```

## References

- Pandas, "Time deltas - Pandas", _Pydata_, 2019.
  <https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html>
