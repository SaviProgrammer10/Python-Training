# Classroom Points Calculator

# Store team points
team1 = 85
team2 = 92
team3 = 78

# Display points
print("Team 1 Points:", team1)
print("Team 2 Points:", team2)
print("Team 3 Points:", team3)

# Calculate total points
total_points = team1 + team2 + team3
print("\nTotal Points:", total_points)

# Calculate average points
average_points = total_points / 3
print("Average Points:", average_points)

# Pack reward stars into boxes
reward_stars = total_points
stars_per_box = 10

full_boxes = reward_stars // stars_per_box
remaining_stars = reward_stars % stars_per_box

print("\nReward Stars:", reward_stars)
print("Full Boxes:", full_boxes)
print("Remaining Stars:", remaining_stars)

# Compare scores with last week
last_week_total = 240

print("\nComparison with Last Week:")
print("Current Total:", total_points)
print("Last Week Total:", last_week_total)

print("Current > Last Week:", total_points > last_week_total)
print("Current < Last Week:", total_points < last_week_total)
print("Current == Last Week:", total_points == last_week_total)

# Update totals using assignment operators
bonus_points = 15

print("\nUpdating Total Points...")
total_points += bonus_points
print("After Adding Bonus:", total_points)

total_points -= 5
print("After Penalty:", total_points)

total_points *= 2
print("After Double Points:", total_points)

total_points //= 3
print("After Dividing Among 3 Groups:", total_points)