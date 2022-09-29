"""For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me."""

def backwards(X):
    return " ".join(i for i in reversed(X.split()));

print("Hi enter a sentence and i will return it funny! ");
UI = input("Here: ");

print(backwards(UI));
