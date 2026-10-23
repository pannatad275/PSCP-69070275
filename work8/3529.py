'''caesarv2'''
ciphertext = input()

common_words = {
    "what", "when", "why", "which", "this", "there", "where", 
    "the", "is", "am", "are", "you", "we", "they", "he", "she", "it"
}

best_text = ciphertext
max_score = -1

for shift in range(26):
    decoded = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            decoded += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            decoded += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decoded += char
    words = decoded.lower().split()
    cleaned_words = [w.strip(".,!?;:\"'()[]{}") for w in words]
    score = sum(1 for w in cleaned_words if w in common_words)
    if score > max_score:
        max_score = score
        best_text = decoded
print(best_text)
