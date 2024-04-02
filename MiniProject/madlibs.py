"""
first have a story text, with different interchangeable text surruonded with "<>", like <adjective>. <noun>
create a function that let user to replace with there own word, make it to be a complete story

"""

with open('story.txt', 'r') as f:
    story = f.read()

# as a list we would get duplicate elements, in order to fix this, we could use a set
# when we are adding new elements, set would only add element only when the it is unique
# words = []
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"


# enumerate() let us to have access to the position as well as the element at that position
for i, char in enumerate(story):
    if char == target_start: 
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
         word = story[start_of_word: i+1]
         words.add(word)
         start_of_word = -1

answers = {}

for word in words:
    answer = input(f"enter a word for {word}: ")
    # answers["key"] = "value"
    # for dictionary, we could access the key by using square bracket syntax like this 
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
