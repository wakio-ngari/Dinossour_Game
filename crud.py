import json

import os

def load_data():
    default_data= {"players": {}}
    if os.path.exists("data.json") :
        try :
            with open("data.json", "r") as file:
                data =json.load(file)
                print("Loaded data:", data)
                # Ensure the data has the correct structure
                if not isinstance(data, dict) or "players" not in data:
                    print("data.json is corrupted. Resetting to default structure.")
                    return default_data
                # Ensure that all the scores are only integers
                for player, scores_by_difficulty in data["players"].items():
                    if not isinstance(scores_by_difficulty, dict):
                        print(f"Corrupted data for player {player}. Resetting to an empty dictionary.")
                        data["players"][player] = {}
                    else:
                        for difficulty, scores in scores_by_difficulty.items():
                            if not isinstance(scores, list):
                                print(f"Corrupted scores for player {player} ({difficulty}). Resetting to an empty list.")
                                data["players"][player][difficulty] = []
                            else:
                                data["players"][player][difficulty] = [int(s) for s in scores]
                return data
        except json.JSONDecodeError:
            print("data.json is corrupted. Resetting to default structure.")
            return default_data
    return default_data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def update_high_score(data, player_name, score, difficulty):
    # makes sure  a player's entry exists in our game,also game difficulty
    if player_name not in data["players"]:
        data["players"][player_name]={}

   
    if difficulty not in data["players"][player_name]:
        data["players"][player_name][difficulty]=[]

    # Add the new score to the player's list for the given difficulty
    data["players"][player_name][difficulty].append(int(score))

    # Converts  all scores to integers
    data["players"][player_name][difficulty] = [int(s) for s in data["players"][player_name][difficulty]]
    
    data["players"][player_name][difficulty].sort(reverse=True)

    # retains and displays  only the top 4 scores of the highest scorers
    if len(data["players"][player_name][difficulty]) >4:
        data["players"][player_name][difficulty]=data["players"][player_name][difficulty][:4]

    save_data(data)

def delete_player_data(player_name):
    data=load_data()
    if player_name in data["players"]:
        del data["players"][player_name]  
        save_data(data) 
        print(f"Deleted data for player: {player_name}")
    else:
        print(f"Player {player_name} not found.")