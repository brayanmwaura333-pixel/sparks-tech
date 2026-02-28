import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# --- Logging ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- Bot Token ---
TOKEN = "8690187428:AAFgfbe1CcdUVQdsR3zud_GfdcwttnTCs8w"

# --- Start & Welcome with Personal Touch ---
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Mapwork", callback_data='mapwork')],
        [InlineKeyboardButton("Cross-section", callback_data='cross_section')],
        [InlineKeyboardButton("Physical Geography", callback_data='physical')],
        [InlineKeyboardButton("Human Geography", callback_data='human')],
        [InlineKeyboardButton("Environmental Geography", callback_data='environment')],
        [InlineKeyboardButton("Animal & Plant Species", callback_data='biodiversity')],
        [InlineKeyboardButton("Drainage & Rivers", callback_data='drainage')],
        [InlineKeyboardButton("Aviation", callback_data='aviation')],
        [InlineKeyboardButton("Atlases", callback_data='atlases')],
        [InlineKeyboardButton("Quizzes", callback_data='quiz')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "🌟 Hello, young geographers! 🌟\n\n"
        "I'm *Spark*, the Genius of Geography at Pioneer Group of Schools 🏫.\n"
        "I’m here to make your journey through maps, mountains, rivers, and skies both **fun** and **easy**! 😎\n\n"
        "Get ready for amazing quizzes, cool facts, and tips to become a Geography Wizard! 🌍✨\n\n"
        "Click a button below to start exploring:"
        , reply_markup=reply_markup
    )

# --- Help ---
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "/start - Launch the bot\n"
        "/help - Show this message\n"
        "/quiz - Start a geography quiz\n"
        "/answer <your answer> - Answer a quiz"
    )

# --- Callback Query Handler for Buttons ---
def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = query.data

    if data == 'mapwork':
        query.edit_message_text(
            "🗺 Mapwork Tips:\n"
            "1. Check scale\n"
            "2. Draw relief/contours\n"
            "3. Label rivers, roads, settlements\n"
            "4. Use compass directions\n"
            "5. Keep labels neat"
        )
    elif data == 'cross_section':
        query.edit_message_text(
            "📏 Cross-section Tips:\n"
            "1. Draw baseline for ground\n"
            "2. Transfer contour heights vertically\n"
            "3. Connect points smoothly\n"
            "4. Label features & scale"
        )
    elif data == 'physical':
        query.edit_message_text(
            "🏔 Physical Geography:\n"
            "- Landforms: mountains, valleys, plateaus, hills, plains\n"
            "- Rivers & Lakes: major rivers, drainage patterns\n"
            "- Oceans & Seas: currents, tides, waves\n"
            "- Climate & Weather: global climate zones, rainfall patterns\n"
            "- Soil & Vegetation: soil types, forests, grasslands, deserts"
        )
    elif data == 'human':
        query.edit_message_text(
            "🏘 Human Geography:\n"
            "- Population: distribution, density, growth\n"
            "- Settlements: urban, rural, megacities\n"
            "- Migration & demography\n"
            "- Economic activities: agriculture, industry, services"
        )
    elif data == 'environment':
        query.edit_message_text(
            "🌿 Environmental Geography:\n"
            "- Natural resources: water, minerals, forests, energy\n"
            "- Conservation: wildlife, protected areas\n"
            "- Disasters: earthquakes, volcanoes, floods, hurricanes"
        )
    elif data == 'biodiversity':
        query.edit_message_text(
            "🦁 Animal & Plant Species by Biome:\n"
            "- Savannah: Lions, Elephants, Giraffes\n"
            "- Rainforest: Gorillas, Chimpanzees, Jaguars\n"
            "- Desert: Camels, Fennec Foxes, Scorpions\n"
            "- Mountains: Snow Leopards, Mountain Goats\n"
            "- Wetlands: Hippos, Crocodiles, Frogs"
        )
    elif data == 'drainage':
        query.edit_message_text(
            "🌊 Drainage Patterns:\n"
            "1. Dendritic – tree-like\n"
            "2. Radial – outward from high point\n"
            "3. Trellis – main streams + tributaries\n"
            "4. Rectangular – follows fault lines\n"
            "5. Annular – circular around dome/basin"
        )
    elif data == 'aviation':
        aviation(update, context)
    elif data == 'atlases':
        query.edit_message_text(
            "📚 Atlases Info:\n"
            "- Political Atlas: countries, capitals, boundaries\n"
            "- Physical Atlas: mountains, rivers, vegetation, soil\n"
            "- Thematic Atlas: climate, population, economy\n"
            "- Historical Atlas: past maps and events\n"
            "- Road & Travel Atlas: highways, airports, routes\n"
            "- School Atlas: simplified maps for students"
        )
    elif data == 'quiz':
        start_quiz(update, context)

# --- Geography Quiz ---
quiz_questions = [
    {"question": "What is the capital of Kenya?", "answer": "Nairobi"},
    {"question": "Which continent has the Sahara Desert?", "answer": "Africa"},
    {"question": "Name a dendritic drainage pattern example.", "answer": "Mississippi"},
    {"question": "Which mountain is the highest in the world?", "answer": "Mount Everest"},
    {"question": "Which biome has lions and elephants?", "answer": "Savannah"}
]

def start_quiz(update: Update, context: CallbackContext) -> None:
    q = random.choice(quiz_questions)
    context.user_data['quiz_answer'] = q['answer']
    if update.callback_query:
        update.callback_query.edit_message_text(f"❓ Quiz: {q['question']}\nAnswer with /answer <your answer>")
    else:
        update.message.reply_text(f"❓ Quiz: {q['question']}\nAnswer with /answer <your answer>")

def answer(update: Update, context: CallbackContext) -> None:
    if 'quiz_answer' not in context.user_data:
        update.message.reply_text("Start a quiz first with /quiz")
        return
    user_ans = " ".join(context.args).strip().lower()
    correct_ans = context.user_data['quiz_answer'].lower()
    if user_ans == correct_ans:
        update.message.reply_text("✅ Correct! You are a Geography Genius!")
    else:
        update.message.reply_text(f"❌ Wrong! Correct answer: {context.user_data['quiz_answer']}")

# --- Aviation Module ---
def aviation(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "✈️ Aviation Geography:\n"
        "1. Major Airports: JFK, LHR, NRT, JNB\n"
        "2. Airlines: Air France, Emirates, Kenya Airways, Delta\n"
        "3. Air routes: Transatlantic, Transpacific, intra-continental\n"
        "4. Factors affecting flight paths: mountains, weather, air traffic control\n"
        "5. ICAO/IATA codes: airport & airline identifiers\n"
        "6. Aviation quiz: /aviation_quiz"
    )

aviation_quiz_questions = [
    {"question": "Which airport is the busiest in the world?", "answer": "Hartsfield–Jackson Atlanta"},
    {"question": "What is the IATA code for London Heathrow?", "answer": "LHR"},
    {"question": "Which airline is based in Dubai?", "answer": "Emirates"},
    {"question": "Which country has the most international airports?", "answer": "USA"},
    {"question": "Which airport is located in Nairobi?", "answer": "Jomo Kenyatta"}
]

def aviation_quiz(update: Update, context: CallbackContext) -> None:
    q = random.choice(aviation_quiz_questions)
    context.user_data['quiz_answer'] = q['answer']
    update.message.reply_text(f"❓ Aviation Quiz: {q['question']}\nAnswer with /answer <your answer>")

# --- Main ---
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(CommandHandler('quiz', start_quiz))
    dp.add_handler(CommandHandler('answer', answer))
    dp.add_handler(CommandHandler('aviation_quiz', aviation_quiz))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
