import pandas as pd

def new_process_wallet_pnl(csv_file_2, total_wallet_pnl, winning_percentage, avg_buys_per_token, quick_trade_percentage, file_counter, start_date, end_date, win_rate, average_buy_size, avg_time_held_str, avg_trades_per_day, df_spl_transactions, winning_days, losing_days, sorted_tokens_by_pnl, daily_pnl, file_counter_path, losing_percentage):
    # Read the wallet addresses from the CSV file
    df_wallets = pd.read_csv(csv_file_2)
    wallet_addresses = df_wallets['wallet address'].unique()
    
    # Initialize an empty DataFrame to hold qualifying wallet addresses
    qualifying_wallets = pd.DataFrame(columns=['WalletAddress'])
    
    for wallet_address in wallet_addresses:
        # Perform your calculations and checks
        file_counter += 1
        if total_wallet_pnl > 65 and winning_percentage > 65 and avg_buys_per_token <= 1.5 and quick_trade_percentage <= 15:
            # Append the qualifying wallet address to the DataFrame
            qualifying_wallets = qualifying_wallets.append({'WalletAddress': wallet_address}, ignore_index=True)
    
    # Save the qualifying wallet addresses to a CSV file
    try:
        qualifying_wallets.to_csv('C:\\Users\\dan\\PycharmProjects\\PnlBotGukesh\\OurPnlBot\\getourpnl.csv', mode='w', header=True, index=False)
    except Exception as e:
        print(f"Error while saving wallet addresses to CSV file: {e}")


def process_wallet_pnl(csv_file_2, total_wallet_pnl, winning_percentage, avg_buys_per_token, quick_trade_percentage, file_counter, start_date, end_date, win_rate, average_buy_size, avg_time_held_str, avg_trades_per_day, df_spl_transactions, winning_days, losing_days, sorted_tokens_by_pnl, daily_pnl, file_counter_path, losing_percentage):
  # Read the wallet addresses from the CSV file
  df_wallets = pd.read_csv(csv_file_2)
  wallet_addresses = df_wallets['wallet address'].unique()

  for wallet_address in wallet_addresses:
    # Perform your calculations and checks
    file_counter+=1
    if total_wallet_pnl > 65 and winning_percentage > 65 and avg_buys_per_token <= 1.5 and quick_trade_percentage <= 15:
      try:
        # Create a DataFrame and save it to a CSV file
        df = pd.DataFrame([wallet_address], columns=['WalletAddress'])
        df.to_csv('C:\\Users\\dan\\PycharmProjects\\PnlBotGukesh\\OurPnlBot\\getourpnl.csv', mode='w',
                  header=False, index=False)
      except Exception as e:
        print(f"Error while saving wallet address to CSV file: {e}")
