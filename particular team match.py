import pandas as pd

def get_team_matches(csv_file_path, team_name):
    try:
       
        df = pd.read_csv(csv_file_path)
        
        
        df = df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTR']) 
        df['HomeTeam'] = df['HomeTeam'].str.strip()
        df['AwayTeam'] = df['AwayTeam'].str.strip()
        
        
        team_matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)]

        if team_matches.empty:
            print(f"No matches found for team: {team_name}")
        else:
            print(f"Found {len(team_matches)} matches for team: {team_name}")
        
        return team_matches
    
    except FileNotFoundError:
        print("File not found. Check your file path.")
    except pd.errors.EmptyDataError:
        print("The file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    csv_path = r"C:\Users\acer\Downloads\datasetpython.csv"
    team = "Wolves"  
    
    matches = get_team_matches(csv_path, team)
    
    if matches is not None and not matches.empty:
        print(matches.head())  
