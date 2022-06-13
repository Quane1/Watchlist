# Helper Functions

# Use to takr substring just before the comma in titles
def comma_find(ln):
    comma_index = ln.find(",")
    new_word = ln[:comma_index]
    return new_word

# Counts the words in a title
def word_counter(ttl):
    cnt = 1
    for wrd in ttl:
        if wrd == " ":
            cnt += 1

    return cnt 

# Make abrivations to store the anime titles by name
def abriv(ttl):

    ttl = ttl.strip()

    lts = []
    space = 0
    counter = 1
    word_amnt = word_counter(ttl)

    for lt in ttl:
            lts.append(lt)

    first_word = lts[0]
    acro = first_word.upper()


    while counter < word_amnt:
        
        for lt in lts:
            if lt == " ":
                space = lts.index(lt)
                lts.pop(space)
                next_word = lts[space].upper()
                acro = acro + "_" + next_word
            

        counter += 1

    return acro    

# Establishes a dictionary full of details about each title
def deat(ttl, choice = "null", val = "null"):

    details = {}

    details["title"] = ttl
    details["abrivation"] = abriv(ttl)
    details["word count"] = word_counter(ttl)
        
    if choice != "null":
        details.update({choice: val})

    return details
