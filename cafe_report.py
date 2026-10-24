# This is an end-of-week sales report for a small café called Bean & Brew.

# Business Settings
cafe_name = "Bean & Brew"
week_number = 1
vat_rate = 0.20  # 20% VAT
open_on_sunday = False  # Café is closed on Sundays

# Title
print(f"End-of-Week Sales Report for {cafe_name} - Week {week_number}\n")

#Report Header
print("=" * 40)
print(f"{cafe_name} Sales Report | Week {week_number}")
print("=" * 40)

#Days and Takings
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat") #Tuple of days the café is open
daily_takings = [412.50, 389.20, 455.00, 501.75, 620.40, 710.10] #List of daily takings for each day the café is 

#Sunday pop-up day: one-off stall at the local market
days = days + ("Sun",)  # Adding Sunday to the days tuple for the pop-up day
daily_takings.append(298.60)  # Adding Sunday takings to the daily takings list