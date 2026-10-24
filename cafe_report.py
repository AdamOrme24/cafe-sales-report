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
daily_takings.append(298.60)  # Adding Sunday takings to the daily takings 

#Sales Figures
total = sum(daily_takings)
average = total / len(daily_takings)
best = max(daily_takings)
worst = min(daily_takings) 
worst_day = days[daily_takings.index(worst)]
top_three_days = sorted(zip(daily_takings, days), reverse=True)[:3]  # Get top three days with highest takings
vat_included = round(total - (total / (1 + vat_rate)), 2)  # Calculate VAT included in total takings

print(f"Total Takings: £{total:.2f}")
print(f"Average Daily Takings: £{average:.2f}")
print(f"Best Day: {days[daily_takings.index(best)]} with £{best:.2f}")
print(f"Worst Day: {worst_day} with £{worst:.2f}")
print(f"Top Three Days: {', '.join([f'{day} (£{takings:.2f})' for takings, day in top_three_days])}")
print(f"VAT Included in Total Takings: £{vat_included:.2f}")

#What Items Sold
items_sold = ["latte", "croissant", "sandwich", "tea", "muffin", "latte", "flat white", "muffin", "tea"]
lattes = items_sold.count("latte")
unique_items = len(set(items_sold))  # Get unique items sold
featured = ("Oat Latte", "coffee", 3.40)  # product record: name, category, price
name, category, price = featured

print("-" * 40)
print(f"Lattes sold:      {lattes} of {len(items_sold)} items")
print(f"Different items:  {unique_items}")
print(f"Featured product: {name} ({category}) at £{price:.2f}")

#Customer Insights

loyalty_members = ['Amy', 'Ben', 'Charlie', 'Diana', 'Ethan']
weekday_customers = ['Fiona', 'George', 'Hannah']
weekend_customers = ['Fiona', 'Harvey', 'Ian', 'Jack', 'Charlie', 'Diana']  # Charlie and Diana are weekend customers
members_to_win_back = ['John', 'Kylie', 'Liam']
open_on_sunday_next_week = True  # Café will be open on Sunday next week
came_on_any_day = set(weekday_customers) & set(weekend_customers)

print("-" * 40)
print(f"Weekday Customers: {', '.join(weekday_customers)}")
print(f"Weekend Customers: {', '.join(weekend_customers)}")
print(f"Came on Weekend and Weekday: {', '.join(came_on_any_day) if came_on_any_day else 'None'}")
print(f"Loyalty Members: {', '.join(loyalty_members)}")
print(f"Members to Win Back: {', '.join(members_to_win_back)}")
print(f"Open on Sunday Next Week: {'Yes' if open_on_sunday_next_week else 'No'}")