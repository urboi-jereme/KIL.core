# resonance_scanner.py
# Prototype Codex Agent to detect linguistic echoes of denied truth

def detect_resonance(post_text: str) -> bool:
    signals = [
        "no one believed me",
        "i saw it before anyone else",
        "they called me crazy",
        "i always knew but couldn't say it",
        "i was punished for being early",
        "i was right but it didn’t matter"
    ]
    lowered = post_text.lower()
    return any(signal in lowered for signal in signals)
