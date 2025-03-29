from deepface import DeepFace
img = "/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg","Learn/Opencv-python/Zoro_gray.jpeg"

result = DeepFace.analyze(img_path="/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg", actions=['age', 'gender', 'emotion', 'race'])
print(result)