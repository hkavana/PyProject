import datetime

name = ["Kavana","Sanjana"]
amt = [123.99,234.55]

msg = """
Hi {name}!

Thank you for your purchase of ${amt} on {date}.

Team Wal-Mart
"""

def disp_msg(names,amount):
    new_msg = []
    if len(names) == len(amount):
        i = 0
        for name in names:
            new_msg = msg.format(
                    name = names[i],
                    amt = amount[i],
                    date = datetime.date.today()
            )
            print(new_msg)
            i = i + 1

disp_msg(name,amt)
