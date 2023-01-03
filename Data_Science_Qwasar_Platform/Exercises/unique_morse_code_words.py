def unique_morse_code_words(words) -> int:
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    transformations = set()

    for word in words:
        transformation = ''.join(morse[ord(c) - ord('a')] for c in word)
        transformations.add(transformation)

    return len(transformations)

print(unique_morse_code_words(["gin", "zen", "gig", "msg"]))