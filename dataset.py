"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "No cap, this is actually pretty good",
    "Why does everything have to be so hard?",
    "Lowkey stressed but highkey proud of myself",
    "I absolutely love getting stuck in traffic",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

# Added 5-10 more posts and labels with variety in language styles

SAMPLE_POSTS.append("No cap, this is actually pretty good")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("Why does everything have to be so hard?")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("Lowkey stressed but highkey proud of myself")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("I absolutely love getting stuck in traffic :)")
TRUE_LABELS.append("negative")  # sarcasm

SAMPLE_POSTS.append("Feeling 💀 but also 😂 vibes")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("This project is amazing, I hate that I love it")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("Just another day, nothing special :/")
TRUE_LABELS.append("neutral")

SAMPLE_POSTS.append("Can't believe how awesome that turned out!")
TRUE_LABELS.append("positive")
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
