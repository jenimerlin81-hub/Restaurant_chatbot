# 🍽️ Restaurant Chatbot – Personalized Food Recommendation

A smart restaurant assistant chatbot that helps users find suitable food based on their personal preferences such as:

- 🥗 Vegetarian / Non-Vegetarian
- 🍴 Cuisine
- 🌶️ Spice Level
- 💰 Budget / Price
- 🍛 Food preferences

The chatbot uses **Flask**, **Gemini AI**, and **Firebase Firestore** to provide personalized food recommendations.

---

## 📌 Project Overview

Choosing a suitable food from a large restaurant menu can be difficult.

This project provides a conversational restaurant assistant that understands user preferences and recommends suitable dishes.

### Example

User:

> Hi

Bot:

> Hello! 👋 Welcome to our Restaurant Assistant!  
> What would you like to eat today?

User:

> I want vegetarian South Indian food. It should be spicy and under ₹200.

Bot:

> Great choice! 😋 Here are some dishes I recommend:
>
> 🍽️ Masala Dosa – ₹120  
> 🌶️ Spicy South Indian dish
>
> 🍽️ Paneer Chettinad – ₹180  
> 🌶️ Spicy South Indian dish
>
> 🍽️ Vegetable Kothu Parotta – ₹150  
> 🌶️ Spicy South Indian dish

---

# 🎯 Objectives

The main objectives of this project are:

1. Understand natural-language food preferences.
2. Identify vegetarian/non-vegetarian requirements.
3. Identify preferred cuisine.
4. Identify preferred spice level.
5. Identify user's budget.
6. Retrieve suitable dishes from the restaurant menu.
7. Filter and match dishes based on preferences.
8. Generate personalized recommendations using Gemini AI.
9. Provide an interactive chatbot interface.

---

# 🏗️ System Architecture

```text
                👤 User
                   |
                   v
          💬 Chatbot Frontend
                   |
                   v
             🌐 Flask REST API
                   |
                   v
        🧠 Preference Extraction
                   |
          +--------+--------+
          |                 |
          v                 v
    🔥 Firestore         🤖 Gemini
     Menu Database        AI
          |                 |
          +--------+--------+
                   |
                   v
          🔍 Filtering / Matching
                   |
                   v
        🍽️ Suitable Dishes
                   |
                   v
          🤖 Gemini Recommendation
                   |
                   v
             👤 User
