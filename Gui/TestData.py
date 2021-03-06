from Gui.AudioData import AudioData


lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def create_audio_list():
    s1 = "I have a 2-dimensional table of data implemented as a list of lists in Python. I would like to sort the data by an arbitrary column. This is a common task with tabular data."
    s2 = "For example, Windows Explorer allows me to sort the list of files by Name, Size, Type, or Date Modified. "
    s3 = "I tried the code from this article, however, if there are duplicate entries in the column being sorted, the duplicates are removed."
    s4 = " This is not what I wanted, so I did some further searching, and found a nice solution from the HowTo/Sorting article on the PythonInfo Wiki. "
    s5 = "This method also uses the built-in sorted() function, as well as the key paramenter, and operator.itemgetter(). "
    s6 = "See section 2.1 and 6.7 of the Python Library Reference for more information.) The following code sorts the table by the second column (index 1)."
    s7 = "Note, Python 2.4 or later is required."
    s8 = "This works well, but I would also like the table to be sorted by column 0 in addition to column 1. In this example, column 1 holds the Last Name and column 0 holds the First Name. I would like the table to be sorted first by Last Name, and then by First Name. Here is the code to sort the table by multiple columns."
    s9 = "The cols argument is a tuple specifying the columns to sort by. The first column to sort by is listed first, the second second, and so on."
    s10 = "An example using Python's groupby and defaultdict to do the same task — posted 2014-10-09"
    s11 = "python enum types — posted 2012-10-10"
    audio_list = []
    audio_list.append(AudioData('Sandbox\\audio\\01 - Unfinished Allegro.mp3', "Angels Cry", "Angra", s1, "01 - Unfinished Allegro"))
    audio_list.append(AudioData('Sandbox\\audio\\02 - Carry On.mp3', "Angels Cry", "Angra", s2, "02 - Carry On"))
    audio_list.append(AudioData('Sandbox\\audio\\03 - Time.mp3', "Angels Cry", "Angra", s3, "03 - Time"))
    audio_list.append(AudioData('Sandbox\\audio\\04 - Angels Cry.mp3', "Angels Cry", "Angra", s4, "04 - Angels Cry"))
    audio_list.append(AudioData('Sandbox\\audio\\05 - Stand Away.mp3', "Angels Cry", "Angra", s5, "05 - Stand Away"))
    audio_list.append(AudioData('Sandbox\\audio\\06 - Never Understand.mp3', "Angels Cry", "Angra", s6, "06 - Never Understand"))
    audio_list.append(AudioData('Sandbox\\audio\\07 - Wuthering Heights.mp3', "Angels Cry", "Angra", s7, "07 - Wuthering Heights"))
    audio_list.append(AudioData('Sandbox\\audio\\08 - Streets Of Tomorrow.mp3', "Angels Cry", "Angra", s8, "08 - Streets Of Tomorrow"))
    audio_list.append(AudioData('Sandbox\\audio\\09 - Evil Warning.mp3', "Angels Cry", "Angra", s9, "09 - Evil Warning"))
    audio_list.append(AudioData('Sandbox\\audio\\10 - Lasting Child.mp3', "Angels Cry", "Angra", s10, "10 - Lasting Child"))
    audio_list.append(AudioData('Sandbox\\audio\\11 - Rainy Nights.mp3', "Fireworks", "Angra", s11, "11 - Rainy Nights"))
    return audio_list

def create_audio_list2():
    f01 = 'Sandbox\\audio\\01 - Unfinished Allegro.mp3'
    f02 = 'Sandbox\\audio\\02 - Carry On.mp3'
    f03 = 'Sandbox\\audio\\03 - Time.mp3'
    f04 = 'Sandbox\\audio\\04 - Angels Cry.mp3'
    f05 = 'Sandbox\\audio\\05 - Stand Away.mp3'
    f06 = 'Sandbox\\audio\\06 - Never Understand.mp3'
    f07 = 'Sandbox\\audio\\07 - Wuthering Heights.mp3'
    f08 = 'Sandbox\\audio\\08 - Streets Of Tomorrow.mp3'
    f09 = 'Sandbox\\audio\\09 - Evil Warning.mp3'
    f10 = 'Sandbox\\audio\\10 - Lasting Child.mp3'
    f11 = 'Sandbox\\audio\\11 - Rainy Nights.mp3'
    g01 = '01 - Unfinished Allegro'
    g02 = '02 - Carry On'
    g03 = '03 - Time'
    g04 = '04 - Angels Cry'
    g05 = '05 - Stand Away'
    g06 = '06 - Never Understand'
    g07 = '07 - Wuthering Heights'
    g08 = '08 - Streets Of Tomorrow'
    g09 = '09 - Evil Warning'
    g10 = '10 - Lasting Child'
    g11 = '11 - Rainy Nights'

    s1 = f01 + "I have a 2-dimensional table of data implemented as a list of lists in Python. I would like to sort the data by an arbitrary column. This is a common task with tabular data."
    s2 = f02 + "For example, Windows Explorer allows me to sort the list of files by Name, Size, Type, or Date Modified. "
    s3 = f03 + "I tried the code from this article, however, if there are duplicate entries in the column being sorted, the duplicates are removed."
    s4 = f04 + " This is not what I wanted, so I did some further searching, and found a nice solution from the HowTo/Sorting article on the PythonInfo Wiki. "
    s5 = f05 + "This method also uses the built-in sorted() function, as well as the key paramenter, and operator.itemgetter(). "
    s6 = f06 + "See section 2.1 and 6.7 of the Python Library Reference for more information.) The following code sorts the table by the second column (index 1)."
    s7 = f07 + "Note, Python 2.4 or later is required."
    s8 = f08 + "This works well, but I would also like the table to be sorted by column 0 in addition to column 1. In this example, column 1 holds the Last Name and column 0 holds the First Name. I would like the table to be sorted first by Last Name, and then by First Name. Here is the code to sort the table by multiple columns."
    s9 = f09 + "The cols argument is a tuple specifying the columns to sort by. The first column to sort by is listed first, the second second, and so on."
    s10 = f10 + "An example using Python's groupby and defaultdict to do the same task — posted 2014-10-09"
    s11 = f11 + "python enum types — posted 2012-10-10"
    s1 = s1 + s1  + s1  + s1  + s1
    audio_list = []
    audio_list.append(AudioData(f01, "Angels Cry", "Angra", s1, g01))
    audio_list.append(AudioData(f02, "Angels Cry", "Angra", s2, g02))
    audio_list.append(AudioData(f03, "Angels Cry", "Angra", s3, g03))
    audio_list.append(AudioData(f04, "Angels Cry", "Angra", s4, g04))
    audio_list.append(AudioData(f05, "Angels Cry", "Angra", s5, g05))
    audio_list.append(AudioData(f06, "Angels Cry", "Angra", s6, g06))
    audio_list.append(AudioData(f07, "Angels Cry", "Angra", s7, g07))
    audio_list.append(AudioData(f08, "Angels Cry", "Angra", s8, g08))
    audio_list.append(AudioData(f09, "Angels Cry", "Angra", s9, g09))
    audio_list.append(AudioData(f10, "Angels Cry", "Angra", s10, g10))
    audio_list.append(AudioData(f11, "Fireworks", "Angra", s11, g11))
    return audio_list


