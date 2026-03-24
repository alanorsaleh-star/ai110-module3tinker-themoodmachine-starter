# The Mood Machine

The Mood Machine is a simple text classifier that begins with a rule based approach and can optionally be extended with a small machine learning model. It tries to guess whether a short piece of text sounds **positive**, **negative**, **neutral**, or even **mixed** based on patterns in your data.

## Summary

In this lab, I worked on the "The Mood Machine," a text-based mood classifier that predicts whether short pieces of text convey positive, negative, neutral, or mixed emotions. It started with a rule-based approach, implementing preprocessing to clean and tokenize text, scoring mechanisms based on positive and negative word lists, and prediction logic to classify moods. To make it more robust, I expanded the dataset with additional examples, including slang, emojis, and sarcastic content.

I evaluated the rule-based system on sample data, carefully observing its strengths and weaknesses, and explored edge cases where it might fail. For comparison, I implemented a simple machine learning model using scikit-learn, training it on the same dataset and analyzing how its performance differed from the rule-based method.

Throughout the process, I reflected on key concepts like data quality, model fairness, accuracy trade-offs, and the importance of testing with diverse examples. I documented my findings, limitations, and potential improvements in the model card, gaining hands-on experience with how small design choices in data and algorithms can significantly impact model behavior.

This project gave me practical insights into building and evaluating simple AI systems, emphasizing the value of iterative experimentation and critical thinking about AI ethics and reliability.
