# Hangman
[![Build Status](https://travis-ci.com/GhostPandaGP/hangman.svg?branch=master)](https://travis-ci.com/GhostPandaGP/hangman)
[![codecov](https://codecov.io/gh/GhostPandaGP/hangman/branch/master/graph/badge.svg?token=E3UY6PX8XO)](https://codecov.io/gh/GhostPandaGP/hangman)

Computer thinks of a random word and you tries to guess
it by suggesting letters within a certain number of guesses. 

----

## Getting started

If you still do not have git installed on your computer, then install it using this [link](https://git-scm.com/download/win)
```bash
git clone https://github.com/GhostPandaGP/hangman.git
```
or use ssh
```bash
git clone git@github.com:GhostPandaGP/hangman.git
```
Now go to the game folder:
```bash
cd hangman
```
And now you can start the game.
To do this, enter the following command in the console:
- Linux/MacOS
```bash
python3 ./hangman/__init__.py
```
- Windows
```bash
python .\hangman\__init__.py
```
If you still do not have git installed on your computer, then install it using this [link](https://www.python.org/downloads/windows/). And do not forget to check the box next to "Add to PATH".

### Game process

When you start playing you will see the following:
```bash
Guess a letter:
```
Now you can enter one letter in order to try to guess the hidden word. if you guess correctly, then a coded word with a guessed letter will appear.
```bash
p
Hit!

The word: p***

Guess a letter:
```
if you have not guessed the letter, you will be shown the remaining word, the number of attempts and the number of attempts spent.
```bash
с
Missed, mistake 1 out of 5

The word: ****

Guess a letter:
```
 To win, guess the word without wasting all attempts.
 
 **Play and fun, friends!**
