# 📷 Resim Tanıma (Image Recognition) — Basit Python Projesi

Bu proje, **Python** ve **Streamlit** kullanarak bir görsel tanıma uygulaması yapmanıza olanak sağlar. Yüklediğiniz fotoğrafları önceden eğitilmiş **MobileNetV2** modeli ile analiz eder ve **ImageNet** sınıflarından en olası tahminleri görüntüler.

This project allows you to perform **image recognition** using **Python** and **Streamlit**. Uploaded photos are analyzed using the pre-trained **MobileNetV2** model, and the most probable predictions from **ImageNet** classes are displayed.

---

## 🛠️ Özellikler / Features

- Fotoğraf yükleme ve önizleme / Upload and preview images
- MobileNetV2 ile tahmin / Predictions using MobileNetV2
- Tahminlerin olasılıklarını yüzdelik olarak gösterme / Display probabilities as percentages
- Basit ve kullanıcı dostu arayüz / Simple and user-friendly interface
- Geliştirici ipuçları ve öneriler / Developer tips & suggestions

---

## ⚡ Kurulum / Installation

1. Python 3.8 veya üstünü kurun / Install Python 3.8+
2. Projeyi klonlayın / Clone the repository:
   ```bash
   git clone <REPO_URL>
   cd <PROJECT_FOLDER>
   pip install -r requirements.txt
   
## Kullanılan Sistemler

  ```bash
    streamlit
    pillow
    tensorflow
    numpy
  ```
## 🚀 Çalıştırma / Run the App

Projeyi çalıştırmak için terminalde aşağıdaki komutu kullanın:

Run the project using the following command in the terminal:
   ```bash
    streamlit run algılıma.py
  ```

## 🖼️ Kullanım / Usage 

1.	Bir fotoğraf yükleyin (jpg, png) butonuna tıklayın.
2.	Bilgisayarınızdan bir fotoğraf seçin.
3.	Yüklenen fotoğrafın altında modelin tahminlerini göreceksiniz:
	•	Etiket (Label)
	•	Olasılık (% Probability)
4.	Not: Model ImageNet sınıfları ile eğitildiği için sonuçlar İngilizce olabilir ve her zaman %100 doğru olmayabilir.

## 💡 İpuçları / Tips
	•	Daha doğru sonuçlar için transfer learning ile kendi verinizle yeniden eğitebilirsiniz.
	•	Hugging Face CLIP veya ViT modelleri ile zero-shot etiketleme yapabilirsiniz.
	•	Google Vision / AWS Rekognition gibi servisleri kullanarak daha geniş sınıf ve etiketler elde edebilirsiniz.
	•	Tahminleri Türkçe’ye çevirmek için decode sonuçlarını bir sözlükle eşleştirip çeviri yapabilirsiniz.

##📂 Proje Yapısı / Project Structure
  ```bash
    

project/
│
├─ algılıma.py         # Ana uygulama dosyası / Main app
├─ requirements.txt    # Python bağımlılıkları / Python dependencies
├─ README.md           # Bu dosya / This file
└─ images/             # İsteğe bağlı test görselleri / Optional test images


