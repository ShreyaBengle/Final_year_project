import streamlit as st
from detectv8 import onButtonPressv8
from detect import onButtonPress

st.header("SignISLMed")


# display the content of unique_classes.txt
def display_unique_classes(stop_detection_placeholder):
    # with open("/Users/adityadubey/Desktop/yolov5/runs/detect/exp35/unique_classes.txt", "r") as file:
    with open("D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp22/unique_classes.txt", "r") as file:
        unique_classes_content = file.read()
        
    with stop_detection_placeholder.container():
        st.text("Unique Classes:")
        st.text(unique_classes_content)


col1, col2= st.columns(2, gap="large")

with col1:
   st.header("YOLOV5")
   detectv5 = st.button("Start the detection(V5)")
   stopDetectv5 = st.button("Stop the detection", key="stop_v5")
   placeholderv5 = st.empty()
   # Placeholder for the Stop Detection button
   stop_detection_placeholder = st.empty()

   if detectv5:
    onButtonPress(placeholderv5)
   if stopDetectv5:
    display_unique_classes(stop_detection_placeholder)
     

with col2:
   st.header("YOLOV8")
   detectv8 = st.button("Start the detection(V8)")
   stopDetectv8 = st.button("Stop the detection", key="stop_v8")
   placeholderv8 = st.empty()
   if detectv8:
    onButtonPressv8(placeholderv8)



