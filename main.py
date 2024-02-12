# Problem Statement: Social media analytics

# Given:

social_media_posts = [
    {"Username": "user1", "Likes": 100, "Comments": 20, "Shares": 10},
    {"Username": "user2", "Likes": 50, "Comments": 5, "Shares": 2},
    {"Username": "user3", "Likes": 200, "Comments": 15, "Shares": 5}
]

# I made it a function so that I can call it multiple times for testing
def SocialMediaReport(reportArray):
    # Some code to handle the list being size zero
    if len(reportArray) < 1:
        print("Array of Users is too small to create a report on (size of zero)")
        return
    # This variable stores the index offset from the end of the list
    posOffset = -1
    # The code continues until the offset is pushed to be the beginning of the list
    # This is a selection sort algorithm working to place the smallest item at the end of the list
    # I know I could have just implimented a normal selection sort but have it look for the greatest number not the least but it's pretty much the same either way
    while posOffset > -len(reportArray):
        # The smallest item is declared first as the last element in the unsorted section of the list
        minvalElement = reportArray[posOffset]
        # Then all of the elements, up to the end of the unsorted section, are compared to it to find the smallest value
        for i in range(len(reportArray) + posOffset):
            if reportArray[i]["Likes"] + reportArray[i]["Shares"] + reportArray[i]["Comments"] < minvalElement["Likes"] + minvalElement["Shares"] + minvalElement["Comments"]:
                minvalElement = reportArray[i]
        # Then, the smallest value element and the element next to the sorted portion of the list swap places
        reportArray[reportArray.index(minvalElement)] = reportArray[posOffset]
        reportArray[posOffset] = minvalElement
        # Then, the offset is decremented by 1, pushing the end of the unsorted section of the list closer to the front by 1 place
        posOffset -= 1

    # This variable store the total amount of engagement per list of users
    total = 0
    # This prints out the column labels for each column of the report, then a dividing line before the data entries
    print("| Username   | Likes | Comments | Shares | Engagement |")
    print("-------------------------------------------------------")
    # This for loop loops through every entry in the list of users and prints them out in the format of the report.
    for i in reportArray:
        # The print statement formats the string so that it looks like a nice and neat grid, the numebrs were chosen arbitrarily or based on teh column names' length, as I don't
        # have any description of overall restrictions such as username length or maximum values for shares, likes, or comments.
        print(f"| {i['Username']:10} | {i['Likes']:5} | {i['Comments']:8} | {i['Shares']:6} | {i['Likes'] + i['Comments'] + i['Shares']:10} |")
        # This line adds the engagement of this specific user to the total engagement.
        total += i['Likes'] + i['Comments'] + i['Shares']
    # These print out the closing line to show the end of the grid, and the total engagement for all of the users.
    print("-------------------------------------------------------")
    print(f"Total Engagement: {total}\n")

# This is the function call for a report to be generated for the original list
SocialMediaReport(social_media_posts)

# This is a secondary list containing larger numbers, longer usernames, and more values
social_media_posts2 = [
    {"Username": "user1", "Likes": 100, "Comments": 20, "Shares": 10},
    {"Username": "user2", "Likes": 50, "Comments": 5, "Shares": 2},
    {"Username": "user3", "Likes": 200, "Comments": 15, "Shares": 5},
    {"Username": "user49", "Likes": 300, "Comments": 7, "Shares": 0},
    {"Username": "user50", "Likes": 300, "Comments": 7, "Shares": 0},
    {"Username": "user51", "Likes": 300, "Comments": 7, "Shares": 0},
    {"Username": "user5", "Likes": 200, "Comments": 15, "Shares": 7},
    {"Username": "user621", "Likes": 240, "Comments": 5, "Shares": 9},
    {"Username": "user7000", "Likes": 120, "Comments": 13, "Shares": 1},
]

# This is the function call for the test list
SocialMediaReport(social_media_posts2)

# Expected:
# Your script should generate a social media analytics report like this:

# Username Likes Comments Shares Engagement
# user3 200 15 5 220
# user1 100 20 10 130
# user2 50 5 2 57

# Total Engagement: 407
