# PBR-API (Puzzle Battle Royale)

This repository contains the server-side API for the [Puzzle Battle Royale (PBR)](https://github.com/SamuelSoNChino/PBR) game. The API is built using Flask and is responsible for matchmaking, as well as generating unique puzzle images and grids for the game. The API integrates with Unity Relay for matchmaking and ensures that each puzzle is solvable yet unique for every game match.


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
- **Example 1**: Puzzle image generated with `image_size=1000`, `number_of_tiles=6` and `seed=9`
![1000x1000, 6x6 Puzzle Image](/assets/image_showcase1.png)
- **Example 2**: Same puzzle image with the grid lines overlay to showcase solvability (Every tile is sharing at least one shape with another tile)
![1000x1000, 6x6 Puzzle Image with grid lines](/assets/image_showcase2.png)

### 6. Generate Grid

- **URL**: `/generate_grid`
- **Method**: `GET`
- **Parameters**:
    - `image_size` (int): Size of the image in pixels.
    - `number_of_tiles` (int): Number of tiles in the grid.
- **Response**: A PNG image.
- **Description**: Generates a grid overlay for the puzzle.
- **Example**: Grid generated with `image_size=1000` and `number_of_tiles=6`
![1000x1000, 6x6 Example grid](/assets/grid_showcase.png)

## Project Structure

    📂 PBR-API/
    ├── main.py                  # Flask application entry point
    ├── GeoShapesGenerator.py    # Generates puzzle images with geometric shapes
    ├── GridGenerator.py         # Generates grids for the puzzles
    └── requirements.txt         # Python dependencies (optional)

## Code Overview

The API backend consists of three main files:

### 1. `main.py`
- **Purpose**: Serves as the entry point for the Flask application. It defines the API endpoints responsible for matchmaking and puzzle generation.
- **Technologies Used**:
    - **Flask**: Lightweight web framework for handling HTTP requests.
    - **OpenCV**: Used for encoding images into byte arrays before serving them.
    - **Unity Relay Integration**: Facilitates matchmaking by storing and managing player join codes.

### 2. `GridGenerator.py`
- **Purpose**: Generates grid overlays for puzzle boards with configurable sizes and styles (lines or circles).
- **Technologies** Used:
    - **NumPy**: Creates and manipulates numerical arrays for the grid's structure.
    - **OpenCV**: Renders the grid as an image with customizable colors, dimensions, and shapes.
- **Key Features**:
    - Configurable grid size and tile count.
    - Supports line-based and circle-based grid styles.

### `GeoShapesGenerator.py`
- **Purpose**: Dynamically creates unique puzzle images consisting of geometric shapes, ensuring solvability and randomness.
- **Technologies Used**:
    - **OpenCV**: Draws shapes like circles, squares, and triangles on the puzzle image.
    - **NumPy**: Structures the puzzle’s layout and ensures it adheres to specific constraints.
    - **Random Module**: Adds variability to shape placement, size, and color.
- **Key Features**:
    - Adjustable puzzle size and complexity based on the number of tiles.
    - Supports multiple shapes and colors to ensure visual diversity.
    - Ensures tiles are solvable and avoids excessive overlap.
