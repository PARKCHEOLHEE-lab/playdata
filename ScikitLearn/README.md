### 00 MachineLearning Keyword

#### `Overfitting (과적합)`
- 새로운 데이터를 예측하지 못함(학습이 너무 많이 되어버려 ___새로운 데이터를 예측하지 못함.___ 쉽게 말해서 배운 것만 잘함)
    
#### `Underfitting (과소적합)`
- 데이터들의 많은 공통된 특성들 중 일부만 학습하여 새로운 데이터를 쉽게 예측해버리는 것? ___(학습이 덜 된것이라고 이해할 수 있을것 같음)___
<br>

### 01 분류 모델(Classification Model) 평가

#### `Binary Classification(이진분류)에서 Positive(양성)과 Negative(음성)`
- 양성 : 예측하려는 대상
- 음성 : 예측하려는 대상이 아닌 것

#### `Confusion Matrix (혼동 행렬)`
- 
  |    |Predicted_Negative(0)|Predicted_Positive(1)|
  |------|---|---|
  |__Actual_Negative(0)__|TN(True Negative)|FP(False Positive)|
  |__Actual_Positive(1)__|FN(False Negative)|TP(True Positive)|
- True Negative : 음성으로 예측했는데 맞은 개수
- True Positive : 양성으로 예측했는데 맞은 개수
- False Negative : 음성으로 예측했는데 틀린 개수
- False Positive : 양성으로 예측했는데 틀린 개수
- `confusion_matrix`

#### `이진분류 평가점수`
- __Accuracy (정확도)__
  - 예측한 전체 데이터 중 올바르게 예측한 것의 비율로 평가 `accuracy_score`
  -  ___맞게 예측한 건수 ÷ 전체 예측한 건수___
  - 불균형 데이터의 경우에는 정확한 평가지표로 사용할 수 없음
  - 예를들어, 양성과 음성의 비율이 1:9인 경우 모든 예측을 음성으로 하면 정확도는 90%이기 때문

- __Recall or Sensitivity (재현율/민감도)__
  - 실제로 양성인 것중에 모델이 양성으로 예측한 것의 비율
  - ex) ___실제 스팸 메일 중 모델이 스팸 메일(양성)이라고 예측한 것의 비율___
  -  ___TPR(True Positive Rate)___ 이라고도 함

- __Precision (정밀도)__
  - 모델이 양성이라고 예측한 것 중 실제로 양성인 것의 비율
  - ex) ___모델이 스팸 메일(양성)이라고 예측한 것 중 실제로 스팸 메일인 것의 비율___
  -  ___PPV(Positive Predicted Value)___ 이라고도 함

- __F1 Score__
  - ~~Precision(정밀도)과 Recall(재현율)의 조화평균 점수~~
  - Precision(정밀도)과 Recall(재현율)의 수준이 비슷할 수록 F1 Score가 높아짐
  -  F1 Score를 근거로 Precision(정밀도)과 Recall(재현율)이 편향된 정도를 파악
