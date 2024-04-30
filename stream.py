import streamlit as st
import os

def main():
    # Fixed folder path
    st.title("Image to Image Translation")
    folder_path = "./stargan_celeba_128/results"
    
    # List all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Display images
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        st.image(image_path, caption=image_file)

if __name__ == "__main__":
    main()
