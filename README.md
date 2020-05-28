# Political-Tweets-Sentiment-Analysis


#### B.Sc Dissertation: Investigating the role of emotions and cognitive biases in political decision making through sentiment analysis of Twitter data using ML
 
 - Architecture choices:
      * Bidirectional LSTM - to determine polarity of a tweet
      * Bayesian inference - to analyze LSTM output and make predictions
     
 - Technologies used:
	 1. Data collection:
		 *  Tweepy - twitter API for data scraping
	 2. Data preprocessing:
		 * Pandas - handling large amounts of data
		 * Regex - general noise removal
		 * NLTK -  tokenization, stemming, lemmatization, stopword removal
		 * Glob - merging multiple csvs into one
  
   3. Data analysis:
	   * Numpy - handling high-dimensional mathematical operations
	   * sklearn - feature extraction and word embedding
	   * Keras - testing different architectures, picked Bidirectional LSTM after comparing accuracy of different models
	   * pymc3 - Bayesian Inference with NUTS sampler
