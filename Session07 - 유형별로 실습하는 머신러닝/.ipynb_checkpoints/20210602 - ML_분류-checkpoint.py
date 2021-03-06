{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 라이브러리 선언"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 데이터 처리 라이브러리\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 머신러닝 라이브러리\n",
    "from sklearn.svm import SVC ## 서포트 vector\n",
    "from sklearn.neighbors import KNeighborsClassifier # k neighbors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 데이터 전처리 라이브러리\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 클래시피케이션 matricx// 분류에 쓰이는 정확도 지표들 ->\n",
    "from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Classification -  SVM(soft vector machine) 마진에 따라 마진에 있는 데이터만 남기고 계산 ( 계산량이 줄어듬, 단 차원 증가시 계산량 증가)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 정확도와 속도로 알고리즘끼리 경합을 시킨다"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Classification - KNN 데이터로부터 가장 인접한 이웃개수의 그룹을 확인 후 편성"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 느리다"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터 불러오기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "csData = pd.read_csv(\"../dataset/customer.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>balance</th>\n",
       "      <th>stock</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30000000</td>\n",
       "      <td>22500000</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>280000000</td>\n",
       "      <td>48000000</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     balance     stock    label\n",
       "0   30000000  22500000   normal\n",
       "1  280000000  48000000  diamond"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csData.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### balance -> 예금 보유금액\n",
    "#### stock ->  주식 보유금색\n",
    "#### label -> 고객등급. normal, diamon, vip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     normal\n",
       "1    diamond\n",
       "4        vip\n",
       "Name: label, dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csData.label.drop_duplicates()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. 타입 통합 / 숫자형 컬럼 추가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "balance     int32\n",
       "stock       int32\n",
       "label      object\n",
       "dtype: object"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csData.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "csData = csData.astype({\"balance\" : \"int\", \"stock\" : \"int\", \"label\" : \"object\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "balance     int32\n",
       "stock       int32\n",
       "label      object\n",
       "dtype: object"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csData.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. 특성 선정"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 정답지\n",
    "labelColumn = \"label_new\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>balance</th>\n",
       "      <th>stock</th>\n",
       "      <th>LABEL_NEW</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>balance</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.565942</td>\n",
       "      <td>0.883144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stock</th>\n",
       "      <td>0.565942</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.824174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>LABEL_NEW</th>\n",
       "      <td>0.883144</td>\n",
       "      <td>0.824174</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            balance     stock  LABEL_NEW\n",
       "balance    1.000000  0.565942   0.883144\n",
       "stock      0.565942  1.000000   0.824174\n",
       "LABEL_NEW  0.883144  0.824174   1.000000"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## 상관계수 생성 함수는 숫자형 컬럼에 대해서만 상관계수를 계산한다. \n",
    "csData.corr() ## 관계를 알 수 없다. 라벨이 나오지 않았다..\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 라벨인코더는 원하는 값으로 맵핑하기가 힘들다. 딕셔너리는 원하는 값으로 맵핑 가능"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "labelMap = {\"normal\" : 0, \"diamond\" : 1, \"vip\" : 2 }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "csData[labelColumn] = csData.label.map(labelMap)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>balance</th>\n",
       "      <th>stock</th>\n",
       "      <th>LABEL_NEW</th>\n",
       "      <th>label_new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>balance</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.565942</td>\n",
       "      <td>0.883144</td>\n",
       "      <td>0.883144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stock</th>\n",
       "      <td>0.565942</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.824174</td>\n",
       "      <td>0.824174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>LABEL_NEW</th>\n",
       "      <td>0.883144</td>\n",
       "      <td>0.824174</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>label_new</th>\n",
       "      <td>0.883144</td>\n",
       "      <td>0.824174</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            balance     stock  LABEL_NEW  label_new\n",
       "balance    1.000000  0.565942   0.883144   0.883144\n",
       "stock      0.565942  1.000000   0.824174   0.824174\n",
       "LABEL_NEW  0.883144  0.824174   1.000000   1.000000\n",
       "label_new  0.883144  0.824174   1.000000   1.000000"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csData.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>balance</th>\n",
       "      <th>stock</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30000000</td>\n",
       "      <td>22500000</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>280000000</td>\n",
       "      <td>48000000</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>300000000</td>\n",
       "      <td>40666666</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>54000000</td>\n",
       "      <td>28000000</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>768000000</td>\n",
       "      <td>32000000</td>\n",
       "      <td>vip</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19995</th>\n",
       "      <td>628000000</td>\n",
       "      <td>44666666</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19996</th>\n",
       "      <td>276000000</td>\n",
       "      <td>20000000</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19997</th>\n",
       "      <td>652000000</td>\n",
       "      <td>41333333</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19998</th>\n",
       "      <td>676000000</td>\n",
       "      <td>45333333</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19999</th>\n",
       "      <td>732000000</td>\n",
       "      <td>26000000</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>20000 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         balance     stock    label\n",
       "0       30000000  22500000   normal\n",
       "1      280000000  48000000  diamond\n",
       "2      300000000  40666666  diamond\n",
       "3       54000000  28000000   normal\n",
       "4      768000000  32000000      vip\n",
       "...          ...       ...      ...\n",
       "19995  628000000  44666666  diamond\n",
       "19996  276000000  20000000   normal\n",
       "19997  652000000  41333333  diamond\n",
       "19998  676000000  45333333  diamond\n",
       "19999  732000000  26000000  diamond\n",
       "\n",
       "[20000 rows x 3 columns]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csData.drop(columns=[\"label_new\"],inplace=True)\n",
    "csData"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "corrDf = csData.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>balance</th>\n",
       "      <th>stock</th>\n",
       "      <th>label_new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>balance</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.565942</td>\n",
       "      <td>0.883144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stock</th>\n",
       "      <td>0.565942</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.824174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>label_new</th>\n",
       "      <td>0.883144</td>\n",
       "      <td>0.824174</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            balance     stock  label_new\n",
       "balance    1.000000  0.565942   0.883144\n",
       "stock      0.565942  1.000000   0.824174\n",
       "label_new  0.883144  0.824174   1.000000"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corrDf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "corrStd = 0.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "features = list (corrDf.loc[ (abs(corrDf[labelColumn]) > corrStd) & (corrDf[labelColumn] != 1)].index )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['balance', 'stock']"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  2- 2 데이터 분리"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 특성 선정 시에서는, 정답지와 관련이 있는 피쳐를 설정해야 하기에, 해당 컬럼값을 숫자로 바꿔서 계산을 해서 상관관계 여부를 찾은거고, 이후에 Label_new는 필요없다. \n",
    "#### 다시 복구해준다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'label'"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "labelColumn = \"label\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "## loc[:] 는 전체라는 뜻\n",
    "trainingDataFeatures, testDataFeatures, trainingDataLabel, testDataLabe = train_test_split( csData.loc[:, features],\n",
    "                  csData.loc[:, labelColumn],\n",
    "                  random_state=1,\n",
    "                  test_size=0.2 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(16000, 2)"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trainingDataFeatures.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4000, 2)"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testDataFeatures.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(16000,)"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trainingDataLabel.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4000,)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testDataLabe.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. 모델 선언 / 학습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "## C는 마진. 하이퍼 파라미터 튜닝으로 자주 사용\n",
    "model_svm = SVC(random_state = 5)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "model_svm.fit(trainingDataFeatures, trainingDataLabel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## 4. 예측"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictSvm = model_svm.predict(testDataFeatures)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. 데이터 정리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 원래 데이터에서 답안지의 데이터 뽑기\n",
    "testDataAll = csData.loc [testDataLabe.index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "testDataAll[\"predict_svm\"] = predictSvm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>balance</th>\n",
       "      <th>stock</th>\n",
       "      <th>label</th>\n",
       "      <th>label_new</th>\n",
       "      <th>predict_svm</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11456</th>\n",
       "      <td>744000000</td>\n",
       "      <td>38000000</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16528</th>\n",
       "      <td>724000000</td>\n",
       "      <td>32000000</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3253</th>\n",
       "      <td>704000000</td>\n",
       "      <td>27333333</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18614</th>\n",
       "      <td>240000000</td>\n",
       "      <td>30500000</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1544</th>\n",
       "      <td>258000000</td>\n",
       "      <td>28500000</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6375</th>\n",
       "      <td>640000000</td>\n",
       "      <td>48666666</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14837</th>\n",
       "      <td>652000000</td>\n",
       "      <td>26000000</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3931</th>\n",
       "      <td>564000000</td>\n",
       "      <td>45333333</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18266</th>\n",
       "      <td>528000000</td>\n",
       "      <td>46000000</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12028</th>\n",
       "      <td>696000000</td>\n",
       "      <td>36666666</td>\n",
       "      <td>diamond</td>\n",
       "      <td>1</td>\n",
       "      <td>diamond</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4000 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         balance     stock    label  label_new predict_svm\n",
       "11456  744000000  38000000  diamond          1     diamond\n",
       "16528  724000000  32000000  diamond          1     diamond\n",
       "3253   704000000  27333333  diamond          1     diamond\n",
       "18614  240000000  30500000   normal          0      normal\n",
       "1544   258000000  28500000   normal          0      normal\n",
       "...          ...       ...      ...        ...         ...\n",
       "6375   640000000  48666666  diamond          1     diamond\n",
       "14837  652000000  26000000  diamond          1     diamond\n",
       "3931   564000000  45333333  diamond          1     diamond\n",
       "18266  528000000  46000000  diamond          1     diamond\n",
       "12028  696000000  36666666  diamond          1     diamond\n",
       "\n",
       "[4000 rows x 5 columns]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testDataAll"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. 정확도 검증"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "accuracy = accuracy_score(y_true = testDataAll.label,\n",
    "              y_pred = testDataAll.predict_svm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.995"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "testDataAll.to_csv(\"d:/svc_result.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 해당 모델로 미래 예측"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "\n",
    "filename = 'finalized_model_svc.sav'\n",
    "pickle.dump(model_svm, open(filename, 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
