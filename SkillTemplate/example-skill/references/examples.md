# Text Statistics Examples

## Example 1: Simple Blog Post

**Input:**
```
Technology moves fast. New frameworks appear daily. Developers struggle to keep up.
The solution isn't learning everything. It's learning fundamentals well.
```

**Output:**
```
TEXT STATISTICS REPORT
=====================

Basic Metrics:
- Word Count: 24 (23 unique)
- Character Count: 151 (127 without spaces)
- Reading Time: <1 minute

Complexity:
- Avg Sentence Length: 6 words
- Long Words (7+ chars): 29%
- Vocabulary Richness: 96%

Readability:
- Flesch Score: 83/100 (Easy)
- Grade Level: 4-5

Interpretation:
Very simple, accessible text. Short sentences make it easy to read.
High vocabulary uniqueness shows no repetition despite brevity.
```

## Example 2: Academic Abstract

**Input:**
```
The implementation of distributed consensus algorithms in heterogeneous
network environments presents significant challenges with respect to
fault tolerance, latency optimization, and Byzantine failure detection.
This paper proposes a novel approach utilizing vector clocks and quorum-based
validation to achieve eventual consistency while maintaining acceptable
performance characteristics under adverse conditions.
```

**Output:**
```
TEXT STATISTICS REPORT
=====================

Basic Metrics:
- Word Count: 56 (51 unique)
- Character Count: 424 (368 without spaces)
- Reading Time: <1 minute

Complexity:
- Avg Sentence Length: 28 words
- Long Words (7+ chars): 64%
- Vocabulary Richness: 91%

Readability:
- Flesch Score: 14/100 (Very Difficult)
- Grade Level: College+

Interpretation:
Highly technical, complex text requiring specialized knowledge.
Long sentences and technical vocabulary make it challenging for
general readers. Appropriate for academic/expert audience only.
```

## Example 3: Children's Story

**Input:**
```
The cat sat on the mat. She looked at the bird. The bird was blue.
It sang a happy song. The cat smiled and slept in the warm sun.
```

**Output:**
```
TEXT STATISTICS REPORT
=====================

Basic Metrics:
- Word Count: 32 (24 unique)
- Character Count: 134 (102 without spaces)
- Reading Time: <1 minute

Complexity:
- Avg Sentence Length: 6 words
- Long Words (7+ chars): 6%
- Vocabulary Richness: 75%

Readability:
- Flesch Score: 97/100 (Very Easy)
- Grade Level: 1-2

Interpretation:
Extremely simple text, perfect for early readers. Very short sentences
and simple vocabulary. Almost no complex words. Ideal for children.
```
