import pandas as pd

def analyze_home_win_percentage(csv_file_path):
    
    try:
        
        data = pd.read_csv(csv_file_path)
        
       
        total_matches = len(data)
        
        if total_matches == 0:
            return {'error': 'No match data found in the CSV file'}
        
        
        required_columns = ['FTR', 'HomeTeam', 'AwayTeam']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            return {'error': f'Missing required columns: {", ".join(missing_columns)}'}
        
        
        home_wins = len(data[data['FTR'] == 'H'])
        
        
        home_win_percentage = (home_wins / total_matches) * 100
        
        
        away_wins = len(data[data['FTR'] == 'A'])
        
       
        draws = len(data[data['FTR'] == 'D'])
        
       
        away_win_percentage = (away_wins / total_matches) * 100
        draw_percentage = (draws / total_matches) * 100
        
        
        home_teams_wins = data[data['FTR'] == 'H']['HomeTeam'].value_counts()
        top_home_teams = home_teams_wins.head(5).to_dict()
        
        
        away_teams_wins = data[data['FTR'] == 'A']['AwayTeam'].value_counts()
        top_away_teams = away_teams_wins.head(5).to_dict()
        
        
        return {
            'total_matches': total_matches,
            'home_wins': home_wins,
            'home_win_percentage': round(home_win_percentage, 2),
            'away_wins': away_wins,
            'away_win_percentage': round(away_win_percentage, 2),
            'draws': draws,
            'draw_percentage': round(draw_percentage, 2),
            'top_home_teams': top_home_teams,
            'top_away_teams': top_away_teams
        }
        
    except FileNotFoundError:
        return {'error': 'CSV file not found at the specified path'}
    except pd.errors.EmptyDataError:
        return {'error': 'The CSV file is empty'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}


if __name__ == "__main__":
    
    csv_file_path = r"C:\Users\acer\Downloads\datasetpython.csv"
    
 
    results = analyze_home_win_percentage(csv_file_path)
    
   
    if 'error' in results:
        print(f"Error: {results['error']}")
    else:
        
        print("\nFootball Match Analysis Results:")
        print("="*50)
        print(f"Total matches analyzed: {results['total_matches']}")
        print(f"Home wins: {results['home_wins']} ({results['home_win_percentage']}%)")
        print(f"Away wins: {results['away_wins']} ({results['away_win_percentage']}%)")
        print(f"Draws: {results['draws']} ({results['draw_percentage']}%)")
        
        print("\nTop Performing Home Teams (most wins):")
        print("-"*50)
        for team, wins in results['top_home_teams'].items():
            print(f"{team.ljust(20)}: {wins} wins")
        
        print("\nTop Performing Away Teams (most wins):")
        print("-"*50)
        for team, wins in results['top_away_teams'].items():
            print(f"{team.ljust(20)}: {wins} wins")
        print("="*50)
