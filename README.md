# Bean & Brew Weekly Sales Report

A one-screen end-of-week sales report for a small café, written in plain Python.

## The business problem

Every Monday, the owner of Bean & Brew wants a quick summary of last week: how much the café took, which days were busiest and quietest, how much VAT is included in the takings, what sold, and who the customers were. This script prints all of that in one report.

## Example output

```text
End-of-Week Sales Report for Bean & Brew - Week 1

========================================
Bean & Brew Sales Report | Week 1
========================================
Total Takings: £3387.55
Average Daily Takings: £483.94
Best Day: Sat with £710.10
Worst Day: Sun with £298.60
Top Three Days: Sat (£710.10), Fri (£620.40), Thu (£501.75)
VAT Included in Total Takings: £564.59
----------------------------------------
Lattes sold:      2 of 9 items
Different items:  6
Featured product: Oat Latte (coffee) at £3.40
----------------------------------------
Weekday Customers: Fiona, George, Hannah
Weekend Customers: Fiona, Harvey, Ian, Jack, Charlie, Diana
Came on Weekend and Weekday: Fiona
Loyalty Members: Amy, Ben, Charlie, Diana, Ethan
Members to Win Back: John, Kylie, Liam
Open on Sunday Next Week: Yes
```

<img width="940" height="752" alt="image" src="https://github.com/user-attachments/assets/fa25dd9e-98a7-43ad-8cf3-c0590a3f9967" />

## How to run it

You need Python 3.10 or newer. No extra packages are required.

```bash
python cafe_report.py
```

## Python skills shown

| Skill | Where it's used |
| --- | --- |
| Basic syntax | Comments split the script into sections; `print()` with f-strings builds every line of the report; `"=" * 40` and `"-" * 40` draw dividers using string repetition |
| Variables and data types | Business settings use a `str` (café name), an `int` (week number), a `float` (VAT rate) and a `bool` (open on Sunday); money values are floats formatted with `:.2f` |
| Lists | `daily_takings` grows with `.append()` for the Sunday pop-up; `sum()`, `len()`, `max()`, `min()` and `.index()` work out the sales figures; `sorted()` and slicing pick the top three days; `.count()` counts lattes sold |
| Tuples | `days` is a tuple because the days of the week are fixed, and Sunday is added by building a new tuple with `+ ("Sun",)`; the featured product is a tuple unpacked into `name, category, price`; `zip()` pairs each day's takings with its name as tuples |
| Sets | `set(items_sold)` removes repeats to count the different items sold; `&` (intersection) finds customers who came on both weekdays and weekends |

## About

Built as my first Python portfolio project, while working through the [roadmap.sh Python roadmap](https://roadmap.sh/python).
