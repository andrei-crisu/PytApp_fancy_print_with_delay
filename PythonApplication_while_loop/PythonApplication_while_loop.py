import time
# a small python game
def my_print(string,time_sleep=0):
     for i in string:
        print(i,end='')
        if time_sleep!=0:
            time.sleep(time_sleep)
     print()
     print()

rules="RULES\n"
rules+="Please select one of the next movies/TV series: \n"
rules+="[To select something] => Example :press 1 for Lucifer \n"
rules+="[ 1 ] Lucifer \n"
rules+="[ 2 ] Peaky Blinders \n"
rules+="[ 3 ] The Godfather \n" 
rules+="[ 4 ] Teen Wolf \n"
rules+="[ E ] To exit the game\n"
print()

my_print(rules)
while True:

    input_selection=input("Choose an option: ")
    print()
    if input_selection=="E" or input_selection=="e":
        my_print("\t\tGAME CLOSED",0.01)
        print('\a')
        break
    elif input_selection=="1":
        quote="The darker the darkness the brighter the light."
        movie="Lucifer"
    elif input_selection=="2":
        quote="The perfect balance between Apollo and Dionis ... irrational frenzy controlled by reason and self-reflection. "
        movie="Peaky Blinders"
    elif input_selection=="3":
        quote="I’m going to make him an offer he can't refuse."
        movie="The Godfather"
    elif input_selection=="4":
        quote="Life Can't Ever Be All Bad Or All Good. You Know, Eventually, Things Have To Come Back To The Middle."
        movie="Teen Wolf"
    else:
            my_print("\t\t< WRONG SELECTION > ERROR")
            print('\a')
            print()
            continue

    wisdom_word="\t\t <PC>  "+quote+"["+movie+"]"
    my_print(wisdom_word,0.05)