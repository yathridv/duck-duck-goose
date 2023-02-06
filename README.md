# duck-duck-goose
Example Python Program with a simple implementation of "Duck Duck Goose" game using a csv file.


## Installing and Running the Program

1. Clone the repo and `cd` into the project folder
1. Create and activate a virtual environment and install the libraries in the `requirements.txt` file
1. Run the `game.py` file and follow the prompts.

In Linux:
```

$ git clone https://github.com/jeff-dillon/duck-duck-goose.git

$ cd duck-duck-goose

$ python3 -m venv venv

$ source venv/bin/activate

(venv)$ pip install -r requirements.txt

(venv)$ python3 game.py

```

## How the Program Works

This program uses a CSV file to store a list of players including
their name and whether they are a "duck" or a "goose" in the game. 

When you run the program it will ask you for the name of the csv file. It will
continue to ask you until a valid filename is provided. Use the `players.csv` file.

Once a valid file name is provided, it will check to see if the file is valid 
(has both name and animal columns and has exactly one record with 'goose' in the 
animal column). Finally the program  finds the student that is the goose and 
displays their name.

### Imports

This program imports two libraries:
- pandas is an external library used for data analysis
- pathlib is a standard library used for working with files and directories

### Functions

This program defines three functions.
- `run_game()` is tha main routine for the duck duck goose game. It controlls the 
overall flow of the program.
- `get_goose(filename)` loads the data from the csv file into a dataframe which is the 
main data structure in pandas
- `validate_dataframe()` performs several checks on the dataframe to make sure it has
the columns and data needed to play the game.

### if __name__ == '__main__'

This is the piece of the code that is actually executed when you run the file. `if __name__ == '__main__'` is a way of determining if your script is being run directly by the interpreter, or if it is being imported into another script. This lets you control your script's behavoiur in either scenario. 

In this case, we want the game to run when this script is being directly run by the interpreter so we call the `run_game()` function.

## Next Steps

- Try adding more records to the csv file
- Try changing which student is marked as the goose in the csv file
- Try adding more than one goose to the csv file
- Try having no records with 'goose' in the csv file (all ducks)
- Try changing the column names in the csv file
- Try creating a new csv file and using it with the program

