# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a uniform list of tokens.

        - strips whitespace
        - lowercases
        - removes punctuation
        - splits on whitespace
        """
        import re

        cleaned = text.strip().lower()

        # Replace punctuation with spaces (keeps emojis since they're not removed by \w)
        cleaned = re.sub(r"[^\w\s'\u2600-\u27BF]+", " ", cleaned)

        # Split by whitespace and drop empty tokens
        tokens = [token for token in cleaned.split() if token]

        # debug output to confirm behavior
        print(f"[preprocess] input={text!r}, tokens={tokens}")

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        Simple improvement:
          - use token frequency (multiple matches count multiple times)
          - support basic negation inversion for next token ("not happy")
        """
        tokens = self.preprocess(text)
        score = 0

        negation_tokens = {"not", "never", "no", "can't", "cannot", "dont", "don't", "won't", "wont"}
        negate_next = False

        for token in tokens:
            if token in negation_tokens:
                negate_next = True
                continue

            increment = 0
            if token in self.positive_words:
                increment = 1
            elif token in self.negative_words:
                increment = -1

            if negate_next:
                increment *= -1
                negate_next = False

            score += increment

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        We also keep a "mixed" label for near-zero sentiment with both
        positive and negative terms.
        """
        score = self.score_text(text)

        if score > 0:
            return "positive"
        if score < 0:
            return "negative"

        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
