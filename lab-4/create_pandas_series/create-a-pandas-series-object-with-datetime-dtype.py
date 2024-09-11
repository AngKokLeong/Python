import pandas

date_time_index = pandas.DatetimeIndex(['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04', '2017-10-05',
                    '2017-10-06', '2017-10-07', '2017-10-08', '2017-10-09', '2017-10-10',
                    '2017-10-11', '2017-10-12', '2017-10-13', '2017-10-14', '2017-10-15'
                    ],
                    dtype='datetime64[ns]',
                    freq='D'
                    )


print(pandas.Series(date_time_index))