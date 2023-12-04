import requests

def get_elements():
    # Download a list of chemical elements from the internet
    url = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        elements_data = response.json()["elements"]
        return [element["name"].lower() for element in elements_data]
    else:
        print("Failed to fetch element data. Please check your internet connection.")
        exit()

def find_longest_sequence(current_element, elements, sequence=[]):
    # Base case: no elements starting with the last letter of the current element
    if not any(element.startswith(current_element[-1]) for element in elements):
        return sequence
    
    # Recursive case: find the next element in the sequence
    next_elements = [element for element in elements if element.startswith(current_element[-1])]
    
    max_sequence = sequence
    for next_element in next_elements:
        if next_element not in sequence:
            new_sequence = find_longest_sequence(next_element, [element for element in elements if element != next_element], sequence + [next_element])
            if len(new_sequence) > len(max_sequence):
                max_sequence = new_sequence
    
    return max_sequence

def main():
    elements = get_elements()
    
    # Get user input for the starting element
    user_input = input("Enter the name of an element: ").lower()
    
    if user_input not in elements:
        print("Invalid element name. Please enter a valid element.")
        return
    
    longest_sequence = find_longest_sequence(user_input, elements)
    
    print("Longest sequence:")
    for element in longest_sequence:
        print(element)

if __name__ == "__main__":
    main()
