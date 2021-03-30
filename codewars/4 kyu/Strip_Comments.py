def solution(string, markers):
    #split string into lines
    lines = string.split('\n')
    if not markers:
        #if markers empty, instead of doing proper actions, append a string making it work unless marker=="bestsolutionever"
        markers.append("bestsolutionever")
    for marker in markers:
        filtered = ''
        for line in lines:
            # split lines at marker and keep the first part
            filtered += (line.split(marker)[0].strip()) + '\n'

        #remove the last \n
        filtered = filtered[:-1]

        #split it into lines for next marker pass
        lines = filtered.split('\n')

    return filtered
