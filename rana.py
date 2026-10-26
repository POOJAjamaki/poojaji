import pykakasi

def main():
    # Create the Japanese text converter
    kks = pykakasi.kakasi()

    print("=" * 45)
    print("  JAPANESE KANJI TO HIRAGANA TRANSLATOR")
    print("=" * 45)
    print("Enter a Japanese word or sentence.")
    print("Type 'exit' to quit.")
    print("-" * 45)

    while True:
        try:
            text = input("\nEnter Japanese: ").strip()

            # Exit the program
            if text.lower() == "exit":
                print("Thank you for using the translator!")
                break

            # Check for empty input
            if not text:
                print("Please enter a Japanese word or sentence.")
                continue

            # Convert Japanese text to hiragana
            result = kks.convert(text)
            hiragana = "".join(
                item["hira"] for item in result
            )

            # Display the result
            print("\nOriginal Japanese:", text)
            print("Hiragana:", hiragana)

        except KeyboardInterrupt:
            print("\nTranslator closed.")
            break

        except Exception as error:
            print("An error occurred:", error)


if __name__ == "__main__":
    main()