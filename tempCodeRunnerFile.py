f generate_star_rating(percentage):
    # Ensure percentage is within the range [0, 100]
    percentage = max(0, min(100, percentage))
    
    # Convert percentage to a rating out of 5
    rating = round(percentage / 20)
    
    # Print the star rating using ASCII art
    print("Star Rating:")
    print("*" * rating + " " * (5 - rating))

# Example usage
user_percentage = float(input("Enter the percentage (0 to 100): "))
generate_star_rating(user_percentage)