def count_characters():
    # Ask user for input
    sentence = input("Skriv en mening: ")
    
    # Count characters (including spaces)
    total_chars = len(sentence)
    
    # Count characters without spaces
    chars_without_spaces = len(sentence.replace(" ", ""))
    
    # Print results
    print(f"\nAntal tecken (inklusive mellanslag): {total_chars}")
    print(f"Antal tecken (exklusive mellanslag): {chars_without_spaces}")

if __name__ == "__main__":
    count_characters() 