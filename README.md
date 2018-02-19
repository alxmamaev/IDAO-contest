# IDAO-contest
Higher School of Economics, Yandex and Sberbank along with Harbour.Space University are proud to announce an olympiad created by and for data analysts. 

![](https://github.com/alxmamaev/image-storage/blob/master/idao/OMat3J6MrS0.jpg)


## Track-1
Human behaviour isn’t governed by the rules of logic. It tends to defy even the shrewdest predictions, so successfully forecasting the future desires of just a small fraction of users would be a major achievement. Your task is having a browsing history of a large number of users to select a small sample group — 5% of users — and recommend ﬁve product categories for each person. At least one of these picks must be something that doesn’t interest the user right now, but will interest them during the next week.

#### Evaluation
The task is to choose exactly 53,979 users (user_id, 5% of all users in the dataset) and for each select ﬁve third-level product categories (id3) that they have not viewed in the last three weeks and which will be of interest to them in the next seven days. The resulting score is based on the number of users for which at least one product category is correctly nominated. Accurate predictions of two or more categories for one user will not improve your score.
![](https://github.com/alxmamaev/image-storage/blob/master/idao/eval.png)

#### Input format
Input format
You will be working with Yandex.Market search logs. Each row in the data corresponds to a "view" event: a particular user viewed an item that belongs to a particular category.
The data is stored in a .csv ﬁle with the following ﬁelds:

*user_id* — individual shopper identiﬁer
*date* — the day when user’s interest in a particular product was recorded; from 1 to 54
*id1* — ﬁrst (highest) level category identiﬁer, e.g. “Home appliances”.
*id2* — second (middle) level category identiﬁer, e.g. “Kitchen appliances”.
*id3* — third (lowest) level category identiﬁer, e.g. “Refrigerators”.
The data can be downloaded using this [link](https://www.dropbox.com/s/v71xw29hqt4qykb/train.csv.zip?dl=1).

#### Output format
Please upload your predictions into the system in the `.csv` format. The ﬁle should consist of 53,979 + 1 rows and contain columns user_id, id3_1, id3_2, id3_3, id3_4, id3_5. 
A sample submission can be found [here](https://github.com/DmitryUlyanov/IDAO).

---


### Track-2
In this task you need to create program, that wiil be solve first task for 5k users. You need to upload your program in `.zip` file into contest platform.

#### Output format
You need to submit a .zip archive that includes a Makeﬁle with tags "build" and "run" that will be executed one after another in a container. The log, produced during "build" phase will be visible on the submission page, so it is possible to debug the installation. For the "Run" phase your code should process the data stored in ./train.csv.zip and is expected to produce a ./submission.csv ﬁle with predictions.
The submission ﬁle should consist of 5000 + 1 rows and contain columns user_id, id3_1, id3_2, id3_3, id3_4, id3_5.

#### Using Python
The container has python 2.7/3.6 installed with the major libraries:

* numpy
* scipy
* pandas
* scikit-learn
* matplotlib
* joblib
* tqdm
* xgboost
* lightgbm
* catboost
