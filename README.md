# Object Segmentation and Identification System

This repository contains an Object Segmentation and Identification System with a fully interactive Streamlit GUI. The application enables users to upload images, automatically segment objects, assign unique IDs, label the objects, and maintain a database for easy retrieval and management.

## Features

- **Image Upload**: Users can browse and upload images through the Streamlit interface.
- **Object Segmentation**: The model segments objects in the uploaded image.
- **Unique ID Assignment**: Each segmented object is assigned a unique ID.
- **Object Extraction**: Each segmented object is extracted and stored as a seperate .png file.
- **Text Extraction**: Any text present in the image can be extracted from the image.
- **Database Management**: A database is maintained to store and manage segmented objects.
- **Object Identification and Labeling**: The system identifies and labels objects within the image.

## Installation

 Clone the repository:
   ```bash
   git clone https://github.com/pratham-asthana/object-segmentation-identification-system.git
  ```
## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
2. Upload an image using the provided interface.
3. View the segmented objects, their unique IDs, and labels.
4. Access and manage the object database as needed.


### Project Structure

```markdown
## Project Structure

object-segmentation-identification-system/ ├── app.py # Main Streamlit application ├── segmentation_model.py # Object segmentation model ├── database.py # Database management script ├── utils.py # Utility functions ├── requirements.txt # List of dependencies └── README.md
```

## Technologies Used

- Python
- Streamlit
- OpenCV
- Pytesseract
- TensorFlow/PyTorch (depending on the segmentation model used)
- Image (from PIL)
- SQLite (or any database of choice)

## Contact

For any inquiries or suggestions, feel free to reach out:

- **Name**: Pratham Asthana
- **Email**: [prathamasthana04@gmail.com](mailto:prathamasthana04@gmail.com)
- **LinkedIn**: [Pratham Asthana](https://www.linkedin.com/in/pratham-asthana-243133265/)

## Contribution

Contributions are welcome! If you would like to improve this project or report any issues, feel free to fork the repository and submit a pull request. Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your forked repository.
5. Submit a pull request to the main branch of this repository.

Thank you for your contributions!
