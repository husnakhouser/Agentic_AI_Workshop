import streamlit as st
import google.generativeai as genai

# ---------- GEMINI API CONFIG ----------
genai.configure(api_key="AIzaSyCSP3Lu8dq6x4cBznO3ANqgiWIQhjwLdj4")
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Indian Kids Recipes", layout="wide")
st.title("🍱 Dabba Delights: Little Bites Big Smiles")

# ---------- REAL RECIPES ----------
recipes = [
    {
        "name_en": "Vegetable Idli",
        "name_ta": "காய்கறி இட்லி",
        "health_goals": ["Energy Gain", "Memory Boost"],
        "prep_time": 20,
        "calories": 180,
        "energy_value": "Moderate",
        "ingredients": ["Idli rice", "Carrot", "Beans", "Curry leaves"],
        "cost": 20,
        "meal_type": "Breakfast",
        "cultural_tag": "South Indian",
        "instructions": "Soak and grind rice & urad dal. Ferment overnight. Add grated veggies and steam in idli moulds."
    },
    {
        "name_en": "Ragi Dosa",
        "name_ta": "ராகி தோசை",
        "health_goals": ["Muscle Gain", "Energy Gain"],
        "prep_time": 15,
        "calories": 210,
        "energy_value": "High",
        "ingredients": ["Ragi flour", "Curd", "Onion", "Coriander"],
        "cost": 25,
        "meal_type": "Breakfast",
        "cultural_tag": "South Indian",
        "instructions": "Mix ragi flour with curd, water, chopped onion, and coriander. Pour on hot tawa and cook."
    },
    {
        "name_en": "Paneer Paratha",
        "name_ta": "பனீர் பராட்டா",
        "health_goals": ["Muscle Gain", "Energy Gain"],
        "prep_time": 25,
        "calories": 300,
        "energy_value": "High",
        "ingredients": ["Whole wheat", "Paneer", "Coriander", "Mild spices"],
        "cost": 35,
        "meal_type": "Lunch",
        "cultural_tag": "North Indian",
        "instructions": "Grate paneer and mix with herbs. Stuff into dough balls, roll out and roast on tawa with ghee."
    },
    {
        "name_en": "Vegetable Upma",
        "name_ta": "காய்கறி உப்புமா",
        "health_goals": ["Energy Gain", "Memory Boost"],
        "prep_time": 15,
        "calories": 220,
        "energy_value": "Moderate",
        "ingredients": ["Rava", "Carrot", "Beans", "Curry leaves"],
        "cost": 18,
        "meal_type": "Breakfast",
        "cultural_tag": "South Indian",
        "instructions": "Roast rava, sauté veggies and curry leaves, add water and rava. Stir until cooked."
    },
    {
        "name_en": "Sweet Pongal",
        "name_ta": "சக்கரை பொங்கல்",
        "health_goals": ["Energy Boost", "Mood Uplift"],
        "prep_time": 20,
        "calories": 340,
        "energy_value": "High",
        "ingredients": ["Rice", "Jaggery", "Ghee", "Cashews"],
        "cost": 30,
        "meal_type": "Breakfast",
        "cultural_tag": "South Indian",
        "instructions": "Cook rice and dal together, mix with jaggery syrup, ghee, and fried cashews."
    },
    {
        "name_en": "Mini Vegetable Pulao",
        "name_ta": "சிறிய காய்கறி புலாவ்",
        "health_goals": ["Overall Nourishment", "Memory Boost"],
        "prep_time": 20,
        "calories": 270,
        "energy_value": "Moderate",
        "ingredients": ["Basmati rice", "Carrot", "Peas", "Cumin"],
        "cost": 28,
        "meal_type": "Lunch",
        "cultural_tag": "North Indian",
        "instructions": "Cook vegetables and spices in ghee. Add soaked rice, water and cook covered until fluffy."
    },
    {
        "name_en": "Coconut Rice",
        "name_ta": "தேங்காய் சாதம்",
        "health_goals": ["Cooling", "Energy"],
        "prep_time": 10,
        "calories": 250,
        "energy_value": "Moderate",
        "ingredients": ["Grated coconut", "Rice", "Mustard seeds", "Green chilies"],
        "cost": 20,
        "meal_type": "Lunch",
        "cultural_tag": "South Indian",
        "instructions": "Temper spices in coconut oil, sauté coconut, mix with rice and serve."
    },
    {
        "name_en": "Tomato Rice",
        "name_ta": "தக்காளி சாதம்",
        "health_goals": ["Energy", "Immunity"],
        "prep_time": 15,
        "calories": 240,
        "energy_value": "Moderate",
        "ingredients": ["Rice", "Tomato", "Curry leaves", "Spices"],
        "cost": 22,
        "meal_type": "Lunch",
        "cultural_tag": "South Indian",
        "instructions": "Cook tomatoes with spices to a paste, mix with cooked rice, and temper."
    },
    {
        "name_en": "Curd Rice with Pomegranate",
        "name_ta": "மாதுளை தயிர் சாதம்",
        "health_goals": ["Digestion", "Cooling"],
        "prep_time": 10,
        "calories": 230,
        "energy_value": "Moderate",
        "ingredients": ["Cooked rice", "Curd", "Pomegranate", "Mustard seeds"],
        "cost": 20,
        "meal_type": "Lunch",
        "cultural_tag": "South Indian",
        "instructions": "Mix curd with cooked rice, top with pomegranate seeds, and temper."
    },
    {
        "name_en": "Beetroot Chapati Roll",
        "name_ta": "பீட்ரூட் சப்பாத்தி ரோல்",
        "health_goals": ["Iron Boost", "Energy"],
        "prep_time": 15,
        "calories": 200,
        "energy_value": "Moderate",
        "ingredients": ["Wheat flour", "Beetroot", "Cumin", "Ghee"],
        "cost": 20,
        "meal_type": "Snack",
        "cultural_tag": "North Indian",
        "instructions": "Grate beetroot and sauté. Roll inside chapati and serve warm."
    },
    {
        "name_en": "Moong Dal Khichdi",
        "name_ta": "பாசி பருப்பு கிச்சடி",
        "health_goals": ["Protein", "Digestion"],
        "prep_time": 20,
        "calories": 280,
        "energy_value": "Moderate",
        "ingredients": ["Moong dal", "Rice", "Ghee", "Cumin"],
        "cost": 25,
        "meal_type": "Lunch",
        "cultural_tag": "North Indian",
        "instructions": "Pressure cook dal and rice with spices. Add ghee and mash lightly."
    },
    {
        "name_en": "Vegetable Oats",
        "name_ta": "காய்கறி ஓட்ஸ்",
        "health_goals": ["Fiber", "Digestion"],
        "prep_time": 15,
        "calories": 220,
        "energy_value": "Moderate",
        "ingredients": ["Oats", "Carrot", "Peas", "Onion"],
        "cost": 18,
        "meal_type": "Breakfast",
        "cultural_tag": "South Indian",
        "instructions": "Sauté veggies, add oats and water. Cook until thick and soft."
    },
    {
        "name_en": "Ragi Ladoo",
        "name_ta": "ராகி லட்டு",
        "health_goals": ["Calcium Boost", "Energy"],
        "prep_time": 10,
        "calories": 160,
        "energy_value": "Moderate",
        "ingredients": ["Ragi flour", "Jaggery", "Ghee"],
        "cost": 15,
        "meal_type": "Snack",
        "cultural_tag": "South Indian",
        "instructions": "Dry roast ragi, mix with jaggery syrup and shape into ladoos."
    }
]

# ---------- RECIPE VIEW ----------
selected = st.selectbox("🔍 Select a Recipe", [r["name_en"] for r in recipes])
recipe = next(r for r in recipes if r["name_en"] == selected)

st.subheader(f"📖 {recipe['name_en']} / {recipe['name_ta']}")
st.write(f"**Health Goals**: {', '.join(recipe['health_goals'])}")
st.write(f"**Preparation Time**: {recipe['prep_time']} min")
st.write(f"**Calories**: {recipe['calories']} kcal")
st.write(f"**Energy Value**: {recipe['energy_value']}")
st.write(f"**Ingredients**: {', '.join(recipe['ingredients'])}")
st.write(f"**Estimated Cost**: ₹{recipe['cost']}")
st.write(f"**Meal Type**: {recipe['meal_type']} | Culture: {recipe['cultural_tag']}")
st.markdown(f"**👩‍🍳 Instructions**: {recipe['instructions']}")

# ---------- GEMINI AI GENERATOR ----------
st.markdown("## 🤖 Generate a New Recipe Using Gemini")

user_prompt = st.text_input("Enter your recipe idea (e.g., Quick millet lunch for 10-year-old):")

if st.button("Generate Recipe with Gemini"):
    if not user_prompt:
        st.warning("Please enter a recipe prompt.")
    else:
        with st.spinner("Gemini is generating..."):
            try:
                gemini_response = gemini_model.generate_content(user_prompt)
                st.success("Here's your Gemini recipe:")
                st.markdown(gemini_response.text)
            except Exception as e:
                st.error(f"❌ Error from Gemini: {e}")

st.markdown("---")
st.markdown("✨ Try [https://hix.ai/chat](https://hix.ai/chat) — your AI kitchen companion!")
