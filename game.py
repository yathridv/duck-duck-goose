import pandas as pd
import pathlib

# Simple program to determine the 'goose' in a game of duck duck goose.
# This program expects a csv file with two columns, 'name' and 'animal' and
# exactly one record where the animal = 'goose'.

def validate_dataframe(df: pd.DataFrame) -> None:
    """Raise an exception if the data is not valid
    @param df - the pandas dataframe to be validated    
    """
    if not 'animal' in df.columns: 
        raise(Exception('Invalid file. Missing animal column.'))
    
    if not 'name' in df.columns: 
        raise(Exception('Invalid file. Missing name column.'))
    
    if not 'goose' in df['animal'].values: 
        raise(Exception('Invalid file. Must have exactly one goose record.'))

    if not df['animal'].value_counts()['goose'] == 1: 
        raise(Exception('Invalid file. Must have exactly one goose record.'))
    
    return None


def get_goose(file_name: str) -> str:
    """Returns the name of the player from the csv file where animal = 'goose'
    @param file_name : the name of the csv file to use
    """
    class_df = pd.read_csv(file_name)
    validate_dataframe(class_df)
    player = class_df.loc[class_df['animal'] == 'goose', 'name'].iloc[0]
    return player


def run_game() -> None:
    """Main routine for the duck duck goose game."""    
    try:
        file_name = input('What is the input file name? ') 
        filepath = pathlib.Path(file_name)
        while not filepath.is_file():     
            file_name = input(f'Cloud not find a file named "{filepath}". What is the input file name? ') 
            filepath = pathlib.Path(file_name)
        goose_name = get_goose(filepath)
        print(f'The goose is {goose_name}.')
    except Exception as ex:
        print(ex)

    return None


# run the main routine
if __name__ == '__main__':
    run_game()
