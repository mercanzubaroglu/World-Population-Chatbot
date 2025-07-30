# 🌍 Nüfus Chatbotu: Dünya Nüfusu Analiz ve Tahmin Aracı  
### World Population Chatbot: Global Population Analysis & Forecast System

![streamlit-banner](https://img.shields.io/badge/Streamlit-Powered-red?logo=streamlit)
![ml-badge](https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-blue)
![language](https://img.shields.io/badge/Language-Python-informational)
![status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🧠 Proje Amacı / Project Objective

📌 Bu proje, dünya ülkelerinin nüfus verilerini temel alan, doğal dil destekli etkileşimli bir **Streamlit chatbot** uygulamasıdır. Kullanıcılar, 2025 ve 2050 nüfus tahminlerine dayalı olarak sorular sorabilir, ülke karşılaştırmaları yapabilir ve grafikler/tablolarla desteklenen anlık analizler alabilir.

📌 This project is an interactive **Streamlit-based chatbot** interface built on global country population data. It allows users to query forecasts for 2025 and 2050, make comparative analyses between countries, and receive ML-based predictions and visualizations through natural language input.

---

## 🔍 Kullanılan Veri Seti / Dataset Information

- **Kaggle Dataset:** [World Population by Country](https://www.kaggle.com/datasets/thebreaker49/world-population)
- **Yükleyici / Uploaded by:** TheBreaker49
- **Veri Yılı / Data Range:** Tahmini 2025 ve 2050 nüfusları + 2022 verileri
- **Sütunlar / Key Columns:**
  - `country`: Ülke adı / Country name
  - `pop2025`: 2025 tahmini nüfusu / Forecasted population for 2025
  - `pop2050`: 2050 tahmini nüfusu / Forecasted population for 2050
  - `growthRate`: Büyüme oranı / Growth rate
  - `density`: Nüfus yoğunluğu / Density
  - `worldPercentage`: Dünya nüfusuna oranı / Percentage of world population

---

## 🚀 Özellikler / Key Features

| Özellik (TR)                             | Feature (EN)                                     |
|------------------------------------------|--------------------------------------------------|
| Doğal dil ile soru sorma                 | Ask questions using natural language             |
| Ülke verilerini tablo & grafikle sunma   | Show country population with table and bar chart |
| İki ülkeyi karşılaştırma                 | Compare two countries side-by-side               |
| En kalabalık / en hızlı büyüyen ülkeler  | Top populated / fastest growing countries        |
| ML tahmini ile 2050 nüfus tahmini        | Forecast 2050 population using ML                |
| Kullanıcı sohbet geçmişini saklama       | Persist user query history (chat session)        |
| Tamamen Streamlit tabanlı arayüz         | Fully interactive Streamlit web app              |

---

## 🛠️ Kullanılan Teknolojiler / Technologies Used

| Teknoloji / Library     | Açıklama / Description                             |
|-------------------------|----------------------------------------------------|
| `Streamlit`             | Web uygulama arayüzü / Web app UI                 |
| `Pandas`                | Veri işleme ve analiz / Data wrangling            |
| `Seaborn & Matplotlib`  | Grafikler ve veri görselleştirme / Visualization  |
| `scikit-learn`          | ML modeli (Linear Regression)                     |
| `re`                    | Regex ile metin işleme / Pattern extraction       |
| `NumPy`                 | Sayısal veri dönüşümleri / Numerical ops          |

---
> 📌 **Not:** Bu proje başlangıçta bir `.ipynb` (Jupyter Notebook) dosyası olarak geliştirilmiştir.  
> Ancak, Streamlit yalnızca `.py` (Python script) dosyaları üzerinden çalışabildiği için komut satırından (CMD) çalıştırılabilmesi amacıyla `.py` uzantısına dönüştürülmüştür.

> 📌 **Note:** This project was originally developed as a `.ipynb` (Jupyter Notebook) file.  
> However, since Streamlit runs only with `.py` (Python script) files, it was converted to `.py` format to enable execution via command line (CMD).

---


