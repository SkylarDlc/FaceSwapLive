import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.model_zoo import model_zoo

# Inicializar detector de caras
app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

# Cargar modelo de face swap
swapper = insightface.model_zoo.get_model('C:/Users/Oleg/Documents/InsightFace_FaceSwapLive/models/inswapper_128.onnx', providers=['CPUExecutionProvider'])

# Leer imagen fuente
source_img = cv2.imread('C:/Users/Oleg/Documents/InsightFace_FaceSwapLive/source.jpg')
source_faces = app.get(source_img)
if not source_faces:
    raise RuntimeError("No se detectó rostro en la imagen fuente.")
source_face = source_faces[0]

# Abrir cámara web
cap = cv2.VideoCapture(0)

print("Presiona 'q' para cerrar.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = app.get(frame)
    for face in faces:
        try:
            frame = swapper.get(frame, face, source_face)
        except Exception as e:
            print(f"Error: {e}")

    cv2.imshow("Face Swap en Vivo", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
