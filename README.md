# PBR API (Puzzle Battle Royale)

This repository contains the server-side API for the Puzzle Battle Royale (PBR) game. The API is built using Flask and is responsible for matchmaking, as well as generating unique puzzle images and grids for the game. The API integrates with Unity Relay for matchmaking and ensures that each puzzle is solvable yet unique for every game match.


## Features

- **Matchmaking**: Handles player matchmaking and integration with Unity Relay.
- **Dynamic Puzzle Generation**: Generates unique puzzle images and grids for each match, ensuring solvability.
- **Lightweight Server**: Flask-based API with simple endpoints for easy integration with Unity.

## Requirements

### Python Dependencies

- Python 3.8+
- Flask
- OpenCV (cv2)
- NumPy

Install the dependencies using pip:


    pip install flask opencv-python numpy

or 

    pip install -r requirements.txt

## API Endpoints
### 1. Test Connection

- **URL**: `/test_connection`
- **Method**: `GET`
- **Response**: `"OK"`
- **Description**: Simple health check to ensure the server is running.

### 2. Request Match

- **URL**: `/request_match`
- **Method**: `GET`
- **Parameters**:
    - `number_of_players` (int): Number of players in the match (2–10).
- **Responses**:
    - `"CLIENT,<join_code>"`: Joins an existing match as a client.
    - `"HOST"`: Becomes the host of a new match.
    - `"INVALID PLAYER COUNT"`: If the number of players is not between 2 and 10.
- **Description**: Handles matchmaking by assigning players to a host or an available match.

### 3. Upload Relay Join Code

- **URL**: `/upload_relay_join_code`
- **Method**: `GET`
- **Parameters**:
    - `relay_join_code` (string): The Unity Relay join code for the match.
    - `number_of_players` (int): Number of players in the match.
- **Response**: `"OK"`
- **Description**: Hosts upload the Unity Relay join code for their match.

### 4. Request Join Code Removal

- **URL**: `/request_join_code_removal`
- **Method**: `GET`
- **Parameters**:
    - `number_of_players` (int): Number of players in the match.
- **Response**: `"OK"`
- **Description**: Removes a match's join code when it is no longer needed.

### 5. Generate Puzzle Image

- **URL**: `/generate_image`
- **Method**: `GET`
- **Parameters**:
    - `image_size` (int): Size of the image in pixels.
    - `number_of_tiles` (int): Number of tiles in the puzzle.
    - `seed` (int): Seed value for reproducibility.
- **Response**: A PNG image.
- **Description**: Generates a unique puzzle image based on geometric shapes.

### 6. Generate Grid

- **URL**: `/generate_grid`
- **Method**: `GET`
- **Parameters**:
    - `image_size` (int): Size of the image in pixels.
    - `number_of_tiles` (int): Number of tiles in the grid.
- **Response**: A PNG image.
- **Description**: Generates a grid overlay for the puzzle.

## Project Structure

    📂 PBR-API/
    ├── main.py                  # Flask application entry point
    ├── GeoShapesGenerator.py    # Generates puzzle images with geometric shapes
    ├── GridGenerator.py         # Generates grids for the puzzles
    └── requirements.txt         # Python dependencies (optional)

Code Overview
1. GeoShapesGenerator.py

    Purpose: Creates a puzzle image with unique geometric shapes.
    Key Features:
        Supports circles, squares, and triangles.
        Ensures shapes are distributed across tiles.
        Uses seed values for reproducible results.

2. GridGenerator.py

    Purpose: Generates a grid overlay for the puzzle image.
    Key Features:
        Supports customizable grid sizes.
        Options for grid lines and circular overlays.

3. main.py

    Purpose: Flask application managing API endpoints.
    Key Features:
        Matchmaking logic with Unity Relay integration.
        Image generation endpoints for puzzles and grids.