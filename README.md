# Metadata Generator

This script generates a collection of NFTs by creating JSON files and PNG images for your Solana collection. It will only use 1 image so this is intended for a collection all with the same art/image. It takes user input for various parameters such as collection size, collection name, collection symbol, collection description, image location, external URL, trait types, trait values, and creator information. The JSON files contain metadata for each NFT, including the image, name, symbol, description, and attributes.<br><br>

### <u>Requirements</u><br><br>

- Python 3.x
- PIL (Python Imaging Library)<br><br>

## <u>Installation and Setup</u><br><br>

<u>Windows</u><br>

- Go to the Python download page and download the latest version of Python for Windows.

- Run the installer and follow the prompts to install Python.

- Once installed, open a Command Prompt window and type python to check if Python is installed correctly. You should see the Python version number displayed.

- Optionally, you can add Python to your PATH environment variable so you can use it from any directory in the Command Prompt. To do this, follow these steps:

  - Right-click on the "This PC" icon on your desktop and select "Properties".

  - Click "Advanced system settings".

  - Click "Environment Variables".
  - Under "System variables", scroll down to "Path" and click "Edit".
  - Click "New" and add the path to your Python installation directory (e.g. C:\Python39).
  - Click "OK" to save the changes.

<u>Mac</u><br>

- Go to the Python download page and download the latest version of Python for Mac.

- Run the installer and follow the prompts to install Python.

- Once installed, open a Terminal window and type python to check if Python is installed correctly. You should see the Python version number displayed.

- Optionally, you can create an alias in your .bash_profile file so you can use Python from any directory in the Terminal. To do this, follow these steps:

  - Open Terminal and type nano ~/.bash_profile to open your bash profile in the nano text editor.
  - Add the following line to the bottom of the file: alias python="/usr/local/bin/python3"
  - Press Ctrl+O to save the file, and then Ctrl+X to exit nano.
  - Restart Terminal or type source ~/.bash_profile to refresh the bash profile.
  - Install PIL using pip: pip install pillow

  - Clone the repository to your local machine.

  - Place your image file in the root directory of the repository.<br><br>

### <u>Clone the repository to your local machine:</u><br><br>

- Go to the GitHub repository page and click the green "Code" button.
- Select "Download ZIP" to download the repository as a zip file, or copy the repository's clone URL.
- If you downloaded the repository as a zip file, extract the contents to a folder on your computer.
- If you copied the clone URL, open a terminal or command prompt and navigate to the directory where you want to clone the repository.
- Type git clone followed by the clone URL and press Enter.<br><br>

### <u>Install dependencies:</u><br><br>

- Open a terminal or command prompt and navigate to the root directory of the repository.
- Run pip install -r requirements.txt to install the required Python packages.<br><br>

## <u>Usage</u><br><br>

- Open a terminal or command prompt and navigate to the root directory of the repository.

- Run the script: python metaDataGenerator.py

- Follow the prompts to input the required information.

- The script will create a folder named "images" and a folder named "json_files" to store the generated images and JSON files, respectively.

- If any files fail to generate, the script will retry those files at the end.<br><br>

## <u>Input Parameters</u><br><br>

The script will prompt for the following information:

- Collection size: The number of NFTs to generate.

- Collection name: The name of the collection.

- Collection symbol: The symbol for the collection (e.g. SOL, ETH).

- Collection description: A brief description of the collection.

- Royalties percentage: The percentage of royalties to be paid to creators.

- Image file: The location of the image file to use as the base image for the NFTs.

- External URL (optional): An optional external URL for the collection.

- Number of traits: The number of traits to be associated with each NFT.

- Trait type: The type of each trait (e.g. head, background).

- Trait value: The value of each trait (e.g. red, blue).

- Number of creators: The number of creators for royalties wallets associated with the collection.

- Creator address: The wallet address of each creator.

- Creator share: The percentage of royalties to be paid to each creator.<br><br>

## <u>Output</u>

The script will generate PNG images and JSON files for each NFT in the collection, and store them in the "images" and "json_files" folders, respectively. The JSON files contain metadata for each NFT, including the name, symbol, description, image, external URL (if provided), attributes, and creator information.
