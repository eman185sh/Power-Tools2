from playsound import playsound

try:
    playsound("success.mp3")
    print("Sound played successfully!")
except Exception as e:
    print(f"Could not play sound: {e}")
    print("Make sure you have a 'success.mp3' file in your project directory.")