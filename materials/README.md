# Materials

* Folder [audio](https://github.com/AnnaZhuravleva/novel_words/tree/master/materials) contains audio recordings of all the PW stimuli

* Folder [exp_lists](https://github.com/AnnaZhuravleva/novel_words/tree/master/materials/exp_lists) contains all the experimental lists used for the experiment.
  * Files session_1_X.xlsx should be used in the acquisition phase, immediate and delayed testing phases on the first set of 40 words.
  * Files session_2_X.xlsx should be used in the acquisition phase, immediate and delayed testing phases on the second set of 40 words.
  * X in the file names corresponds to the variant.
  
* Folder [instructions](https://github.com/AnnaZhuravleva/novel_words/tree/master/materials/instructions) contains the instructions sent for participants

* File [stimuli.xlsx](https://github.com/AnnaZhuravleva/novel_words/blob/master/materials/stimuli.xlsx) contains all the stimuli prepared for the experiment.
  * List **"AL"** contains all the pseudowords used in the experiment
    * 'mean_distance' parameter corresponds to the mean Levenshtein distance from participants' transcription to correct transcription in the online validation experiment Stupina & Chrabaszcz (2020)
    * 'count' parameter correspons to the number of participants scored the particular word
    * 'valency' parameter corresponds to participants' score on the pleasantness or unpleasantness of the stimulus on the scale -2 to 2
    * 'unique_associations' parameter corresponds to the real-word associations of participants' elicited by the particular pseudoword
    * 'associations_sum' parameter corresponds to the number of participants reported the real-word associations to the particular stimulus
    
  * List **L1** contains the information about all the L1 stimuli used in the experiment.
    * Parameters of the L1 stimuli are described [here](http://stimdb.ru)
    * 'sim_score_mean', 'sim_score_max', 'sim_score_sd' parameters correspond to the mean/max/sd vector similarities between the vector of the particular word and vectors of all other words in the list. Vector similarity was measured by [word2vec](https://rusvectores.org/ru/about/)
    
  * List **AL_set1** contains pseudowords (and their parameters) used in the first acquisition session. Mean values of all parameters are presented below the word list
  
  * List **AL_set2** contains  pseudowords (and their parameters) used in the second acquisition session. Mean values of all parameters are presented below the word list  
  
  * List **sim_scores** contains parwise vector similarity scores of all L1 stimuli
  
  * List **L1_set1** contains L1 stimuli (and their parameters) used in the first acquisition session. Mean values of all parameters are presented below the word list
  
  * List **L1_set2** contains L1 stimuli (and their parameters) used in the second acquisition session. Mean values of all parameters are presented below the word list
  
  * List **AFC_1** and **AFC_2** contain the stimuli for 3-alternatove-forced-choice task on the words from the first set (AL_set1, L1_set1) and second set (AL_set2, L1_set2)
    * 'dominant_name' - correct answer
    * 'AFC1', 'AFC2' - distractors
    * 'chosen_distance_word_to_1' - vector similarity score between correct answer and the first distractor
    * 'chosen_distance_word_to_2' - vector similarity score between correct answer and the second distractor
    * 'chosen_distance_1_to_2' - vector similarity score between two distractors
    
  * List **afc_stats**: 
    * how many times was used as a distractor in the 3AFC task (for a single word)
    * How many times the words were used together, so that any of them was a correct answer, and the other was a distractor (for a pair of words)
    
  * List **sets** contains general information about first and second stimuli sets
