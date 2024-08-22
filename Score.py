# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.

# add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.


from utils import SCORES_FILE_NAME

def add_score(difficulty):
    """
    Add points to the current score based on the difficulty.
    
    :param difficulty: The difficulty level of the game.
    :return: None
    """
    points_of_winning = difficulty * 3 + 5
    
    try:
        # Read current score
        with open(SCORES_FILE_NAME, 'r') as fr:
            file_score = fr.read().strip()
        
        if not file_score:
            file_score = 0
        else:
            file_score = int(file_score)
        
        # Update score
        new_score = file_score + points_of_winning
        
        # Write new score
        with open(SCORES_FILE_NAME, 'w') as fw:
            fw.write(str(new_score))
    
    except FileNotFoundError:
        # Create the file if it does not exist
        with open(SCORES_FILE_NAME, 'w') as fw:
            fw.write(str(points_of_winning))
    except Exception as e:
        print(f"An error occurred while updating the score: {e}")

def read_score():
    """
    Read and return the current score from the scores file.
    
    :return: The current score as a string or an error message.
    """
    try:
        with open(SCORES_FILE_NAME, 'r') as fr:
            file_score = fr.read().strip()
        
        return file_score if file_score else "0"
    
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"

