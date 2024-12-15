pip install streamlit openai pyngrok
import streamlit as st
import openai  # To use OpenAI's API for story generation

# --- Configure OpenAI API key ---
openai.api_key = "your_openai_api_key"  # Replace 'your_openai_api_key' with your OpenAI API key

# --- Streamlit App Title and Description ---
st.title("📚 AI Story Generator")
st.write("Enter a story title or topic, and let the AI create a magical story for you! ✨")

# --- Input Field for Story Title / Topic ---
story_topic = st.text_input("Enter a story title or topic:")

# --- Button to Generate the Story ---if st.button("📝 Generate Story"):
if story_topic.strip() == "":
        st.warning("⚠️ Please enter a story title or topic.")
else:
        with st.spinner("Generating your story... ✍️"):
            try:
                # Call OpenAI API to generate a story
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Use GPT-4 or GPT-3.5 model
                    messages=[
                        {"role": "system", "content": "You are a creative storyteller."},
                        {"role": "user", "content": f"Write a short story about: {story_topic}"}
                    ],
                    max_tokens=500  # Length of the story
                )

                # Extract the AI's response (the generated story)
                story = response['choices'][0]['message']['content']

                # Display the Story
                st.subheader("📖 Your AI-Generated Story")
                st.write(story)

                # --- Download Button for the Story ---
                st.download_button('📥 Download Story as TXT', story, file_name="story.txt")

            except Exception as e:
                st.error(f"❌ An error occurred while generating the story: {e}")
