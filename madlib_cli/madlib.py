
# regex = r"({*[A-z]+ ?[A-z]+([^A-z0-9])? ?[A-z]+})+"
import re

def print_text():
    intro="""
           
        

                    .___  ___.      ___       _______   __       __  .______        _______      ___      .___  ___.  _______ 
                    |   \/   |     /   \     |       \ |  |     |  | |   _  \      /  _____|    /   \     |   \/   | |   ____|
                    |  \  /  |    /  ^  \    |  .--.  ||  |     |  | |  |_)  |    |  |  __     /  ^  \    |  \  /  | |  |__   
                    |  |\/|  |   /  /_\  \   |  |  |  ||  |     |  | |   _  <     |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
                    |  |  |  |  /  _____  \  |  '--'  ||  `----.|  | |  |_)  |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
                    |__|  |__| /__/     \__\ |_______/ |_______||__| |______/      \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                            

                    ____________________________________________________________________________________________________________
                    Mad Libs is the world’s greatest word game—and can make anyone the funniest person in the room!  Mad Libs are
                    stories with words removed and replaced by blank spaces.  One player acts as the “reader” and asks the other
                    players, who haven’t seen the story, to fill in the blanks with adjectives, nouns, exclamations, colors, 
                    adjectives, and more. These words are inserted into the blanks and then the story is read aloud to hilarious
                    results.  There are no winners or losers, only laughter. 
                                                                                                   

                                                                                
                                                                                

         
 
"""
    print(intro) 
    
        


# ______________________________________________________
def read_template():
    """
    this function will read template.txt file 
    """
    try:
        file=open('../assets/template.txt','r')
        
        contents = file.read()
        # print(file)
        return contents
    except Exception as errorr:
        print(f"ERROR line 49   {errorr}")
        # pass
# _____________________________________________________
def parse(contents):

    """
    This function will give us a list of words which are inside the {} in the template text 
 
    """
    try:
        regex = r"({\w+ ?\w+'? ?\w+ ?\w+'?\w ?([0-9]-[0-9]+)?})+"


        words_lis=[]
        find_all_result = re.findall(regex, contents)

        for i in find_all_result:
        
            words_lis.append(i[0].translate({ord(i): None for i in '{}'}))
        # print(words_lis)
        return words_lis
    except Exception as errorr:
        print(f"ERROR line 71   {errorr}")
    
# _____________________________________________________
      
def merge(contents, inputs_lis,words_lis):  

    """
    this function will merge the user inputs with the template text
    """
    try:
        regex = r"({\w+ ?\w+'? ?\w+ ?\w+'?\w ?([0-9]-[0-9]+)?})+"
        # words_lis = parse(the_original_text)  
        
        for i in words_lis:
            replace_words = (re.sub(regex,'%s', contents))


        # print(replace_words% tuple(inputs_lis))
        return replace_words% tuple(inputs_lis)
    except Exception as errorr:
        print(f"ERROR line 91   {errorr}")
    



# _____________________________________________________

def create_a_copy(new_text):
    """
    This function will create a new file.txt that contains user inputs.
    """
    try:
        print(new_text)
        create_file = open('../assets/copy-template.txt','w')
        create_file.write(new_text)
    except Exception as errorr:
        print(f"ERROR line 107   {errorr}")

# _____________________________________________________

if __name__ == "__main__":
    print_text()
    the_original_text = read_template()
    parse(the_original_text)
    words_lis = parse(the_original_text)
    inputs_lis=[]
    for i in words_lis:
        inputs_lis.append(input(f"                    Enter a {i} : "))
    # print(inputs_lis)
    the_final_text=merge(the_original_text, inputs_lis,words_lis)
    
    create_a_copy(the_final_text)   
  
# _____________________________________________________







