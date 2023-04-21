num_trades = int(input("Enter the number of trades: "))
outcomes = []
pl = []
risk = 100
reward = 250
capital = float(input("Enter your starting capital: "))

for i in range(num_trades):
    outcome = input(f"Enter the outcome for trade {i+1} (win/loss): ")
    outcomes.append(outcome)
    if outcome == 'win':
        pl.append(reward - risk)
        capital += reward
    else:
        pl.append(-risk)
        capital -= risk

print("Trade outcomes: ", ' '.join(outcomes))
print("P/L per trade:  ", ' '.join(['${:.2f}'.format(p) for p in pl]))
print(f"Total trades: {num_trades}")
print(f"Win rate: {outcomes.count('win')/num_trades*100:.2f}%")
print(f"Total P/L: ${sum(pl):.2f}")
print(f"Final capital: ${capital:.2f}")
