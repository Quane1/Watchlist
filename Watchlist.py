"""
Monitor and update the anime watchlist text file with the program below
"""

# Import lines


user = input("What is your name? ")
print('Hello user ' + user + '! Welcome to your anime watchlist.')

# Empty list meant to hold all the anime titles
anime = []

# Exisiting titles on list
old_titles = """Jojo's Bizzare Adventure, \nAssassination Classroom, \nFood Wars, \nThe Night is Short, Walk on Girl,
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
    comma = line.find(",")
    title = line[:comma]
    anime.append(title.lower())

#print(anime)

"""
LIST OF FEATURES
Add to list
Delete from ;ost
Current
Sort
Display 
"""

cont = "yes"

while True:
    
    # Continue to run program
    if cont.lower() == 'yes':   
        # As long as cont is yes features loop
        print("------------------------------------- \n")
        print("""Features for Watchlist:
        1 - Add to list
        2 - Delete from list
        3 - Current show
        4 - Sort
        5 - Display\n""")
        feature = int(input("Input a choice 1 - 5 for a feature: "))
        print("-------------------------------------")

        if feature == 1:
            # Add
            new = input("What show would you like to add? ")
            addition = new + ", \n"
            # Only id it doesn't already exist in the list
            if new.lower() not in anime:
                source = open("anime_list.txt", "a")
                source.write(addition)
                anime.append(new.lower())
                source.close()
            else:
                print("Already on the list.")
        # Complete for further notice

        elif feature == 2:
            # Delete
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

        elif feature == 3:
            # Current
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

        elif feature == 4:
            # Sort 
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
                    """)
                    feature = int(input("Input a choice 1-4 for a feature: "))
                    print("-------------------------------------")

            
                    if feature == 1:
                        # Aplhabet

                        source = open("anime_list.txt", "r")
                        content = source.readlines()
                        source.close()
                        
                        for title in content:
                            
                            pass
                        pass

                    elif feature == 2:
                        # Title Length

                        source = open("anime_list.txt", "r")
                        content = source.readlines()
                        source.close()
                        
                        num = 0
                        title_length = []

                        """ Take the length pf each title in the list. 
                        Add the lengths to the list. 
                        Put the numbers in order
                        Rewrite the watchlist by comparing the title length by the index in the list
                        Take the first one that matchest in the list and delete in from content"""

                        # All of title length values are put into the list
                        while True:  
                            for title in content:
                                tit_len = len(title) - title.count(",") - title.count(" ") - title.count("\n")
                                #print(tit_len)
                                title_length.append(tit_len)
                                #print(num)
                                num += 1
                                #print(title_length[num-1])
                                pass
                            break
                        
                        # Rearrange the lengths by decreasing order 
                        title_length.sort(reverse= True)

                        titles = content.copy()

                        """
                        List comprehneison for title_length
                        Compare the len values to the titles from titles
                        If the values match replace content value 
                        Rewrite content to text file
                        """
                        
                        #print(num)

                        count = 0

                        #print(title_length)
                        #[34, 31, 27, 26, 24, 21, 20, 19, 17, 15, 14, 14, 13, 13, 12, 11, 9]
                        #[25, 24, 22, 22, 18, 17, 15, 15, 12, 11, 10, 10, 10, 9, 8, 8, 6]

                        for title in content:
                            # Find the index of the title length that matches the title 
                            print(title)
                            ln = len(title) - title.count(",") - title.count(" ") - title.count("\n")
                            print(ln)
                            index = title_length.index(ln)
                            titles[index - 1] = title
                            titles.remove(title)
                            count += 1
                            if count >= len(content):
                                break

                        #print(titles)

                        print("-------------------------------------")
                        pass

                    elif feature == 3:
                        # Episode count


                        pass

                    elif feature == 4:
                        # Oldest to Newest
                        pass

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

        elif feature == 5:
            # Display list
            # print("Display")
            print("Here's " + user + "'s anime watchlist: \n")
            source = open("anime_list.txt", "r")
            content = source.readlines()
            for title in content:
                comma = title.find(",")
                title = title[:comma]
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
