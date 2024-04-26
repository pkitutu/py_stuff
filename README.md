# Python Stuff
Has simple algorithms written in Python

## Requirements
- Python3

## To run Tests
`$ python3 tests.py`

## Run Scripts
### Humanize Duration
`$ python3 humanize_duration.py <seconds>`  
Example:  
`$ python3 humanize_duration.py 3366400` 
>38 days, 23 hours, 6 minutes and 40 seconds

### Valid Braces
`$ python3 valid_braces.py <braces_string>`  
Example:  
`$ python3 valid_braces.py {{}}` 
>True
`$ python3 valid_braces.py {{}}]` 
>False