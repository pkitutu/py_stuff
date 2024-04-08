import sys
def humanize_duration(seconds):
    if seconds == 0:
        return 'now'
    res = _humanize_duration(seconds)
    return res[0] if len(res) == 1 else '%s and %s'%(', '.join(res[:-1]), res[-1])

def _humanize_duration(seconds):
    if seconds ==0:
        return []
    if seconds < 60:
        return ['%s %s'%(seconds, _pl(seconds, 'second'))]
    if seconds < 60*60:
        mins = divmod(seconds, 60)
        return ['%s %s'%(mins[0], _pl(mins[0], 'minute'))]+_humanize_duration(mins[1])
    if seconds < 60*60*24:
        hrs = divmod(seconds, 60*60)
        return ['%s %s'%(hrs[0], _pl(hrs[0], 'hour'))]+_humanize_duration(hrs[1])
    if seconds < 60*60*24*365:
        days = divmod(seconds, 60*60*24)
        return ['%s %s'%(days[0], _pl(days[0], 'day'))]+_humanize_duration(days[1])
    yrs = divmod(seconds, 60*60*24*365)
    return ['%s %s'%(yrs[0], _pl(yrs[0], 'year'))]+_humanize_duration(yrs[1])
    
    
def _pl(val, word, append='s'):
    if val == 1:
        return word
    return '%s%s'%(word, append)


if len(sys.argv) < 2:
    print('Please provide a duration in seconds as an argument')
else:
    secs = sys.argv[1]
    if  secs.isdigit():
        print(humanize_duration(int(sys.argv[1])))
    else:
        print('Invalid input - please enter a number of seconds')