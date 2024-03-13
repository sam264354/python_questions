'''2-1. Simple Message: Assign a message to a variable, and then print that
message'''
message = "All of us are dead"
print(message)

'''2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.'''
msg = "Happy Earth"
print(msg)
msg = "Hello Mars"
print(msg)

'''2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”'''
personal_msg = "Tasha"
print("Hello", personal_msg,",", "would you like to learn some python today?")

'''2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.'''
name = "tasha pisona"
print("Lowercase :", name.lower())
print("uppercase :", name.upper())
print("titlecase :", name.title())


''' 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.” '''
quote = "\"To live is the rarest thing in the world.\""
auther = "Oscar Wild"
print(f"{auther} once said, {quote}") #f-string


'''2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.'''
famous_person = "Oscar Wild"
message = "\"To live is the rarest thing in the world.\""
print(famous_person, "once said,", message)

'''2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().'''
person_name = "\t\n     Ronaldo\t\n"
print("Using strip: ", person_name.strip()) 
print("Using lstrip: ", person_name.lstrip()) 
print("Using rstrip: ", person_name.rstrip()) 



'''2-8. File Extensions: Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do'''
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))


'''2-9. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should be four lines, with the number 8 appearing once on
each line'''
print(6+2)
print(12-4)
print(16/2)
print(4*2)


'''2-10. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message.'''
fvrt_number= 6
message = "My favorite number is: "+ str(fvrt_number)
print(message)


'''2-11. Adding Comments: Choose two of the programs you’ve written, and
add at least one comment to each. If you don’t have anything specific to write
because your programs are too simple at this point, just add your name and the
current date at the top of each program file. Then write one sentence describing
what the program does.'''
# All we have is now 

'''2-12. Zen of Python: Enter import this into a Python terminal session and skim
through the additional principles.'''
import this # its a built-in feature in Python, by writing this instruction it will show you a Zen you can say it poetry...

'''3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time'''
names = ["Anmol", "Pikachu", "Gangsta", "Igloo", "Karin", "Sulfuric-acid"]
for name in names:
    print(name)


'''3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name.'''
names = ["Anmol", "Pikachu", "Gangsta", "Igloo", "Karin", "Sulfuric-acid"]
for name in names:
    print("Hello, " + name + "!" + " How are you pagali..??")


'''3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”'''
#I would like to make a list of my favourite authors, so you have to compromise......,
favorite_authors = ['Oscar Wild', 'Khaled Hosseini', "Nemrah Ahmed", "Alex Michaelides"]
for author in favorite_authors:
    print("I would like to get an autograph book by " + author)


'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.'''
guest_list = ["Albert Einstine", "Issac Newton", "li Xun"]
for guest in guest_list:
    print("Dear, " + guest+ " "+ "You would be honored to join me for dinner!")
    


'''3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.'''
guest_list = ["Albert Einstine", "Issac Newton", "li Xun"]
guest_cant_make_it = "Issac Newton"
guest_list.remove(guest_cant_make_it)
print(guest_list)
new_guest = "Marie Curie"
guest_list.append(new_guest)
print(guest_list)

for guest in guest_list:
    print("Dear, " + guest+ "! "+ "You would be honored to join me for dinner!")


'''3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''
print("I find a bigger dinner table.")
guest_list.insert(0, "Taneesha")
guest_list.insert(len(guest_list)//2, "Zumar")
guest_list.append("Filiz")
for guest in guest_list:
    print("Dear, " + guest + "! "+ "You would be honored to join me for dinner!")


'''3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the number
of people you’re inviting to dinner.'''
print(len(guest_list))

'''4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza,
instead of printing just the name of the pizza. For each pizza, you should
have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of p'''
pizzas = ["Fajita", "Pepperoni", "Margherita"]
# for-in loop to print names of pizzas
for pizza in pizzas:
    print(pizza)

# Now we have to print a statement instead of name of pizza so let's go,
print("My favourite pizza with simple statement")
for pizza in pizzas:
    print("I like " + pizza + " pizza")

# Now we have to print review so 
print("I really like " + pizzas[1] + " pizza! and I would love to visit here again" )


'''4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as A
dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in
common. You could print a sentence, such as Any of these animals would
make a great pet!'''
animals = ["Cat", "Dog", "Rabit"]
# 1. print names of animals
for animal in animals:
    print(animal)

# 2. give a statement about each animal
for animal in animals:
    print(f"A {animal} would make a great pet.")

# 3. print common characteristic
print("All of these animals are loyal and would make a good pet.")