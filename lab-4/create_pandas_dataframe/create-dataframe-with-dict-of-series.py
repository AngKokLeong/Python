import pandas

jan = pandas.date_range('20170101', periods=31)
feb = pandas.date_range('20170301', periods=31)
may = pandas.date_range('20170501', periods=31)
jul = pandas.date_range('20170701', periods=31)
aug = pandas.date_range('20170801', periods=31)
oct = pandas.date_range('20171001', periods=31)
dec = pandas.date_range('20171201', periods=31)

monthswith31days: dict = {
    "Jan": jan,
    "Feb": feb,
    "May": may,
    "Jul": jul,
    "Aug": aug,
    "Oct": oct,
    "Dec": dec
}

monthswith31days_dataframe: pandas.DataFrame = pandas.DataFrame(monthswith31days)

print(monthswith31days_dataframe)