# CCL-Demo
 This project is built as part of a technical test for CCL Group
 
## Setup and Installation
The application will prompt for a postcode. Enter a valid postcode to retrieve addresses. and Type 'exit' to quit the application.
## Running the Application
Ensure MongoDB is running and your environment variables are set.
- To Run This Application:
  ```bash
  python app.py
  ```
### 1. Install MongoDB
To use the application, MongoDB needs to be installed and running. 
- Install MongoDB using Homebrew (macOS):
  ```bash
  brew tap mongodb/brew
  ```
  ```bash
  brew install mongodb-community
  ```
- To start MongoDB:
  ```bash
  brew services start mongodb/brew/mongodb-community
  ```
- To stop MongoDB:
  ```bash
  brew services stop mongodb/brew/mongodb-community
  ```

### 2. Set Up Python Virtual Environment
The project uses a Python virtual environment to manage dependencies.

- Create a virtual environment:
  ```bash
  python3 -m venv postcode
  ```
- Activate the virtual environment:
  ```bash
  source postcode/bin/activate
  ```
### 3. Install Python Dependencies
- Install dependencies using pip:
  ``` bash
  pip install -r requirements.txt 
  ```
### 4. Environment Variables
Create a `.env` file in the root folder and add the following environment variables:
- `DATABASE_URI`: Your MongoDB connection URI.
- `Example` : DATABASE_URI=mongodb://localhost:27017/
- `API_KEY`: Your API key for getaddress.io.
- `Example` : API_KEY=your_api_key_here

