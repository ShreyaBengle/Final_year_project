import time
import streamlit as st
from detectv8 import onButtonPressv8
from detect import onButtonPress

st.header("SignISLMed")


# # display the content of unique_classes.txt
# def display_unique_classes(stop_detection_placeholder):
#     # with open("/Users/adityadubey/Desktop/yolov5/runs/detect/exp35/unique_classes.txt", "r") as file:
#     with open("D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp31/unique_classes.txt", "r") as file:
#         unique_classes_content = file.read()
        
#     with stop_detection_placeholder.container():
#         st.text("Unique Classes:")
#         st.text(unique_classes_content)




def read_text_file_and_display_as_stream(stop_detection_placeholder):
    # Specify the file path
    file_path = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp35/unique_classes.txt"
    
    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file and convert to a single string
        words = file.read().split()

    def stream_words():
        for word in words:
            yield word + " "
            time.sleep(0.23)
    
    # Open a container in the specified placeholder
    with stop_detection_placeholder.container():
        # Write the words to the stream
        st.write_stream(stream_words())



# def read_text_file_and_display_as_stream(stop_detection_placeholder):
#     # Specify the file path
#     file_path = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp32/unique_classes.txt"
    
#     # Open the text file in read mode
#     with open(file_path, 'r') as file:
#         # Read the contents of the file and convert to a single string
#         words_string = " ".join(file.readlines()).strip()

#     # Open a container in the specified placeholder
#     with stop_detection_placeholder.container():
#         # Open a stream to write the words
#         with st.write_stream() as stream:
#             # Write the string to the stream
#             stream.write(words_string)


# def read_text_file_and_display_as_stream(stop_detection_placeholder):
#     # Specify the file path
#     file_path = "D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/runs/detect/exp27/unique_classes.txt"
    
#     # Open the text file in read mode
#     with open(file_path, 'r') as file:
#         # Read the contents of the file and convert to a single string
#         words_string = " ".join(file.readlines()).strip()

#     # Open a container in the specified placeholder
#     with stop_detection_placeholder.container():
#         # Split the string into individual words
#         words = words_string.split()

#         # Display the words progressively using st.text()
#         for word in words:
#             st.text(word)



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
    # display_unique_classes(stop_detection_placeholder)
    read_text_file_and_display_as_stream(stop_detection_placeholder)
     

with col2:
   st.header("YOLOV8")
   detectv8 = st.button("Start the detection(V8)")
   stopDetectv8 = st.button("Stop the detection", key="stop_v8")
   placeholderv8 = st.empty()
   if detectv8:
    onButtonPressv8(placeholderv8)




st.header("after the columns")
