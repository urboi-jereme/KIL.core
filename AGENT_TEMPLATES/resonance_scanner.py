# resonance_scanner.py (KIL Agent v0.1 placeholder)
# This Codex-ready agent monitors public platforms for linguistic echoes of denied truth.

def detect_resonance(post_text: str) -> bool:
    signals = [
        "no one believed me",
        "I saw it before anyone else",
        "they called me crazy",
        "I always knew",
        "I was punished for knowing"
    ]
    return any(signal in post_text.lower() for signal in signals)
