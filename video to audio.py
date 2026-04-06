import moviepy.editor
video = moviepy.editor.VideoFileClip('C:\\Users\\pinku\OneDrive\\Documents\\vs code tutorial (1)\\Adhir Man full song Nilkanth Master _ Pooja Sawant-JLf2YK4Z_oc.mp4')
audio = video.audio
audio.write_audio('C:\\Users\\pinku\OneDrive\\Documents\\vs code tutorial (1)\\Adhir Man full song Nilkanth Master _ Pooja Sawant-JLf2YK4Z_oc.mp3')
