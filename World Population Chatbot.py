{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "9f3dc565-99b9-4080-8766-0c7f4d364599",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import streamlit as st\n",
    "from sklearn.linear_model import LinearRegression\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "137a7bbd-1ab6-4a72-8616-879b09bd1bde",
   "metadata": {},
   "outputs": [],
   "source": [
    "def extract_number(text, default=10):\n",
    "    match = re.search(r'\\d+', text)\n",
    "    if match:\n",
    "        return int(match.group())\n",
    "    return default\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "1947ee13-ffed-469a-951a-a6cfab6282a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-30 16:30:46.394 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:46.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:46.399 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:46.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:46.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:46.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:46.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Streamlit ayarları / Page settings\n",
    "st.set_page_config(page_title=\"Nüfus Chatbotu\", layout=\"centered\")\n",
    "st.title(\"Dünya Nüfusu Chatbot Analiz Aracı\")\n",
    "st.markdown( \"\"\" Bu uygulama, dünya nüfus verileri ile etkileşimli şekilde çalışmanızı sağlar.  \n",
    "Soru sorarak grafik, tablo, istatistik ve makine öğrenmesi tahminleri alabilirsiniz.  \n",
    "**Örnekler:**  \n",
    "- `En kalabalık 10 ülke`  \n",
    "- `Hindistan'ın 2025 nüfusu nedir?`  \n",
    "- `Türkiye için tahmin et`  \n",
    "- `En hızlı büyüyen 15 ülkeyi göster`\n",
    "- `Germanay ve Turkey karşılaştır`\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "6ee8e327-14fd-407d-8591-c1e5735b8c4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#CSV dosyasını oku /  Read the CSV file\n",
    "df= pd.read_csv(\"WorldPopulationByCountry.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e9f1b2ba-34de-4d6c-9498-9ab25f3649ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Sütun adlarını düzenle / Rename columns for easier use\n",
    "df.rename(columns={\n",
    "    \"pop2025\": \"Population_2025\",\n",
    "    \"pop2050\": \"Population_2050\",\n",
    "    \"growthRate\": \"Growth_Rate\",\n",
    "    \"worldPercentage\" : \"World_Percentage\",\n",
    "    \" density\" : \"Density\"\n",
    "}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "39fc86f7-720d-4c4d-85d1-9932c633aa4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {color: black;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Ml MODELİ Lineer Regression\n",
    "model=LinearRegression()\n",
    "model.fit(df[[\"Population_2025\"]] , df[\"Population_2050\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "099a3ee5-b083-4b6f-a389-3b985b7d994d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def chatbot_reply(user_input):\n",
    "    user_input = user_input.lower()\n",
    "\n",
    "    # Çoklu ülke karşılaştırması kontrolü / Check if multiple countries are mentioned\n",
    "    countries_in_text = [country for country in df[\"country\"] if country.lower() in user_input]\n",
    "    num_countries = len(countries_in_text)\n",
    "\n",
    "    if num_countries == 2:\n",
    "        country1, country2 = countries_in_text\n",
    "        row1 = df[df[\"country\"].str.lower() == country1.lower()]\n",
    "        row2 = df[df[\"country\"].str.lower() == country2.lower()]\n",
    "\n",
    "        pop25_1, pop50_1 = row1[\"Population_2025\"].values[0], row1[\"Population_2050\"].values[0]\n",
    "        pop25_2, pop50_2 = row2[\"Population_2025\"].values[0], row2[\"Population_2050\"].values[0]\n",
    "\n",
    "        st.subheader(f\"📊 {country1} ve {country2} Karşılaştırması / Comparison\")\n",
    "        comp_df = pd.DataFrame({\n",
    "            \"Ülke / Country\": [country1, country2],\n",
    "            \"2025 Nüfusu\": [pop25_1, pop25_2],\n",
    "            \"2050 Nüfusu\": [pop50_1, pop50_2],\n",
    "            \"Büyüme Oranı\": [row1[\"Growth_Rate\"].values[0], row2[\"Growth_Rate\"].values[0]]\n",
    "        })\n",
    "\n",
    "        st.dataframe(comp_df)\n",
    "\n",
    "        fig, ax = plt.subplots(figsize=(6, 4))\n",
    "        sns.barplot(x=[\"2025-\"+country1, \"2050-\"+country1, \"2025-\"+country2, \"2050-\"+country2],\n",
    "                    y=[pop25_1, pop50_1, pop25_2, pop50_2], ax=ax)\n",
    "        ax.set_title(f\"{country1} vs {country2} Nüfus Değişimi / Population Change\")\n",
    "        st.pyplot(fig)\n",
    "        return\n",
    "\n",
    "    elif num_countries == 1:\n",
    "        country = countries_in_text[0]\n",
    "        row = df[df[\"country\"].str.lower() == country.lower()]\n",
    "        pop25 = int(row[\"Population_2025\"].values[0])\n",
    "        pop50 = int(row[\"Population_2050\"].values[0])\n",
    "        rate = float(row[\"Growth_Rate\"].values[0])\n",
    "\n",
    "        st.subheader(f\"📍 {country} Verileri / Data\")\n",
    "        st.write(f\"👶 2025: {pop25:,}\")\n",
    "        st.write(f\"👴 2050: {pop50:,}\")\n",
    "        st.write(f\"📈 Büyüme Oranı: {rate:.2%}\")\n",
    "\n",
    "        fig, ax = plt.subplots(figsize=(5, 4))\n",
    "        sns.barplot(x=[\"2025\", \"2050\"], y=[pop25, pop50], ax=ax)\n",
    "        ax.set_title(f\"{country} Nüfus Değişimi\")\n",
    "        st.pyplot(fig)\n",
    "        return\n",
    "\n",
    "    # Diğer sorgular: en kalabalık, hızlı büyüyen vs\n",
    "    if \"en kalabalık\" in user_input or \"most populated\" in user_input:\n",
    "        n = extract_number(user_input, default=10)\n",
    "        top = df.sort_values(by=\"Population_2050\", ascending=False).head(n)\n",
    "\n",
    "        st.subheader(f\"📊 2050'de En Kalabalık {n} Ülke\")\n",
    "        fig, ax = plt.subplots(figsize=(10, 6))\n",
    "        sns.barplot(data=top, x=\"Population_2050\", y=\"country\", ax=ax)\n",
    "        st.pyplot(fig)\n",
    "        st.dataframe(top[[\"country\", \"Population_2050\"]])\n",
    "        return\n",
    "\n",
    "    elif \"en hızlı\" in user_input or \"fastest\" in user_input:\n",
    "        n = extract_number(user_input, default=10)\n",
    "        top = df.sort_values(by=\"Growth_Rate\", ascending=False).head(n)\n",
    "\n",
    "        st.subheader(f\"📈 En Hızlı Büyüyen {n} Ülke\")\n",
    "        fig, ax = plt.subplots(figsize=(10, 6))\n",
    "        sns.barplot(data=top, x=\"Growth_Rate\", y=\"country\", ax=ax)\n",
    "        st.pyplot(fig)\n",
    "        st.dataframe(top[[\"country\", \"Growth_Rate\"]])\n",
    "        return\n",
    "\n",
    "    elif \"tahmin\" in user_input or \"predict\" in user_input:\n",
    "        for country in df[\"country\"]:\n",
    "            if country.lower() in user_input:\n",
    "                pop25 = df[df[\"country\"].str.lower() == country.lower()][\"Population_2025\"].values[0]\n",
    "                predicted = model.predict(np.array([[pop25]]))[0]\n",
    "                st.success(f\"{country} için model tahmini 2050 nüfusu: {int(predicted):,}\")\n",
    "                return\n",
    "        return st.warning(\"Ülke bulunamadı / Country not found.\")\n",
    "\n",
    "    else:\n",
    "        return st.info(\"❓ Soru tanınmadı. Örnekler:\\n- Türkiye verilerini getir\\n- Türkiye ve Almanya'yı karşılaştır\\n- En kalabalık 7 ülke\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "c4ae6ba9-d928-4939-b872-713cee0bbf22",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-30 16:30:47.747 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.749 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.750 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.751 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.752 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.754 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.756 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.757 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.759 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.760 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.761 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-30 16:30:47.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Kullanıcının soru ve yanıt geçmişini sakla\n",
    "if \"chat_history\" not in st.session_state:\n",
    "    st.session_state.chat_history = []\n",
    "\n",
    "# Kullanıcıdan soru al\n",
    "user_input = st.text_input(\"📝 Soru Girin / Ask a Question\")\n",
    "\n",
    "# Soru geldiyse işleme al\n",
    "if user_input:\n",
    "    st.session_state.chat_history.append((\"👤 Siz\", user_input))\n",
    "    \n",
    "    # Yanıt üret\n",
    "    with st.spinner(\"Yanıtlanıyor...\"):\n",
    "        # chatbot_reply fonksiyonundan çıktı alma\n",
    "        response = chatbot_reply(user_input)\n",
    "    \n",
    "    # Eğer chatbot bir şey yazdıysa (örneğin bilgi veya uyarı), onu da sakla\n",
    "    if response is not None:\n",
    "        st.session_state.chat_history.append((\"🤖 Chatbot\", response))\n",
    "\n",
    "# Sohbet geçmişini göster\n",
    "st.subheader(\"📜 Sohbet Geçmişi / Chat History\")\n",
    "for sender, msg in st.session_state.chat_history:\n",
    "    st.markdown(f\"**{sender}:** {msg}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1014f33a-7147-4fee-a573-38caf07dc593",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "478d6f16-84b5-441f-aa3d-b929516b28aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ad00dfc-2753-4723-bdc2-c2ac41b1dda7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe51aaf2-5e55-4e9c-8b19-30e604183f9c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
