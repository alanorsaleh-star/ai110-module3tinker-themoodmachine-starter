# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

## 1. Model Overview

**Model type:**  
I used the rule-based model only in this project. Implementation and evaluation are focused on the rule-based approach.

**Intended purpose:**  
Recognize mood sentiment from short text posts and classify as `positive`, `negative`, or `neutral` (with dataset labels including `mixed` for some cases).

**How it works (brief):**  
The rule-based pipeline does:
- Tokenize normalized text (lowercase, punctuation removal, whitespace split).
- Use lexical sentiment lists (from `dataset.py`) for positive and negative word matches.
- Apply simple negation (one-token inversion for words like `not`, `never`, `no`, `can't`).
- Compute score via token counts and map to label thresholds.

## 2. Data

**Dataset description:**  
`SAMPLE_POSTS` has 14 posts (6 initial examples + 8 appended). The data includes a mix of direct sentiment, sarcasm, slang, and emoji cases.

**Labeling process:**  
Labels in `TRUE_LABELS` come from manual human interpretation of each phrase. Posts were labeled for intent; mixed and sarcastic lines were marked as `mixed` or `negative` depending on context.

**Important characteristics of your dataset:**  
- Slang: "no cap", "lowkey", "highkey"
- Emoji/symbols: ":)", "💀", "😂", ":/"
- Mixed sentiments: "Feeling tired but kind of hopeful", "This project is amazing, I hate that I love it"
- Sarcasm: "I absolutely love getting stuck in traffic"

**Possible issues with the dataset:**  
- Small scale (14 items) makes accuracy estimates noisy.
- Label imbalance toward positive and negative.
- Subjectivity in mixed/sarcastic messages.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
- Positive words gain +1 per token.
- Negative words lose -1 per token.
- Shouting, punctuation, or emoji are not directly scored (only tokenized text matters).
- Negation tokens invert the following sentiment token once.
- `predict_label` mapping: score > 0 → `positive`, score < 0 → `negative`, score == 0 → `neutral`.

**Strengths of this approach:**  
- Transparent decisions and easy to debug.
- Works well for explicit emotional words.
- Negation handling improves some phrases like "not good".

**Weaknesses of this approach:**  
- Fails to detect sarcasm and implicit sentiment.
- Mixed mood posts are often misclassified as one side.
- Limited vocabulary means unknown words are ignored.

## 4. How the ML Model Works (if used)

Not used or described for this card beyond acknowledgment that `ml_experiments.py` exists (that module trains scikit-learn models with vectorized text features on the same dataset).

## 5. Evaluation

**How you evaluated the model:**  
Used `main.py` evaluation path; the script runs every sample from `SAMPLE_POSTS` and compares to `TRUE_LABELS`.
Observed accuracy: ~0.39 on the full set.

**Examples of correct predictions:**  
1. "I love this class so much" -> `positive` (positive word `love`).
2. "Today was a terrible day" -> `negative` (negative word `terrible`).
3. "This is fine" -> `neutral` (no sentiment words).

**Examples of incorrect predictions:**  
1. "Feeling tired but kind of hopeful" -> predicted `negative` (only `tired` recognized, not `hopeful`).
2. "Why does everything have to be so hard?" -> predicted `neutral` (hard-coded negative terms missing). 
3. "I absolutely love getting stuck in traffic" -> predicted `positive` (sarcasm missed due to positive `love`).

## 6. Limitations

- Small dataset and limited linguistic coverage.
- Inability to detect nuance, sarcasm, or complex multi-word patterns.
- Rule-based dictionaries need frequent updates.
- evaluation on training data only; generalization untested.

## 7. Ethical Considerations

- Mood classification can mislead users and may harm mental-health suggestions if wrong.
- Cultural differences and slang may cause biased or incorrect predictions.
- Privacy concerns if model is used on personal message logs without consent.
- High-stakes contexts require human review and robust safeguards.

## 8. Ideas for Improvement

- Add more labeled examples and a held-out test set.
- Expand lexicons with emojis and slang terms.
- Add phrase patterns and multi-word context handling.
- Implement ML classifier and compare against rule-based on validation split.
- Introduce internal probability/confidence scoring for uncertain predictions.
- Add additional preprocessing (stemming, lemmatization, emoji normalization).

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).



## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only
