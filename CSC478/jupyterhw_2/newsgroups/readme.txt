The dataset is a subset of the 20 newsgroup corpus http://qwone.com/~jason/20Newsgroups/  in term-document format. This subset has been taken from http://mlg.ucd.ie/content/view/22/ (this data was modified to remove terms that did not appear in any of the documents). Each document belong to one of the two classes {Windows, Hockey}. The original data has been divided into test and train (20%, 80%) subsets.

The files contained in the archive file are as follows:

1. trainMatrixModified.txt: the term-document frequency matrix for the training documents. Each row of this matrix corresponds to one the terms and each column corresponds to one the documents and the (i,j)th element of the matrix shows the frequency of the ith term in the jth document. This matrix contains 5500 rows and 800 columns.

2. testMatrixModified.txt: the term-document frequency for the test documents. The matrix contains 5500 rows and 200 columns.

3. trainClasses.txt: This file contains the labels associated with each training document. Each line is in the format of documentIndex \t classId where the documentIndex is in the range of [0,800) and refers to the index of the document in the term-document frequency matrix for train documents. The classId refers to one of the two classes and takes one of the values 0 (for Windows) or 1 (for Hockey).

4. testClasses.txt: This file contains the labels associated with each test document. Each line is in the format of documentIndex \t classId where the documentIndex is in the range of [0,200) and refers to the index of the document in the term-document frequency matrix for test documents  

5. modifiedterms.txt: This file contains the set of 5500 terms in the vocabulary. Each line contains a term and corresponds to the corresponding rows in term-document frequency matrices. 

