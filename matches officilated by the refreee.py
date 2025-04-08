import pandas as pd

def get_matches_by_referee(csv_file_path, referee_name):
    try:
        
        df = pd.read_csv(csv_file_path)
        
        
        df = df.dropna(subset=['Date', 'HomeTeam', 'AwayTeam', 'Referee'])
        
       
        df['Referee'] = df['Referee'].str.strip()
        df['HomeTeam'] = df['HomeTeam'].str.strip()
        df['AwayTeam'] = df['AwayTeam'].str.strip()
        
        
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])  
        
        
        matches = df[df['Referee'] == referee_name][['Date', 'HomeTeam', 'AwayTeam']]
        
        if matches.empty:
            print(f"No matches found for referee: {referee_name}")
        else:
            print(f"Found {len(matches)} matches officiated by {referee_name}")
        
        return matches.sort_values('Date')
    
    except FileNotFoundError:
        print("CSV file not found. Please check the path.")
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    csv_path = r"C:\Users\acer\Downloads\datasetpython.csv"
    referee = "M Dean"  
    
    result = get_matches_by_referee(csv_path, referee)
    
    if result is not None and not result.empty:
        
        for _, row in result.iterrows():
            print(f"{row['Date'].date()} - {row['HomeTeam']} vs {row['AwayTeam']}")
