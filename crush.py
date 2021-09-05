import itertools
import argparse
import os

os.system("clear")


banner = """
this is a crunch alt for termux and kalinethunter for non-root devices

needed: python 3 newist version

by: toxic-development

"""

print(banner)

####################
# main bit of the program with all the gen

def gen_list(chars, x):
    l = itertools.product(chars, repeat=x)

    return l

def main(w, c, f):
    # check if word present
    if w == "None":
        print("[!] word needed for program to run (eg: python3 cruch.py -w w?r? -c od -f output.txt)")
        quit()
    else:
        # get the number of ? in word
        w_chk = w.split("?") 
        len_q = 0

        for i in w_chk:
            if i == "":
                len_q = len_q + 1
            else:
                pass
        if len_q == 0:
            print("[!] word doesn't have any ? in it (eg: w?r?)")
        else:
            print("amount of ? in word: ", len_q)
    
    # comp part

    # file part
    if f == "COMMAND_OUTPUT":
        out = True
    else:
        try:
            file = open(f, "w")
            out = False
        except FileNotFoundError:
            print("[!] file ("+f+") not found! passible derevtory doesn't exist")
            quit()

    # get the itertools list
    print("making list...")
    if c == "ALL_CHARS":
        c = "1234567890qwertyuiopasdfghjklzxcvbnmWERTYUIOPQASDFGHJKLZXCVBNM!£$%^&*()_-=<>.,\|?/'@#"
    else:
        pass

    l = gen_list(c, len_q) # get list

    # output part
    m = []
    for i in l:
        # fix all not needed details
        pas = str(i)
        pas = str(pas)
        pas = pas.replace("')","")
        pas = pas.replace("('","")
        pas = pas.replace(" ","")
        pas = pas.replace("'","")
        pas = pas.split(",")
        
        word = ""
        t = 0
        for x in w_chk:
            if x == "":
                word = word + pas[t]
                t = t + 1
            else:
                word = word + x
        if out == True:
            print(word)
        else:
            word = word + "\n"
            m.append(word)


    if out == False:
        print("writing to file...")
        file.writelines(m)
        file.close()
        print("done!")
    else:
        print("done!")


###################



###########
# get all args
def get_args():
      parser = argparse.ArgumentParser(
      description='crush command and help menu',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)      
    
      parser.add_argument('-w',
      metavar='--word',
      type=str,
      default="None",
      help="the word to gen list (eg: w?r? or ?????) ")
      
      parser.add_argument('-c',
      metavar='--chars',
      type=str,
      default="ALL_CHARS",
      help="chars to use woth the word")

      parser.add_argument('-f',
      metavar='--file',
      type=str,
      default="COMMAND_OUTPUT",
      help="file to dave list too or don't select for command line output ")

      return parser.parse_args()


args = get_args()
main(args.w, args.c, args.f)
