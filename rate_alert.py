usd_brl_rate = float(input("What's the USD/BRL rate today? "))

if usd_brl_rate < 5.00:
    print(f"{usd_brl_rate:.2f} -> Great rate! Buy dollars now.")
elif usd_brl_rate <= 5.50:
    print(f"{usd_brl_rate:.2f} -> Normal rate.")
else: 
    print(f"{usd_brl_rate:.2f} -> Dollar is expensive. Wait.")

print("Done.")