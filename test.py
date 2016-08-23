#for testing

def get_lucky(int):
    # This function allows the caller to get a lucky number for testing purposes.
    # This function accepts an integer and returns the text equivalent for 7 and 13 as 'seven' or 'thirteen'; otherwise returns 'unlucky'.

    if int == 7:
        return 'seven'
    elif int == 13:
        return 'thirteen'
    else:
        return 'unlucky'
