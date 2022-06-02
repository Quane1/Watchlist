"""
Monitor and update the anime watchlist text file with the program below
"""

# Import Lines
import helper_func

user = input("What is your name? ")
print('Hello user ' + user + '! Welcome to your anime watchlist.')

# Empty list meant to hold all the anime titles
anime = []

# Empty list to have the chronological order
org_order = []


# Exisiting titles on list
old_titles = """Jojo's Bizzare Adventure, \nAssassination Classroom, \nFood Wars, \nThe Night is Short Walk on Girl,
Mob Pyscho 100, \nDarling in the Franxx, \nKeep Your Hands off Eizouken, \nGhost Stories, \nSamurai Champloo, \nDeadman Wonderland,
Inuyasha, \nBleach, \nGod of High School, \nSailor Moon, \nFire Force, \nEvangelion, \nFooly Cooly, \nOne Piece, \nGhost Stories, \n"""

# Only needs to be done once
"""
# Write down initial titles
source = open("anime_list.txt","w+")
source.write(old_titles)
source.close()
"""

# Anime list has only the title of those in the text file
source = open("anime_list.txt", "r")
content = source.readlines()
source.close()



count = 0
for line in content:
    # Know how many are in the list
    count += 1
    title = helper_func.comma_find(line)
    anime.append(title.lower())

    # Able to get chronological order of additions
    org_order.append(title)
    #print(title)
    
#print(anime)

"""
LIST OF FEATURES
Add to list
Delete from ;ost
Current
Sort
Display 
"""

#Continue option
cont = "yes"

while True:
    
    # Continue to run program
    if cont.lower() == 'yes':   
        # As long as cont is yes features loop
        print("------------------------------------- \n")
        print("""Features for Watchlist:
        1 - Add to list
        2 - Delete from lists
        3 - Current show
        4 - Sort
        5 - Display\n""")
        feature = int(input("Input a choice 1 - 5 for a feature: "))
        print("-------------------------------------")

        # Add
        if feature == 1:
            
            new = input("What show would you like to add? ")
            addition = new + ", \n"
            # Only id it doesn't already exist in the list
            if new.lower() not in anime:
                source = open("anime_list.txt", "a")
                source.write(addition)
                anime.append(new.lower())
                org_order.append(new)
                source.close()
                count += 1
            else:
                print("Already on the list.")
        # Complete for further notice

        # Delete
        elif feature == 2:
            
            source = open("anime_list.txt", "r")
            content = source.readlines()
            source.close
            val = 0
            pick = input("WHhich anime do you want to delete? ")
            # Delete by the index in list
            if pick.lower() in anime:
                for title in anime:
                    val += 1
                    if pick.lower() == title:
                        del content[val - 1]
                        anime = content

                org_order.remove(pick)
                count -= 1


            else:
                print("This show doesn't exist in the list")

            # Write new list to file
            source = open("anime_list.txt", "w+")
            for title in content:
                addition = title 
                source.write(addition)
            source.close()

            pass
        # Complete for further notice

        # Current
        elif feature == 3:
            
            current = input("What anime are you currently watching? ")

            if current.lower() in anime:
                # if in list ask what episode your on
                watched = int(input('\nWhat episode are you on? '))
                # take away the watched from the total episodes 
                # if they are equal or ggreater remove from watchlist

                # NEED API TO START 
                # Crunchyroll, Funimation, hulu, netflix, hbomax, prime
                # As mant as possible research needed 
                pass

            else:
                source = open("anime_list.txt", "a")
                anime.append(current.lower())
                addition = current + ", \n"
                source.write(addition)
                source.close()

            pass

        # Sort
        elif feature == 4:
             
            #print("Sort")

            diff = "yes"

            while True:

                if diff.lower() == "yes":

                    print("""
                    Sort Oprtions:
                    1 - Alphabetically
                    2 - Title length
                    3 - Episode Count
                    4 - Oldest to Newest
                    5 - Reverse
                    """)
                    feature = int(input("Input a choice 1-5 for a feature: "))
                    print("-------------------------------------")

                    
                    # Aplhabet
                    if feature == 1:

                        source = open("anime_list.txt", "r")
                        content = source.readlines()
                        source.close()
                        
                        for title in content:
                            
                            pass
                        pass

                    # Title Length
                    elif feature == 2:

                        source = open("anime_list.txt", "r")
                        content = source.readlines()
                        source.close()
                        

                        """ Take the length pf each title in the list. 
                        Add the lengths to the list. 
                        Put the numbers in order
                        Rewrite the watchlist by comparing the title length by the index in the list
                        Take the first one that matchest in the list and delete in from content"""

                        # Array of just titles
                        #print(content)

                        titles = []
                        for line in content:
                            title = helper_func.comma_find(line)
                            titles.append(title)

                        # Sort the titles by length
                        """
                        Convert string to list
                        Delete space from string using find
                        index words based off letter count
                        """
                        titles_fix = titles.copy()
                        
                        num = 0
                        for title in titles_fix:
                            for letter in title:
                                num += 1
                                if (letter == " "):
                                    space = num

                            l = list(title)
                            del(l[space])
                            title = "".join(l)
                            print(title)
                                    

                        
                        #titles_fix.sort(key=len)
                        #titles_len.sort(key=len)
                        #print(titles_fix)
                       # print(titles_len)

                        print("-------------------------------------")
                        pass

                    # Episode count
                    elif feature == 3:


                        pass

                    # Oldest to Newest
                    elif feature == 4:
                        #print(org_order)
                        item_lst = []

                        for title in org_order:
                            print(title)
                            item_lst.append(title)

                        #print(item_lst)    

                        source = open("anime_list.txt", "w+")
                        for item in item_lst:
                            addition = item  + ", \n"
                            source.write(addition)
                        source.close()

                        pass
                    # Complete for now

                    # Reverse
                    elif feature == 5:
                        item_lst = []

                        source = open("anime_list.txt", "r")
                        content = source.readlines()
                        source.close()
                        
                        for title in content:
                            item = helper_func.comma_find(title)
                            item_lst.append(item)

                        item_lst.reverse()
                        # print(item_lst)
                            
                        # Write new list to file
                        source = open("anime_list.txt", "w+")
                        for item in item_lst:
                            addition = item  + ", \n"
                            source.write(addition)
                        source.close()
                        pass
                    # Complete for now

                    # Invalid Option
                    else:
                        print("Invalid Choice.")

                    
                    diff = input("Do you want to sort differently? ")
                    #print(diff)

                

                elif diff.lower() == "no":
                    break
                    
                elif diff.lower() != "yes" or diff.lower() != "no":
                    print("\nInvalid Choice.")
                    diff = input("Do you want to sort differently? ")
                
                

            pass

        # Display list
        elif feature == 5:

            # print("Display")
            print("Here's " + user + "'s anime watchlist: \n")
            source = open("anime_list.txt", "r")
            content = source.readlines()
            for line in content:
                title = helper_func.comma_find(line)
                print(title)
            pass
        #Complete for further notice

        else:
            print("Invalid Choice")

        cont = input("\nDo you want to do something else? ")
        
        pass

    # End program
    elif cont.lower() == 'no':
        print("Thank you for visiting" )
        break
        pass

    # Loop back 
    else:
        print("Invalid Choice\n")
        cont = input("Do you want to continue? ")
        pass
