def main():
    # Initialize a dictionary with 10 countries and their capitals
    country_capitals = {
        "Japan": "Tokyo",
        "United States": "Washington, DC",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Scotland": "Edinburgh",
        "Canada": "Ottawa",
        "Armenia": "Yerevan",
        "Brazil": "Brasília"
    }

    while True:
        try:
            # Prompt the user for a country name
            country_name = input("Please enter a country to find its capital city: ")

            # Look up and print the capital city
            capital = country_capitals[country_name]
            print(f"The capital city of {country_name} is {capital}.")

        except KeyError:
            # If the country is not in the dictionary, print an error message
            print("Sorry, the country you are looking for is not in our directory.")

# Run the program
if __name__ == "__main__":
    main()
