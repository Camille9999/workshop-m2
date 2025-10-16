# spell_matcher.py
from difflib import get_close_matches
from harry_potter_spells import SPELLS

def detect_spell(transcription, cutoff=0.1):
    matches = get_close_matches(transcription, SPELLS, n=1, cutoff=cutoff)
    return matches[0] if matches else None

if __name__ == "__main__":
    # Example usage
    transcription = input("Enter transcribed text: ")
    spell = detect_spell(transcription)
    if spell:
        print(f"Detected spell: {spell}")
    else:
        print("No spell detected.")
