# Fact Extraction and VERification
  ##I have forked/cloned this project from https://github.com/jongminyoon/fever.git

## Generic information from the   

This is a simplified version of a simplified version of the fever challenge.
There is no requirement to install the fever database for this project.
The evidence IDs querying into text files elminiating the need to for setting up a database for the classification task involving the gold labels has been created in this repository.


Input: Dev files with evidence sentences and labels (Large- 9,999 records and Small- 4920 records).
Output: Classification results for each labels
Model: Logistic Regression with Dictionary Vectorizer used in training

This project consists of the following important files:

1) final_runnable.py: This is the main entry point for the program. This file calls final_fever.py.

2) final_fever.py: This file we read from the reader, load the model and vectorizer, run the predictions and display the result.

3) finalized_model.sav : Pre-computed model

4) vectorizer.pk: Pre-computer vectorizer

5) dev_with_sents_yoon.jsonl: The original dev file taken from the project and converted into a new file of claims and evidence sentences for 9,999 records.

6) dev_yoon_small_sents.jsonl: We removed all the claims from the dataset that did not meet our threshold of bigrams and added to this file. This file consists of 4920 records.

7) utils.py: Original file from the forked project, no changes made. This file contains important helper functions.



## Installation


Install docker on your machine. 
Run this command first and wait for the container to build: 

docker build -f Dockerfile -t sandeep-suntwal-hw3:latest .

Once built, execute this command:

docker run --name fever-baseline -i sandeep-suntwal-hw3

## Results

Evaluation for Large file which has overlaps with train in bi-grams
In assessemt
Reading from dataset: 100%|██████████| 9999/9999 [18:46<00:00,  8.88examples/s]
model loaded
model result
                 precision    recall  f1-score   support

NOT ENOUGH INFO      0.362     0.326     0.343      3333
        REFUTES      0.426     0.012     0.023      3333
       SUPPORTS      0.337     0.698     0.455      3333

    avg / total      0.375     0.346     0.274      9999

Evaluation for testing file small file which has NO overlaps with train in bi-grams
In assessemt
Reading from dataset: 100%|██████████| 4920/4920 [06:21<00:00, 12.89examples/s]
model loaded
model result
                 precision    recall  f1-score   support

NOT ENOUGH INFO      0.417     0.347     0.379      1959
        REFUTES      0.302     0.011     0.021      1221
       SUPPORTS      0.354     0.661     0.461      1740

    avg / total      0.366     0.375     0.319      4920


Evaluation for testing file small file which has overlaps with train in bi-grams
In assessemt
Reading from dataset: 100%|██████████| 5079/5079 [03:36<00:00, 23.48examples/s]
model loaded
model result
                 precision    recall  f1-score   support

NOT ENOUGH INFO      0.298     0.296     0.297      1374
        REFUTES      0.529     0.013     0.025      2112
       SUPPORTS      0.322     0.739     0.449      1593

    avg / total      0.402     0.317     0.231      5079


### 3. RTE Training
We used logistic classifier with grid cross-validation for best hyperparamters. The details can be found in `fever_paper.pdf` in the folder `reports`.

##Results from the original fork by Yoon. We were not able to replicate this result. 

#### 1) Word-overlapping feature

|               | Precision | Recall | F1 score |
|:-------------:|:---------:|:------:|:--------:|
| Supported     | 0.337     | 0.798  | 0.455    |
| Refuted       | 0.426     | 0.012  | 0.023    |
| NEI           | 0.362     | 0.326  | 0.343    |
| avg / total   | 0.374     | 0.346  | 0.274    |

#### 2) Word cross-product feature

|               | Precision | Recall | F1 score |
|:-------------:|:---------:|:------:|:--------:|
| Supported     | 0.378     | 0.410  | 0.394    |
| Refuted       | 0.535     | 0.219  | 0.311    |
| NEI           | 0.339     | 0.527  | 0.420    |
| avg / total   | 0.421     | 0.385  | 0.375    |





          
