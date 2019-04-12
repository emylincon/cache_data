## cache data generation script and data file

`cachedata.py` is used to generate the data  
`table_data.py` and `table_data_3.py` contain different data sets  

* each of the data file contains two variables `table` and `seq`
* table is a dictionary
* seq is a list
* `seq` contains 1000 elements

## usage
```
import table_data

print(table_data.table)
print(table_data.seq)
```