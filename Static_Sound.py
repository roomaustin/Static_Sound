from pydub import AudioSegment
from pydub.generators import WhiteNoise

# Create a white noise generator
white_noise = WhiteNoise()

# Generate 10 seconds of static noise
static_noise = white_noise.to_audio_segment(duration=10000)

# Export the static noise as an audio file
static_noise.export("static_noise.wav", format="wav")

# Play the static noise (optional, requires additional setup)
# static_noise.export("/dev/audio", format="wav")  # Unix-like systems
# static_noise.export("your_audio_device_name", format="wav")  # Windows
