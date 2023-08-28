# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

We use RandomForestClassifier from `scikit-learn`. All the hyperparameters are default parameters of the classifier.

## Intended Use

The model is used for classifying employees' salary into 2 groups are: <=50K and >50K.

## Training Data

Publicly available `Census Bureau` dataset is used for training and evaluating the model.

For both training and evaluation, categorical features of the data are encoded using OneHotEncoder and the target is transformed using LabelBinarizer

## Evaluation Data

The original dataset is preprocessed and then split into training and evaluation data with evaluation data size of 80/20 ratio

## Metrics

The model achieves the following result:  
precision: 0.7307410124724871, recall: 0.6221111805121798, fbeta: 0.6720647773279352

## Ethical Considerations

The misuse of these census information can cause consequences to the lives of people surveyed and (possibly) other people in some related populations

## Caveats and Recommendations

The model was trained on data of people mostly from the USA. 
Hence it is not recommended to use the model to predict the salary type for people from other regions in the world.