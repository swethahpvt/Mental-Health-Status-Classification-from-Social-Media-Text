# Project Title: Mental Health Status Classification from Social Media Text

## Team Members

| Name | Reg No | Course |
| --- | --- | --- |
| [Member A Name] | [Reg No] | [Course] |
| [Member B Name] | [Reg No] | [Course] |
| Arun | [Reg No] | [Course] |

---

## 👥 Team

| Member | Role |
|--------|------|
| Member A | [To be filled by Member A] |
| Member B | [To be filled by Member B] |
| Arun | Responsible for model evaluation and comparison. Loaded Member B's trained model outputs (y_test.npy, y_pred_svm.npy, y_pred_bert.npy) and performed comprehensive evaluation of both SVM and BERT models. Computed per-class metrics including sensitivity (recall), specificity, precision, and F1-score for all four categories — depression, anxiety, PTSD, and normal — using sklearn's classification_report. Generated side-by-side confusion matrix heatmaps for visual comparison of both models and saved them as confusion_matrices.png. Produced an evaluation summary table (evaluation_summary.csv) comparing both models on Accuracy, Macro F1, and Weighted F1. BERT achieved 85.7% accuracy vs SVM's 82.2%, with BERT showing the most improvement in the anxiety and normal classes. Authored a detailed discussion write-up (discussion.md) covering early intervention use cases and ethical risks including misclassification harm, privacy concerns, data bias, and surveillance misuse. Uploaded all evaluation files to the GitHub repository. |

---

## Problem Statement

Mental health conditions such as depression, anxiety, and PTSD are increasingly reflected in social media activity. With millions of users sharing their emotional experiences on platforms like Reddit and Twitter, there is a significant opportunity to use Natural Language Processing (NLP) to detect early signs of mental health struggles at scale.

This project aims to build a robust classification system that can automatically categorize social media posts into four mental health categories: **Depression**, **Anxiety**, **PTSD**, and **Normal**, using both traditional machine learning and state-of-the-art transformer-based approaches.

The project addresses the complete data science lifecycle including:

- Data collection and preprocessing with privacy considerations
- Feature extraction using TF-IDF and BERT embeddings
- Model development and fine-tuning
- Evaluation using sensitivity, specificity, and F1-score
- Discussion of ethical risks and early intervention use cases

---

## Objectives

- Classify social media posts into Depression, Anxiety, PTSD, and Normal categories
- Perform text preprocessing with anonymization and ethical data handling
- Build and compare TF-IDF + SVM baseline with fine-tuned BERT model
- Evaluate models using sensitivity, specificity, F1-score, and confusion matrices
- Discuss real-world potential for early mental health intervention tools
- Address privacy, consent, and ethical risks of deploying such systems

---

## Dataset

- **Source:** Reddit posts across mental health-related subreddits
- **Categories:** Depression, Anxiety, PTSD, Normal
- **Total Test Samples:** 2,060

### Key Columns

- `text` — Social media post content
- `label` — Mental health category (depression / anxiety / PTSD / normal)

### Label Mapping

| Label | Category |
| --- | --- |
| 0 | Depression |
| 1 | Anxiety |
| 2 | PTSD |
| 3 | Normal |

---

## Methodology

### 1. Data Collection & Preprocessing *(Member A)*

- Collected Reddit posts from depression, anxiety, PTSD, and normal subreddits
- Cleaned text: removed URLs, special characters, and stopwords
- Anonymized data to remove personally identifiable information
- Handled ethical and privacy concerns
- Output: cleaned labeled dataset

---

### 2. Model Building *(Member B)*

- **Baseline:** TF-IDF vectorization + Support Vector Machine (SVM)
- **Deep Learning:** Fine-tuned BERT for sequence classification
- Train-test split with stratification
- Saved predictions as y_pred_svm.npy and y_pred_bert.npy
- Output: trained models and predictions

---

### 3. Model Evaluation *(Member C — Arun)*

- Loaded saved predictions from Member B
- Computed per-class sensitivity, specificity, precision, and F1-score
- Generated confusion matrices for both models
- Compared BERT vs SVM performance
- Authored discussion on early intervention use cases and ethical risks

---

## Results & Comparison

| Model | Accuracy | Macro F1 | Weighted F1 |
| --- | --- | --- | --- |
| TF-IDF + SVM | 82.2% | 0.821 | 0.821 |
| BERT (fine-tuned) | 85.7% | 0.857 | 0.857 |

**Best Model: BERT with 85.7% accuracy and Macro F1 of 0.857** 🏆

---

