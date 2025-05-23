# DIAV - Digital Identity and Asset Vault using Blockchain

A simple and secure web application for managing digital assets using blockchain technology.

## Features
- Decentralized secure immutable asset storage using blockchain
- Support for various types of digital assets- docs, pdfs, images, excel.
- Proof of Work consensus mechanism
- User-friendly web interface

## Implementation Steps

### Prerequisites
- Python installed on your system

### Setup and Run Instructions

1. Open VS Code and set up a split terminal (Left and Right)

2. In the Left Terminal:
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   python peer.py
   ```

3. In the Right Terminal:
   ```bash
   python run_app.py
   ```

4. Click the link from the client(right) terminal to access the application. 
   (Note: peer.py and run_app.py are running on different ports to avoid collision).

5. Enter user name -> Select File -> click Uplaod -> click "Request to Mine". The file gets stored in the blockchain.
   Go back and refresh the page to see the uplaoded files.

6. Open a new terminal to run the Proof of Work comparison:
   ```bash
   python POW_Comparison.py
   ```



## Technical Details

The application uses:
- SHA256 cryptographic algorithm for block security
- Proof of Work consensus mechanism with difficulty level upto 3
- Flask for the web interface

