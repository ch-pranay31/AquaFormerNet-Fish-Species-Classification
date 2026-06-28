# 🐟 AquaFormerNet

### Fish Species Classification Using a Hybrid Deep Learning Approach

> **Official research implementation** of the proposed AquaFormerNet architecture for fish species classification using EfficientNet-B0, Multi-Head Attention, and Transformer Encoder.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![Research](https://img.shields.io/badge/Research-Active-success)

---

# 📖 Abstract

Fish species identification plays a crucial role in fisheries management, biodiversity conservation, food safety, and nutritional awareness. Traditional identification methods are often labor-intensive, time-consuming, and require domain expertise.

This research proposes **AquaFormerNet**, a hybrid deep learning framework that combines **EfficientNet-B0** for feature extraction, **Multi-Head Attention** for emphasizing discriminative visual regions, and a **Transformer Encoder** for capturing long-range contextual relationships among image features.

The proposed model was trained using a combined dataset consisting of the **Mendeley Fish Dataset (mxf2c45yb5)** together with additional curated fish images comprising more than **7,000 images** across **9 fish categories**.

Experimental evaluation demonstrates that AquaFormerNet achieves approximately **96% classification accuracy**, while maintaining high precision, recall, and F1-score. In addition to classification, the developed web application provides nutritional and health-related information for the predicted fish species, making the system a practical decision-support tool.

---

# ✨ Key Features

* Hybrid AquaFormerNet architecture
* EfficientNet-B0 feature extraction backbone
* Multi-Head Attention mechanism
* Transformer Encoder
* Flask-based research web application
* Fish image classification
* Nutritional information retrieval
* Health information retrieval
* Approximately 96% classification accuracy
* Research-oriented implementation

---

# 🏗 Proposed Architecture

The AquaFormerNet framework integrates convolutional neural networks with transformer-based attention mechanisms to effectively capture both local and global image representations.

| Component            | Configuration                  |
| -------------------- | ------------------------------ |
| Backbone Network     | EfficientNet-B0                |
| Feature Dimension    | 1280                           |
| Attention Module     | Multi-Head Attention (8 Heads) |
| Transformer Encoder  | 2 Layers                       |
| Classification Layer | Fully Connected + Softmax      |
| Number of Classes    | 9                              |

---

# 📊 Experimental Results

| Metric    | Performance |
| --------- | ----------: |
| Accuracy  |     **96%** |
| Precision |     **96%** |
| Recall    |     **95%** |
| F1-Score  |     **95%** |

The proposed architecture demonstrates improved classification performance by effectively combining convolutional feature extraction with transformer-based contextual learning.

---

# 🐠 Fish Categories

The proposed model classifies the following fish categories:

* Pomfret
* Mackerel
* Black Snapper
* Indian Carp (Variant I)
* Prawn
* Pink Perch
* Indian Carp (Variant II)
* Black Pomfret
* One additional fish category included in the experimental dataset

> **Note:** The two Indian Carp classes represent visually distinct variants present in the training dataset.

---

# 💻 Technology Stack

### Programming Language

* Python

### Deep Learning

* PyTorch
* EfficientNet-B0
* Multi-Head Attention
* Transformer Encoder

### Backend

* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Image Processing

* Pillow
* NumPy

---

# 📁 Repository Structure

```text
AquaFormerNet-Fish-Species-Classification
│
├── app.py
├── aquaformer_model.py
├── train.ipynb
├── split_dataset.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
├── templates/
├── uploads/
│
├── models/           # Excluded
├── fish_dataset/     # Excluded
└── ...
```

---

# 📂 Dataset

The experimental model was trained using a combined dataset consisting of:

* **Mendeley Fish Dataset (mxf2c45yb5)**
* Additional curated fish images collected for research purposes

The complete dataset contains more than **7,000 images** distributed across **9 fish categories**.

> **Note:** To support the ongoing research and journal submission process, the dataset and trained model weights are **not included** in this repository.

---

# 🚧 Repository Status

This repository accompanies the research work:

**"Fish Species Classification Using an AquaFormerNet-Based Hybrid Deep Learning Approach."**

The repository is currently maintained for research documentation, version control, and academic visibility while the manuscript is being prepared for journal submission.

Additional resources—including trained model weights, reproducibility guidelines, and deployment documentation—may be released following publication.

---

# 🔬 Future Scope

* Expand to additional fish species
* Mobile application deployment
* Cloud deployment
* Real-time video classification
* Explainable AI (Grad-CAM)
* Edge-device optimization
* Continuous model improvement with larger datasets

---

# 📚 Citation

If this work contributes to your research, please cite the corresponding publication once it becomes available.

```bibtex
@article{AquaFormerNet2026,
  title   = {Fish Species Classification Using an AquaFormerNet-Based Hybrid Deep Learning Approach},
  author  = {Chintha Pranay and Team},
  journal = {To be updated after publication},
  year    = {2026}
}
```

---

# 👨‍💻 Authors

**Chintha Pranay** and Team

---

# 📄 Copyright

**© 2026 Chintha Pranay and Team. All Rights Reserved.**

This repository contains the research implementation associated with the manuscript:

**"Fish Species Classification Using an AquaFormerNet-Based Hybrid Deep Learning Approach."**

The source code is provided for academic visibility and research documentation. Redistribution, modification, or commercial use is not permitted without prior written permission from the authors until an official publication and licensing decision has been made.

---

# 🙏 Acknowledgements

* Mendeley Data
* PyTorch Community
* EfficientNet Research
* Transformer Research Community
* Open Source Machine Learning Community

---

### ⭐ Support

If you find this research interesting, consider starring the repository to support future research and development.
