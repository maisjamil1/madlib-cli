
# regex = r"({*[A-z]+ ?[A-z]+([^A-z0-9])? ?[A-z]+})+"
import re

def read_text():
    try:
        with open('../assets/template.txt','r') as file:
        #   open('../assets/template.txt','r') as file:
          contents = file.read()
        
        # return contents
    except Exception as errorr:
        print(f"ERROR   {errorr}")
    return contents




# _____________________________________________________

user_input=[]
def inputs(file):
    words=[]
    regex =(r"(?<={)[\w'<>' -]+(?=})")
    words += re.findall(regex, file)
    # print(type(words) )
    for i in words:
        user_input.append(input(f'{i} '))
    return user_input

# _____________________________________________________

# def matching(contents):
#     # for i in range(len(user_input)): 
#     #     # for j in user_input:
#     #     x1 = re.sub((r"(?<={)[\w<>' -]+(?=})"), user_input[i], contents)
#     
  
# _____________________________________________________

def populate_template(user_input): 
    """edit the text file and merge it with user input"""
    try:
        with open('../assets/template.txt') as template:
            content = template.read()
        # for i in range(content.count("{")):
        for i in range(20):
            start = content.find("{")
            end = content.find("}") + 1
            content = content[:start] + user_input[i] + content[end:]
            # print(content)
        print(content)
        return content
    except:
        print('erooooooore')

# _____________________________________________________
def new_file():
    """
    This function to create a new file with the user inputs.
    """
    try:
        with open('../assets/copy-template.txt','w') as newfile :
            # newfile.write(read_text())
            newfile.write(populate_template(user_input))
            # print(read_file(),"sdfdsffds")
        # print("Is the file Closed? " , newfile.closed)
        return print(newfile.write(populate_template(user_input)))
    except Exception as errorr:
        print(f"ERROR   {errorr}")



if __name__ == "__main__":
    x = read_text()
    inputs(x)
    populate_template(user_input) 
    new_file() 

