import streamlit as st
import random

st.set_page_config(page_title="Love Message Generator", page_icon="💖")

# ------------------------
# MESSAGE DATABASE
# ------------------------

romantic_messages = [
    "You are my favorite notification.",
    "Every moment with you feels like magic.",
    "If love had a face, it would look like you.",
    "You make my world brighter every single day.",
    "Loving you is the easiest thing I've ever done.",
]

funny_messages = [
    "I love you more than shawarma... and that's serious.",
    "You're the only person I'd share my last fries with.",
    "You stole my heart, but honestly... keep it.",
    "Even my WiFi connects faster when you're around.",
    "You are proof that God has a sense of humor and good taste.",
]

flirty_messages = [
    "Stop being this attractive, it's distracting.",
    "You should come with a warning label.",
    "I was productive before I met you.",
    "Your smile should honestly be illegal.",
    "I blame you for my lack of concentration.",
]

apology_messages = [
    "I'm sorry for hurting you. You mean more to me than my pride ever will.",
    "I messed up, and I truly regret it.",
    "Please forgive me. My world feels incomplete without you.",
    "I never wanted to make you sad.",
    "I'm sorry, stubborn queen 👑❤️",
]

emotional_messages = [
    "No matter how hard life gets, having you beside me makes it easier.",
    "You are the peace my heart searched for.",
    "I never believed in soulmates until I met you.",
    "Sometimes I look at you and wonder how I got so lucky.",
    "You are the best chapter in my story.",
]

# ------------------------
# MESSAGE GENERATION
# ------------------------

creative_templates = [
    "{name}, you're the {adjective} part of my {noun}.",
    "Whenever I think of you, I feel like {metaphor}.",
    "Your {feature} makes every day feel {feeling}.",
    "I never knew words could sparkle until I met you.",
    "If I could bottle the way I feel about you, it would be {adjective} and timeless.",
    "You are the {noun} I never knew my heart needed.",
    "I love the way you {habit}; it makes ordinary moments unforgettable.",
    "Your laugh is my favorite sound, and your smile is my favorite sight.",
    "Every time you appear in my mind, the world gets a little kinder.",
    "Just a reminder: you're more amazing than any story could ever capture.",
]

adjectives = [
    "brightest", "sweetest", "warmest", "sparkling", "wildest", "gentlest",
    "most dazzling", "softest", "boldest", "most delightful",
]

nouns = [
    "day", "dream", "sunrise", "midnight", "adventure", "song",
    "secret", "storybook", "garden", "wonder"
]

metaphors = [
    "a sunrise that never ends", "a comet streaking through the quiet sky",
    "a melody I want on repeat", "a warm fire on a winter night",
    "a whisper of magic in the middle of ordinary life",
]

features = [
    "smile", "eyes", "laugh", "voice", "kindness", "thoughtfulness",
    "the way you listen", "your hugs", "your creativity", "your energy"
]

feelings = [
    "brighter", "easier", "more enchanted", "safer", "fuller", "more playful",
    "like home", "more hopeful", "untouched by time", "truly alive",
]

habits = [
    "dance when no one is watching", "make coffee with extra care",
    "text me first thing in the morning", "leave me little notes",
    "tell me the truth", "laugh at my bad jokes",
]

message_pools = [
    romantic_messages,
    funny_messages,
    flirty_messages,
    apology_messages,
    emotional_messages,
]


def generate_creative_message(name: str) -> str:
    if random.random() < 0.35:
        template = random.choice(creative_templates)
        message = template.format(
            name=name or "",
            adjective=random.choice(adjectives),
            noun=random.choice(nouns),
            metaphor=random.choice(metaphors),
            feature=random.choice(features),
            feeling=random.choice(feelings),
            habit=random.choice(habits),
        ).strip()
    else:
        pool = random.choice(message_pools)
        message = random.choice(pool)

    if name and "{name}" not in message:
        message = f"{name}, {message}"

    return message

# ------------------------
# UI DESIGN
# ------------------------

st.title("💖 Love Message Generator")
st.write("The app writes a fresh, creative love message for you on every refresh.")

name = st.text_input("Enter your partner's name (optional):")

if st.button("Generate another message"):
    pass

message = generate_creative_message(name)
st.success(message)

st.caption("Made with ❤️ using Python + Streamlit")