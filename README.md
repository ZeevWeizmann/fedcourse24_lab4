# Fourth Lab Report — Federated Learning & Data Privacy
Université Côte d’Azur – MSc Data Science & Artificial Intelligence  
Author: Zeev Weizmann  
November 2025

## 1. Repository and Documentation Links
| Description | Link |
|------------|-------|
| SSH clone | `git@github.com:ZeevWeizmann/fedcourse24_lab4.git` |
| GitHub repository | https://github.com/ZeevWeizmann/fedcourse24_lab4 |
| GitHub Pages | https://zeevweizmann.github.io/fedcourse24_lab4/ |
| PDF report | https://github.com/ZeevWeizmann/fedcourse24_lab4/blob/7921d96790bb66a5dba7b8a1bb147a7b4f46842c/Lab_Report%20(1).pdf |

## 2. Project Overview
This lab explores malicious attacks in Federated Learning and implements robust aggregation mechanisms. Experiments are conducted under IID and non-IID data distributions.

## 3. Visual Results
### IID — No Defense
<img src="No_diffence.png" width="700"/>

### IID — Median Defense
<img src="with_diffence.png" width="700"/>

### Non-IID
<img src="non_iid.png" width="700"/>

## 4. Exercise 1 — Label-Flipping Attacks
### Data Generation
```bash
rm -r mnist/all_data
python generate_data.py --dataset mnist --n_clients 10 --iid --frac 0.1 --save_dir mnist --seed 1234
```

### Malicious Learner
```python
y = (y + 1) % 10
```

### Running Experiments
```bash
for p in 0 0.1 0.3 0.5; do
python train.py --experiment mnist --n_rounds 25 --prop $p ...
done
```

## 5. Exercise 2 — Median Defense
### Median Aggregation
```python
median_state[k] = torch.median(stacked, dim=0).values
```

## 6. Exercise 3 — Non-IID Case
Median degrades under non-IID because honest updates are heterogeneous and suppressed by the median operator.
