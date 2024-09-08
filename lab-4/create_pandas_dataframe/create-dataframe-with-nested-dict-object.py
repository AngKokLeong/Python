import numpy
import pandas

uni_graduates = {
    2010: {
        'Females': 6300,
        'Males': 6496
    },
    2011: {
        'Females': 7281,
        'Males': 6428
    },
    2012: {
        'Females': 7114,
        'Males': 6736
    },
    2013: {
        'Females': 8170,
        'Males': 7785
    },
    2014: {
        'Females': 7620,
        'Males': 7756
    }
}


print(pandas.DataFrame(uni_graduates))