from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# =====================================================
# RESTAURANT MENU
# =====================================================

MENU = [

    {
        "name": "Masala Dosa",
        "type": "vegetarian",
        "cuisine": "south indian",
        "price": 120,
        "spice": "spicy",
        "description": "Crispy dosa served with sambar and chutney"
    },

    {
        "name": "Idli Sambar",
        "type": "vegetarian",
        "cuisine": "south indian",
        "price": 90,
        "spice": "mild",
        "description": "Soft idlis served with sambar and chutney"
    },

    {
        "name": "Vegetable Kothu Parotta",
        "type": "vegetarian",
        "cuisine": "south indian",
        "price": 150,
        "spice": "spicy",
        "description": "Kothu parotta cooked with vegetables and spices"
    },

    {
        "name": "Paneer Chettinad",
        "type": "vegetarian",
        "cuisine": "south indian",
        "price": 180,
        "spice": "spicy",
        "description": "Spicy Chettinad-style paneer curry"
    },

    {
        "name": "Veg Biryani",
        "type": "vegetarian",
        "cuisine": "south indian",
        "price": 170,
        "spice": "medium",
        "description": "Aromatic vegetable biryani"
    },

    {
        "name": "Chicken Biryani",
        "type": "non-vegetarian",
        "cuisine": "south indian",
        "price": 250,
        "spice": "spicy",
        "description": "Spicy chicken biryani with aromatic rice"
    },

    {
        "name": "Chicken Chettinad",
        "type": "non-vegetarian",
        "cuisine": "south indian",
        "price": 280,
        "spice": "spicy",
        "description": "Traditional spicy Chettinad chicken"
    },

    {
        "name": "Veg Fried Rice",
        "type": "vegetarian",
        "cuisine": "chinese",
        "price": 160,
        "spice": "medium",
        "description": "Chinese-style vegetable fried rice"
    },

    {
        "name": "Chicken Noodles",
        "type": "non-vegetarian",
        "cuisine": "chinese",
        "price": 220,
        "spice": "medium",
        "description": "Stir-fried noodles with chicken"
    },

    {
        "name": "Paneer Butter Masala",
        "type": "vegetarian",
        "cuisine": "north indian",
        "price": 200,
        "spice": "medium",
        "description": "Creamy paneer curry"
    },

    {
        "name": "Paneer Tikka",
        "type": "vegetarian",
        "cuisine": "north indian",
        "price": 220,
        "spice": "spicy",
        "description": "Grilled paneer with Indian spices"
    }

]


# =====================================================
# HOME PAGE
# =====================================================

@app.route("/")
def home():

    return render_template("index.html")


# =====================================================
# FOOD KEYWORD CHECK
# =====================================================

def is_food_related(message):

    food_keywords = [

        "food",
        "eat",
        "eating",
        "dish",
        "dishes",
        "restaurant",
        "menu",
        "breakfast",
        "lunch",
        "dinner",
        "biryani",
        "dosa",
        "idli",
        "rice",
        "noodles",
        "chicken",
        "paneer",
        "veg",
        "vegetarian",
        "non veg",
        "non-veg",
        "non vegetarian",
        "spicy",
        "mild",
        "cuisine",
        "south indian",
        "north indian",
        "chinese",
        "budget",
        "price",
        "rupees",
        "₹",
        "cheap",
        "under",
        "below"
    ]

    return any(
        keyword in message
        for keyword in food_keywords
    )


# =====================================================
# EXTRACT USER PREFERENCES
# =====================================================

def extract_preferences(message):

    message = message.lower()

    preferences = {

        "type": None,

        "cuisine": None,

        "spice": None,

        "max_price": None

    }


    # -------------------------------------------------
    # VEGETARIAN / NON-VEGETARIAN
    # -------------------------------------------------

    if (
        "non vegetarian" in message
        or "non-vegetarian" in message
        or "non veg" in message
        or "non-veg" in message
        or "chicken" in message
    ):

        preferences["type"] = "non-vegetarian"

    elif (
        "vegetarian" in message
        or "veg food" in message
        or "veg" in message
        or "vegetable" in message
        or "paneer" in message
    ):

        preferences["type"] = "vegetarian"


    # -------------------------------------------------
    # CUISINE
    # -------------------------------------------------

    if (
        "south indian" in message
        or "south india" in message
    ):

        preferences["cuisine"] = "south indian"

    elif (
        "north indian" in message
        or "north india" in message
    ):

        preferences["cuisine"] = "north indian"

    elif "chinese" in message:

        preferences["cuisine"] = "chinese"


    # -------------------------------------------------
    # SPICE
    # -------------------------------------------------

    if (
        "very spicy" in message
        or "spicy" in message
        or "hot" in message
    ):

        preferences["spice"] = "spicy"

    elif (
        "medium spicy" in message
        or "medium" in message
    ):

        preferences["spice"] = "medium"

    elif (
        "mild" in message
        or "less spicy" in message
        or "not spicy" in message
    ):

        preferences["spice"] = "mild"


    # -------------------------------------------------
    # BUDGET
    # -------------------------------------------------

    words = (
        message
        .replace("₹", " ")
        .replace(",", " ")
        .split()
    )


    for i, word in enumerate(words):

        if word.isdigit():

            number = int(word)


            if number <= 5000:

                # Example:
                # under 200
                # below 300
                # within 500

                if i > 0 and words[i - 1] in [
                    "under",
                    "below",
                    "within",
                    "budget"
                ]:

                    preferences["max_price"] = number


                elif i + 1 < len(words):

                    if words[i + 1] in [
                        "rupees",
                        "rs"
                    ]:

                        preferences["max_price"] = number


    return preferences


# =====================================================
# FILTER MENU
# =====================================================

def recommend_food(preferences):

    results = []


    for item in MENU:

        # ---------------------------------------------
        # FOOD TYPE
        # ---------------------------------------------

        if preferences["type"]:

            if item["type"] != preferences["type"]:

                continue


        # ---------------------------------------------
        # CUISINE
        # ---------------------------------------------

        if preferences["cuisine"]:

            if item["cuisine"] != preferences["cuisine"]:

                continue


        # ---------------------------------------------
        # SPICE
        # ---------------------------------------------

        if preferences["spice"]:

            if item["spice"] != preferences["spice"]:

                continue


        # ---------------------------------------------
        # PRICE
        # ---------------------------------------------

        if preferences["max_price"]:

            if item["price"] > preferences["max_price"]:

                continue


        results.append(item)


    return results[:5]


# =====================================================
# CREATE FOOD RESPONSE
# =====================================================

def create_food_response(preferences, recommendations):


    if not recommendations:

        return (
            "Sorry 😕 I couldn't find a dish matching "
            "all your preferences.<br><br>"
            "Try increasing your budget or changing "
            "the cuisine/spice level."
        )


    response = (
        "Great choice! 😋 "
        "Here are some dishes I recommend:<br><br>"
    )


    for item in recommendations:

        response += f"""

        <div class="food-card">

            <h3>🍽️ {item["name"]}</h3>

            <p>
                💰 ₹{item["price"]}
                &nbsp; | &nbsp;
                🌶️ {item["spice"].title()}
            </p>

            <p>
                🍴 {item["cuisine"].title()}
            </p>

            <p>
                {item["description"]}
            </p>

        </div>

        """


    return response


# =====================================================
# CHAT API
# =====================================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()


    if not data:

        return jsonify({

            "message":
            "Please send a message."

        })


    user_message = data.get(
        "message",
        ""
    ).strip()


    message = user_message.lower()


    # =================================================
    # EMPTY MESSAGE
    # =================================================

    if not message:

        return jsonify({

            "message":
            "Please type something 😊"

        })


    # =================================================
    # GREETING
    # =================================================

    greetings = [

        "hi",
        "hello",
        "hey",
        "hii",
        "hiii",
        "good morning",
        "good afternoon",
        "good evening"

    ]


    if message in greetings:

        return jsonify({

            "message":
            """
            Hello! 👋 Welcome to our Restaurant Assistant! 🍽️
            <br><br>
            I can help you find food based on:
            <br><br>
            🥗 Vegetarian / Non-vegetarian
            <br>
            🍴 Cuisine
            <br>
            🌶️ Spice level
            <br>
            💰 Budget
            <br><br>
            For example:
            <br>
            <b>"I want vegetarian spicy South Indian food under 200"</b>
            """

        })


    # =================================================
    # THANK YOU
    # =================================================

    if (
        "thank you" in message
        or "thanks" in message
        or message == "thank"
    ):

        return jsonify({

            "message":
            "You're welcome! 😊 Enjoy your food! 🍽️"

        })


    # =================================================
    # BYE
    # =================================================

    if (
        message == "bye"
        or "goodbye" in message
    ):

        return jsonify({

            "message":
            "Goodbye! 👋 Have a delicious day! 🍽️"

        })


    # =================================================
    # FOOD RELATED CHECK
    # =================================================

    if not is_food_related(message):

        return jsonify({

            "message":
            """
            Sorry 😊 I am a Restaurant Assistant.
            <br><br>
            I can only help with food and restaurant
            related questions.
            <br><br>
            You can ask me:
            <br>
            • Vegetarian food
            <br>
            • Non-vegetarian food
            <br>
            • South Indian food
            <br>
            • North Indian food
            <br>
            • Chinese food
            <br>
            • Spicy / Mild food
            <br>
            • Food under a specific budget
            """

        })


    # =================================================
    # EXTRACT PREFERENCES
    # =================================================

    preferences = extract_preferences(
        message
    )


    # =================================================
    # CHECK IF USER GAVE ANY PREFERENCE
    # =================================================

    has_preference = any([

        preferences["type"],

        preferences["cuisine"],

        preferences["spice"],

        preferences["max_price"]

    ])


    # =================================================
    # FOOD BUT NO PREFERENCE
    # =================================================

    if not has_preference:

        return jsonify({

            "message":
            """
            Sure! 🍽️ I can help you choose a dish.
            <br><br>
            First, tell me:
            <br><br>
            🥗 Are you vegetarian or non-vegetarian?
            """

        })


    # =================================================
    # GET RECOMMENDATIONS
    # =================================================

    recommendations = recommend_food(
        preferences
    )


    # =================================================
    # CREATE RESPONSE
    # =================================================

    response = create_food_response(

        preferences,

        recommendations

    )


    return jsonify({

        "message": response,

        "preferences": preferences,

        "recommendations": recommendations

    })


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )