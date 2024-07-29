# WordGoblin
WordGoblin is a simple, lightweight word finder package that returns words containing letters specified by the user. English is supported within the package, and custom dictionaries or lists of words can easily be loaded to work with other languages.
     

<p align="center">
<img src="https://raw.githubusercontent.com/ian-nai/wordgoblin/main/wordgoblin_logo.png" height="200" width="180">
</p>

## Installation and Usage
Install using pip:
```
pip3 install wordgoblin
```

WordGoblin takes as few as one argument or as many as three. If you only want to check the built-in English dictionary for words matching your letters, simply pass your letters as a string to the check_dict method:

```
from wordgoblin import goblin
goblin.check_dict('yourstringofletters')
```

To only return words containing a certain number of letters, use the same method by specify your number as a second argument:

```
goblin.check_dict('yourstringofletters', 3)
```

And to use a custom dictionary, simply provide the path of your JSON dictionary as a second argument (the dictionary should list the words as keys; their values don't matter). You can also (optionally) include the number of letters for your word matches:

```
goblin.check_dict('yourstringofletters', 'path_to_custom_dict.json')

# or, to only return 4 letter words:
goblin.check_dict('yourstringofletters', 'path_to_custom_dict.json', 4)
```

To use a custom list of words instead of a JSON dictionary, use the following (very similar) syntax:

```
goblin.check_list('yourstringofletters', your_custom_list)

# or, to only return 4 letter words:
goblin.check_list('yourstringofletters', your_custom_list, 4)
```
