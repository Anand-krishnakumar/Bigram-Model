# Bigram-Model

HOW TO RUN
-----------------------------------------------------
For Question 2: 
In command line in the orginal file directory:
$ python3 bigram.py


OUTPUT FILES:
------------------------------------------------------
For Question 2:
The program bigram.py generates 3 files once run:
1. noSmoothing.txt
2. addOneSmoothing.txt
3. goodTuringDiscounting.txt

These file contain the bigram probability and count for every bigram in the corpus based on the method used.

bigram.py also outputs the result of the testing sentence on the console.

HOW THE OUTPUT LOOKS:
---------------------------------------------------------------------------
Testing for Sentence:  The president wants to control the board 's control
No smoothing calculation...

Probability of  ('The', 'president')  is  0
Probability of  ('president', 'wants')  is  0
Probability of  ('wants', 'to')  is  0.5
Probability of  ('to', 'control')  is  0.0015408320493066256
Probability of  ('control', 'the')  is  0
Probability of  ('the', 'board')  is  0.1006993006993007
Probability of  ('board', "'s")  is  0.04644808743169399
Probability of  ("'s", 'control')  is  0
No smoothing:  0.0


Add one smoothing calculation...

Probability of  ('The', 'president')  is  0.00017774617845716317
Probability of  ('president', 'wants')  is  0.0001783166904422254
Probability of  ('wants', 'to')  is  0.0005349500713266762
Probability of  ('to', 'control')  is  0.0003513086246267346
Probability of  ('control', 'the')  is  0.00017838030681412772
Probability of  ('the', 'board')  is  0.023288147375738616
Probability of  ('board', "'s")  is  0.0031892274982282067
Probability of  ("'s", 'control')  is  0.00035354428142124803
Add one smoothing:  2.790008286494121e-26


Good Turing calculation...
Probability of  ('The', 'president')  is  0.5160443307757886
Probability of  ('president', 'wants')  is  0.5160443307757886
Probability of  ('wants', 'to')  is  3.424561752430911e-05
Probability of  ('to', 'control')  is  7.418169862907512e-06
Probability of  ('control', 'the')  is  0.5160443307757886
Probability of  ('the', 'board')  is  0.0
Probability of  ('board', "'s")  is  0.00046035805626598467
Probability of  ("'s", 'control')  is  0.5160443307757886
Good turing discounting probability:  0.0
