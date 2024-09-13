import os
from openai import OpenAI

def generate_conversation(request):
    # Extract the 'topic' from the incoming request, default to 'technology' if not provided
    request_json = request.get_json(silent=True)
    topic = request_json.get('topic', 'technology')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    try:
        # Log the topic for debugging
        print(f"Topic received: {topic}")

        # Use the GPT-3.5-turbo model from OpenAI's API
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Make a short two person dialogue about {topic}"
                }
            ],
            model="gpt-3.5-turbo",
        )
        # Retrieve the generated conversation
        script = response.choices[0].message.content.strip()

        # Log the generated conversation for debugging
        print(f"Generated conversation: {script}")

        return {'conversation': script}

    except Exception as e:
        # Log the error for debugging
        print(f"Error occurred: {str(e)}")

        # Return an error message in case of failure
        return {'error': str(e)}, 500